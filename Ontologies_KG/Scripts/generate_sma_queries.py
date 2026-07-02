#!/usr/bin/env python3
"""Generate SPARQL initialization/result templates from a simple fe:SimulationProfile TTL file.

This script intentionally avoids rdflib so it can run in a lightweight environment.
It supports the profile style used in Profiles/*.ttl: one fe:SimulationProfile with
comma-separated QName values for fe:requiresClass, fe:requiresProperty, etc.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_PREFIXES = """PREFIX fe:   <http://example.org/fire_and_evacuation#>
PREFIX crm:  <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>"""


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if '#' in line:
            line = line.split('#', 1)[0]
        lines.append(line)
    return '\n'.join(lines)


def values_for(clean_text: str, predicate: str) -> list[str]:
    pattern = rf"{re.escape(predicate)}\s+([^.;]+)[.;]"
    found: list[str] = []
    for match in re.finditer(pattern, clean_text, flags=re.S):
        raw = match.group(1).replace('\n', ' ')
        for value in raw.split(','):
            value = value.strip()
            if value and not value.startswith('"'):
                found.append(value)
    return found


def literal_for(clean_text: str, predicate: str, default: str) -> str:
    match = re.search(rf"{re.escape(predicate)}\s+\"([^\"]+)\"", clean_text)
    return match.group(1) if match else default


def format_values(values: list[str], indent: str = '    ') -> str:
    return '\n'.join(f'{indent}{value}' for value in values)


def generated_name(profile_path: Path, profile_id: str) -> str:
    if profile_id:
        return re.sub(r'[^A-Za-z0-9_\-]+', '_', profile_id)
    return profile_path.stem


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate SPARQL queries from a fe:SimulationProfile TTL file.')
    parser.add_argument('profile', type=Path, help='Path to a profile TTL file')
    parser.add_argument('--out-dir', type=Path, default=Path('Request/generated'), help='Output directory')
    parser.add_argument('--template-dir', type=Path, default=Path('Request/Templates'), help='Template directory')
    args = parser.parse_args()

    raw = args.profile.read_text(encoding='utf-8')
    clean = strip_comments(raw)

    profile_id = literal_for(clean, 'fe:profileIdentifier', args.profile.stem)
    name = generated_name(args.profile, profile_id)

    classes = values_for(clean, 'fe:requiresClass')
    required_props = values_for(clean, 'fe:requiresProperty')
    optional_props = values_for(clean, 'fe:optionalProperty')
    produced_props = values_for(clean, 'fe:producesProperty')

    if not classes:
        raise SystemExit('No fe:requiresClass values found in profile')

    properties = []
    for prop in required_props + optional_props:
        if prop not in properties:
            properties.append(prop)

    init_template = (args.template_dir / 'sma_init_construct_template.sparql').read_text(encoding='utf-8')
    select_template = (args.template_dir / 'sma_init_select_template.sparql').read_text(encoding='utf-8')
    result_template = (args.template_dir / 'sma_result_insert_template.sparql').read_text(encoding='utf-8')

    input_iri = f'fe:Input_{name}'

    init_query = init_template.format(
        PREFIXES=DEFAULT_PREFIXES,
        CLASS_VALUES=format_values(classes),
        PROPERTY_VALUES=format_values(properties),
        INPUT_IRI=input_iri,
    )

    select_query = select_template.format(
        PREFIXES=DEFAULT_PREFIXES,
        CLASS_VALUES=format_values(classes),
        PROPERTY_VALUES=format_values(properties),
    )

    produced_hints = '\n'.join(f'    # - {prop}' for prop in produced_props) or '    # - no produced properties declared'
    result_query = result_template.format(
        PREFIXES=DEFAULT_PREFIXES,
        PRODUCED_PROPERTY_HINTS=produced_hints,
    )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    init_path = args.out_dir / f'{name}_init_construct.sparql'
    select_path = args.out_dir / f'{name}_init_select.sparql'
    result_path = args.out_dir / f'{name}_result_insert.sparql'
    init_path.write_text(init_query, encoding='utf-8')
    select_path.write_text(select_query, encoding='utf-8')
    result_path.write_text(result_query, encoding='utf-8')

    print(f'Generated {init_path}')
    print(f'Generated {select_path}')
    print(f'Generated {result_path}')


if __name__ == '__main__':
    main()
