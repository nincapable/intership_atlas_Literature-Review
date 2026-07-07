#!/usr/bin/env python3
"""Generate SPARQL and CSV mapping artifacts from fe:SimulationProfile RDF files.

The user-facing contract stays intentionally simple: a researcher declares what a
SMA reads and writes in a Turtle profile. Internally, this script uses rdflib so
that profiles are parsed as RDF graphs instead of fragile text snippets. CSV is
then used as the external exchange format with simulators.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass, field
from io import StringIO
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF

FE = Namespace('http://example.org/fire_and_evacuation#')

DEFAULT_NAMESPACES: tuple[tuple[str, str], ...] = (
    ('fe', 'http://example.org/fire_and_evacuation#'),
    ('crm', 'http://www.cidoc-crm.org/cidoc-crm/'),
    ('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
    ('rdfs', 'http://www.w3.org/2000/01/rdf-schema#'),
    ('owl', 'http://www.w3.org/2002/07/owl#'),
    ('xsd', 'http://www.w3.org/2001/XMLSchema#'),
)

INPUT_CSV_COLUMNS = ['entity', 'class', 'property', 'value', 'value_type', 'value_lang']
RESULT_CSV_COLUMNS = ['run_id', 'scenario_id', 'input_id', 'output_id', 'entity', 'step', 'time', 'property', 'value', 'value_type']


@dataclass(frozen=True)
class SimulationProfile:
    """RDF-backed contract describing what a SMA consumes and produces."""

    uri: URIRef
    identifier: str
    root_class: str | None
    required_classes: list[str]
    required_properties: list[str]
    optional_properties: list[str]
    produced_classes: list[str]
    produced_properties: list[str]
    prefixes: dict[str, str]
    expand_properties: list[str] = field(default_factory=list)
    expand_classes: list[str] = field(default_factory=list)
    max_depth: int | None = None

    @property
    def all_input_properties(self) -> list[str]:
        return unique_preserve_order(self.required_properties + self.optional_properties)


@dataclass(frozen=True)
class GeneratedQueries:
    init_construct: str
    init_select: str
    result_insert: str


@dataclass(frozen=True)
class GeneratedArtifacts:
    init_construct: Path
    init_select: Path
    result_insert: Path
    input_mapping: Path
    output_mapping: Path
    result_example_csv: Path


def unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def generated_name(profile_path: Path, profile_id: str) -> str:
    if profile_id:
        return re.sub(r'[^A-Za-z0-9_\-]+', '_', profile_id)
    return profile_path.stem


def qname(graph: Graph, value: URIRef) -> str:
    """Return a SPARQL-friendly QName when possible, otherwise a bracketed IRI."""
    return graph.namespace_manager.normalizeUri(value)


def literal_string(graph: Graph, subject: URIRef, predicate: URIRef, default: str) -> str:
    value = graph.value(subject, predicate)
    if isinstance(value, Literal):
        return str(value)
    return default


def int_value(graph: Graph, subject: URIRef, predicate: URIRef) -> int | None:
    value = graph.value(subject, predicate)
    if value is None:
        return None
    try:
        parsed = int(value.toPython() if isinstance(value, Literal) else str(value))
    except (TypeError, ValueError):
        raise ValueError(f'{qname(graph, predicate)} must be an integer literal') from None
    if parsed < 0:
        raise ValueError(f'{qname(graph, predicate)} must be greater than or equal to 0')
    return parsed


def uri_values(graph: Graph, subject: URIRef, predicate: URIRef) -> list[str]:
    values: list[str] = []
    for value in graph.objects(subject, predicate):
        if isinstance(value, URIRef):
            values.append(qname(graph, value))
    return unique_preserve_order(values)


def namespace_is_used(graph: Graph, namespace: str) -> bool:
    for subject, predicate, obj in graph:
        if str(subject).startswith(namespace) or str(predicate).startswith(namespace):
            return True
        if isinstance(obj, URIRef) and str(obj).startswith(namespace):
            return True
    return False


def prefixes_from_graph(graph: Graph) -> dict[str, str]:
    prefixes = {prefix: iri for prefix, iri in DEFAULT_NAMESPACES}
    for prefix, namespace in graph.namespaces():
        if prefix and namespace_is_used(graph, str(namespace)):
            prefixes[str(prefix)] = str(namespace)
    return prefixes


def format_prefixes(prefixes: dict[str, str]) -> str:
    default_prefix_names = {prefix for prefix, _ in DEFAULT_NAMESPACES}
    ordered: list[tuple[str, str]] = []
    for prefix, iri in DEFAULT_NAMESPACES:
        ordered.append((prefix, prefixes.get(prefix, iri)))
    for prefix in sorted(prefixes):
        if prefix not in default_prefix_names:
            ordered.append((prefix, prefixes[prefix]))
    return '\n'.join(f'PREFIX {prefix}:{" " * max(1, 5 - len(prefix))}<{iri}>' for prefix, iri in ordered)


def find_profile_subject(graph: Graph, profile_path: Path) -> URIRef:
    profiles = sorted(
        (subject for subject in graph.subjects(RDF.type, FE.SimulationProfile) if isinstance(subject, URIRef)),
        key=str,
    )
    if not profiles:
        raise ValueError(f'No fe:SimulationProfile resource found in {profile_path}')
    if len(profiles) > 1:
        labels = ', '.join(qname(graph, profile) for profile in profiles)
        raise ValueError(f'Multiple fe:SimulationProfile resources found in {profile_path}: {labels}')
    return profiles[0]


def load_profile(profile_path: Path) -> SimulationProfile:
    """Load a Turtle fe:SimulationProfile as RDF and expose its simple contract."""
    graph = Graph()
    graph.parse(profile_path, format='turtle')

    subject = find_profile_subject(graph, profile_path)
    identifier = literal_string(graph, subject, FE.profileIdentifier, profile_path.stem)
    root = graph.value(subject, FE.hasRootClass)
    root_class = qname(graph, root) if isinstance(root, URIRef) else None

    profile = SimulationProfile(
        uri=subject,
        identifier=identifier,
        root_class=root_class,
        required_classes=uri_values(graph, subject, FE.requiresClass),
        required_properties=uri_values(graph, subject, FE.requiresProperty),
        optional_properties=uri_values(graph, subject, FE.optionalProperty),
        produced_classes=uri_values(graph, subject, FE.producesClass),
        produced_properties=uri_values(graph, subject, FE.producesProperty),
        prefixes=prefixes_from_graph(graph),
        expand_properties=uri_values(graph, subject, FE.expandProperty),
        expand_classes=uri_values(graph, subject, FE.expandClass),
        max_depth=int_value(graph, subject, FE.maxDepth),
    )

    if not profile.required_classes:
        raise ValueError(f'No fe:requiresClass values found in {profile_path}')
    return profile


def format_values(values: list[str], indent: str = '    ') -> str:
    return '\n'.join(f'{indent}{value}' for value in values)


def generate_flat_construct(profile: SimulationProfile, template: str, input_iri: str) -> str:
    return template.format(
        PREFIXES=format_prefixes(profile.prefixes),
        CLASS_VALUES=format_values(profile.required_classes),
        PROPERTY_VALUES=format_values(profile.all_input_properties),
        INPUT_IRI=input_iri,
    )


def generate_deep_construct(profile: SimulationProfile, template: str | None = None, input_iri: str | None = None) -> str:
    """
    Generate a future deep CONSTRUCT query that follows selected RDF links.

    If the profile does not declare fe:expandProperty and fe:maxDepth, this keeps
    the current flat CONSTRUCT behavior. When both are present, it emits a simple
    property-path expansion over the declared properties up to the requested depth.
    """
    if not profile.expand_properties or not profile.max_depth:
        if template is None or input_iri is None:
            raise ValueError('template and input_iri are required for flat CONSTRUCT generation')
        return generate_flat_construct(profile, template, input_iri)

    depth = profile.max_depth
    prefixes = format_prefixes(profile.prefixes)
    expand_values = format_values(profile.expand_properties)
    class_values = format_values(profile.required_classes)
    property_values = format_values(profile.all_input_properties)
    input_line = f'{input_iri} a fe:SimulationInput ;\n      fe:describesEntity ?entity .'

    path_patterns = []
    for level in range(1, depth + 1):
        source = '?entity' if level == 1 else f'?node{level - 1}'
        target = f'?node{level}'
        path_patterns.append(f'  OPTIONAL {{ {source} ?expandProperty {target} . }}')
    path_where = '\n'.join(path_patterns)
    construct_nodes = '\n'.join(
        f'  ?node{level} ?property ?value{level} .' for level in range(1, depth + 1)
    )
    optional_node_values = '\n'.join(
        f'  OPTIONAL {{ ?node{level} ?property ?value{level} . }}' for level in range(1, depth + 1)
    )

    return f"""# Generated from a fe:SimulationProfile.
