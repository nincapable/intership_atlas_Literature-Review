#!/usr/bin/env python3
"""Export SMA input data from an RDF knowledge graph to simulator-facing CSV."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import RDF

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from generate_sma_queries import DEFAULT_NAMESPACES, INPUT_CSV_COLUMNS, SimulationProfile, load_profile, qname  # noqa: E402


def bind_default_namespaces(graph: Graph) -> None:
    for prefix, namespace in DEFAULT_NAMESPACES:
        graph.bind(prefix, namespace)


def parse_graph(path: Path, rdf_format: str | None = None) -> Graph:
    graph = Graph()
    bind_default_namespaces(graph)
    graph.parse(path, format=rdf_format or guess_format(path))
    return graph


def guess_format(path: Path) -> str | None:
    suffix = path.suffix.lower()
    if suffix in {'.ttl', '.turtle'}:
        return 'turtle'
    if suffix in {'.nt'}:
        return 'nt'
    if suffix in {'.rdf', '.xml'}:
        return 'xml'
    if suffix in {'.jsonld', '.json'}:
        return 'json-ld'
    return None


def expand_term(value: str, prefixes: dict[str, str]) -> URIRef:
    if value.startswith('<') and value.endswith('>'):
        return URIRef(value[1:-1])
    if value.startswith('http://') or value.startswith('https://'):
        return URIRef(value)
    if ':' in value:
        prefix, local = value.split(':', 1)
        if prefix in prefixes:
            return URIRef(prefixes[prefix] + local)
    raise ValueError(f'Cannot expand RDF term {value!r}; use a known QName or absolute URI')


def object_to_csv(graph: Graph, obj: URIRef | Literal | BNode) -> tuple[str, str, str]:
    if isinstance(obj, URIRef):
        return qname(graph, obj), 'uri', ''
    if isinstance(obj, Literal):
        datatype = qname(graph, obj.datatype) if isinstance(obj.datatype, URIRef) else ''
        return str(obj), datatype, obj.language or ''
    if isinstance(obj, BNode):
        return f'_:{obj}', 'bnode', ''
    return str(obj), '', ''


def export_rows(profile: SimulationProfile, data_graph: Graph) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    class_terms = [(class_name, expand_term(class_name, profile.prefixes)) for class_name in profile.required_classes]
    property_terms = [(prop_name, expand_term(prop_name, profile.prefixes)) for prop_name in profile.all_input_properties]

    for class_name, class_uri in class_terms:
        for entity in sorted(data_graph.subjects(RDF.type, class_uri), key=str):
            if not isinstance(entity, (URIRef, BNode)):
                continue
            entity_value = qname(data_graph, entity) if isinstance(entity, URIRef) else f'_:{entity}'
            for property_name, property_uri in property_terms:
                for obj in sorted(data_graph.objects(entity, property_uri), key=str):
                    value, value_type, value_lang = object_to_csv(data_graph, obj)
                    rows.append({
                        'entity': entity_value,
                        'class': class_name,
                        'property': property_name,
                        'value': value,
                        'value_type': value_type,
                        'value_lang': value_lang,
                    })
    return rows


def write_input_csv(profile_path: Path, data_path: Path, out_path: Path, rdf_format: str | None = None) -> Path:
    profile = load_profile(profile_path)
    data_graph = parse_graph(data_path, rdf_format)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=INPUT_CSV_COLUMNS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(export_rows(profile, data_graph))
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description='Export SMA initialization data from RDF to CSV.')
    parser.add_argument('--profile', type=Path, required=True, help='Path to a fe:SimulationProfile TTL file')
    parser.add_argument('--data', type=Path, required=True, help='Path to RDF data to export')
    parser.add_argument('--out', type=Path, required=True, help='Output CSV path')
    parser.add_argument('--format', dest='rdf_format', default=None, help='Optional rdflib input format, e.g. turtle')
    args = parser.parse_args()

    try:
        path = write_input_csv(args.profile, args.data, args.out, args.rdf_format)
    except Exception as exc:
        raise SystemExit(str(exc)) from exc
    print(f'Generated {path}')


if __name__ == '__main__':
    main()