# Deep extraction prototype following fe:expandProperty up to fe:maxDepth.
{prefixes}

CONSTRUCT {{
  ?entity a ?class .
  ?entity ?property ?value .
{construct_nodes}
  {input_line}
}}
WHERE {{
  VALUES ?class {{
{class_values}
  }}

  VALUES ?property {{
{property_values}
  }}

  VALUES ?expandProperty {{
{expand_values}
  }}

  ?entity a ?class .
  OPTIONAL {{ ?entity ?property ?value . }}
{path_where}
{optional_node_values}
}}
"""


def generate_queries(profile: SimulationProfile, template_dir: Path, input_iri: str) -> GeneratedQueries:
    init_template = (template_dir / 'sma_init_construct_template.sparql').read_text(encoding='utf-8')
    select_template = (template_dir / 'sma_init_select_template.sparql').read_text(encoding='utf-8')
    result_template = (template_dir / 'sma_result_insert_template.sparql').read_text(encoding='utf-8')

    init_query = generate_deep_construct(profile, init_template, input_iri)
    select_query = select_template.format(
        PREFIXES=format_prefixes(profile.prefixes),
        CLASS_VALUES=format_values(profile.required_classes),
        PROPERTY_VALUES=format_values(profile.all_input_properties),
    )
    produced_hints = '\n'.join(f'    # - {prop}' for prop in profile.produced_properties)
    if not produced_hints:
        produced_hints = '    # - no produced properties declared'
    result_query = result_template.format(
        PREFIXES=format_prefixes(profile.prefixes),
        PRODUCED_PROPERTY_HINTS=produced_hints,
    )
    return GeneratedQueries(init_query, select_query, result_query)


def input_mapping(profile: SimulationProfile, input_csv_name: str) -> dict[str, object]:
    return {
        'profile': profile.identifier,
        'input_csv': input_csv_name,
        'columns': [
            {'name': 'entity', 'role': 'subject', 'type': 'uri'},
            {'name': 'class', 'role': 'rdf_class', 'type': 'uri'},
            {'name': 'property', 'role': 'predicate', 'type': 'uri'},
            {'name': 'value', 'role': 'object', 'type': 'mixed'},
            {'name': 'value_type', 'role': 'datatype_or_uri', 'type': 'string'},
            {'name': 'value_lang', 'role': 'language', 'type': 'string'},
        ],
        'required_classes': profile.required_classes,
        'required_properties': profile.required_properties,
        'optional_properties': profile.optional_properties,
        'notes': 'CSV is the simulator-facing input table; RDF typing is preserved through value_type and value_lang.',
    }


def output_mapping(profile: SimulationProfile, result_csv_name: str) -> dict[str, object]:
    return {
        'profile': profile.identifier,
        'result_csv': result_csv_name,
        'columns': [
            {'name': 'run_id', 'role': 'simulation_run_identifier', 'type': 'uri_or_local_id'},
            {'name': 'scenario_id', 'role': 'scenario_identifier', 'type': 'uri_or_local_id'},
            {'name': 'input_id', 'role': 'simulation_input_identifier', 'type': 'uri_or_local_id'},
            {'name': 'output_id', 'role': 'simulation_output_identifier', 'type': 'uri_or_local_id'},
            {'name': 'entity', 'role': 'updated_entity', 'type': 'uri_or_local_id'},
            {'name': 'step', 'role': 'simulation_step', 'type': 'integer'},
            {'name': 'time', 'role': 'simulation_time', 'type': 'decimal'},
            {'name': 'property', 'role': 'produced_predicate', 'type': 'uri'},
            {'name': 'value', 'role': 'produced_value', 'type': 'mixed'},
            {'name': 'value_type', 'role': 'datatype_or_uri', 'type': 'string'},
        ],
        'produced_classes': profile.produced_classes,
        'produced_properties': profile.produced_properties,
        'allowed_value_types': ['uri', 'xsd:string', 'xsd:integer', 'xsd:decimal', 'xsd:double', 'xsd:boolean'],
        'uri_rules': {
            'qname': 'Values like fe:Zone_A are emitted as QNames.',
            'absolute_uri': 'Values beginning with http:// or https:// are emitted as bracketed IRIs.',
            'local_id': 'Bare identifiers are minted in the fe: namespace after conservative sanitization.',
        },
        'example_row': {
            'run_id': 'SimulationRun_001',
            'scenario_id': 'Scenario_001',
            'input_id': f'Input_{profile.identifier}',
            'output_id': 'Output_001',
            'entity': 'Zone_A',
            'step': '120',
            'time': '600.0',
            'property': 'fe:hasEvacuationTime',
            'value': '540.0',
            'value_type': 'xsd:double',
        },
    }


def result_example_csv(profile: SimulationProfile) -> str:
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=RESULT_CSV_COLUMNS, lineterminator='\n')
    writer.writeheader()
    writer.writerow({
        'run_id': 'SimulationRun_001',
        'scenario_id': 'Scenario_001',
        'input_id': f'Input_{profile.identifier}',
        'output_id': 'Output_001',
        'entity': 'Zone_A',
        'step': '120',
        'time': '600.0',
        'property': 'fe:hasFinalStatus',
        'value': 'evacuated',
        'value_type': 'xsd:string',
    })
    writer.writerow({
        'run_id': 'SimulationRun_001',
        'scenario_id': 'Scenario_001',
        'input_id': f'Input_{profile.identifier}',
        'output_id': 'Output_001',
        'entity': 'Zone_A',
        'step': '120',
        'time': '600.0',
        'property': 'fe:hasEvacuationTime',
        'value': '540.0',
        'value_type': 'xsd:double',
    })
    return output.getvalue()


def write_json(path: Path, content: dict[str, object]) -> None:
    path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_queries(profile_path: Path, out_dir: Path, template_dir: Path) -> GeneratedArtifacts:
    profile = load_profile(profile_path)
    name = generated_name(profile_path, profile.identifier)
    input_iri = f'fe:Input_{name}'
    queries = generate_queries(profile, template_dir, input_iri)

    out_dir.mkdir(parents=True, exist_ok=True)
    init_path = out_dir / f'{name}_init_construct.sparql'
    select_path = out_dir / f'{name}_init_select.sparql'
    result_path = out_dir / f'{name}_result_insert.sparql'
    input_mapping_path = out_dir / f'{name}_input_mapping.json'
    output_mapping_path = out_dir / f'{name}_output_mapping.json'
    result_example_path = out_dir / f'{name}_results_example.csv'

    init_path.write_text(queries.init_construct, encoding='utf-8')
    select_path.write_text(queries.init_select, encoding='utf-8')
    result_path.write_text(queries.result_insert, encoding='utf-8')
    write_json(input_mapping_path, input_mapping(profile, f'{name}_input.csv'))
    write_json(output_mapping_path, output_mapping(profile, f'{name}_results.csv'))
    result_example_path.write_text(result_example_csv(profile), encoding='utf-8')

    return GeneratedArtifacts(
        init_construct=init_path,
        init_select=select_path,
        result_insert=result_path,
        input_mapping=input_mapping_path,
        output_mapping=output_mapping_path,
        result_example_csv=result_example_path,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate SPARQL queries and CSV mappings from a fe:SimulationProfile TTL file.')
    parser.add_argument('profile', type=Path, help='Path to a profile TTL file')
    parser.add_argument('--out-dir', type=Path, default=Path('Request/generated'), help='Output directory')
    parser.add_argument('--template-dir', type=Path, default=Path('Request/Templates'), help='Template directory')
    args = parser.parse_args()

    try:
        artifacts = write_queries(args.profile, args.out_dir, args.template_dir)
    except Exception as exc:
        raise SystemExit(str(exc)) from exc

    for path in artifacts.__dict__.values():
        print(f'Generated {path}')


if __name__ == '__main__':
    main()
