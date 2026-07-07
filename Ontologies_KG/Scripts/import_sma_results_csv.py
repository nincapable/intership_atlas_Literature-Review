#!/usr/bin/env python3
"""Convert simulator result CSV files into SPARQL INSERT DATA updates."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from generate_sma_queries import RESULT_CSV_COLUMNS, SimulationProfile, format_prefixes, load_profile  # noqa: E402

DEFAULT_RESULT_GRAPH = 'http://example.org/fire_and_evacuation/simulation/results'


def sanitize_local_id(value: str) -> str:
    cleaned = re.sub(r'[^A-Za-z0-9_\-]+', '_', value.strip())
    cleaned = cleaned.strip('_') or 'Unnamed'
    if cleaned[0].isdigit():
        cleaned = f'_{cleaned}'
    return cleaned


def uri_term(value: str, profile: SimulationProfile) -> str:
    value = value.strip()
    if not value:
        raise ValueError('URI value cannot be empty')
    if value.startswith('<') and value.endswith('>'):
        return value
    if value.startswith('http://') or value.startswith('https://'):
        return f'<{value}>'
    if ':' in value:
        prefix = value.split(':', 1)[0]
        if prefix in profile.prefixes:
            return value
    return f'fe:{sanitize_local_id(value)}'


def datatype_term(value_type: str, profile: SimulationProfile) -> str:
    value_type = value_type.strip()
    if value_type.startswith('<') and value_type.endswith('>'):
        return value_type
    if value_type.startswith('http://') or value_type.startswith('https://'):
        return f'<{value_type}>'
    if ':' in value_type:
        prefix = value_type.split(':', 1)[0]
        if prefix in profile.prefixes:
            return value_type
    raise ValueError(f'Unsupported datatype {value_type!r}; use a QName or absolute URI')


def escape_literal(value: str) -> str:
    return value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r')


def object_term(value: str, value_type: str, profile: SimulationProfile) -> str:
    if value_type == 'uri':
        return uri_term(value, profile)
    if value_type == 'bnode':
        raise ValueError('BNode result values are not supported for SPARQL INSERT generation')
    datatype = datatype_term(value_type or 'xsd:string', profile)
    return f'"{escape_literal(value)}"^^{datatype}'


def stable_final_state_id(output_id: str, entity: str, step: str) -> str:
    return f'FinalState_{sanitize_local_id(output_id)}_{sanitize_local_id(entity)}_{sanitize_local_id(step)}'


def read_result_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open('r', encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        missing = [column for column in RESULT_CSV_COLUMNS if column not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f'Missing result CSV columns: {", ".join(missing)}')
        return [{key: (row.get(key) or '').strip() for key in RESULT_CSV_COLUMNS} for row in reader]


def generate_insert_from_rows(profile: SimulationProfile, rows: list[dict[str, str]], result_graph: str = DEFAULT_RESULT_GRAPH) -> str:
    run_triples: set[str] = set()
    output_triples: set[str] = set()
    state_triples: set[str] = set()

    for row in rows:
        run = uri_term(row['run_id'], profile)
        scenario = uri_term(row['scenario_id'], profile)
        input_id = uri_term(row['input_id'], profile)
        output = uri_term(row['output_id'], profile)
        entity = uri_term(row['entity'], profile)
        state = uri_term(stable_final_state_id(row['output_id'], row['entity'], row['step']), profile)
        prop = uri_term(row['property'], profile)
        obj = object_term(row['value'], row['value_type'], profile)
        step_literal = object_term(row['step'], 'xsd:integer', profile)
        time_literal = object_term(row['time'], 'xsd:decimal', profile)

        run_triples.add(
            f'    {run} a fe:SimulationRun ;\n'
            f'        fe:usesScenario {scenario} ;\n'
            f'        fe:consumesInput {input_id} ;\n'
            f'        fe:producesOutput {output} .'
        )
        output_triples.add(
            f'    {output} a fe:SimulationOutput ;\n'
            f'        fe:hasFinalState {state} ;\n'
            f'        fe:producedByRun {run} .'
        )
        state_triples.add(
            f'    {state} a fe:FinalState ;\n'
            f'        fe:stateOfEntity {entity} ;\n'
            f'        fe:hasSimulationStep {step_literal} ;\n'
            f'        fe:hasSimulationTime {time_literal} ;\n'
            f'        fe:producedByRun {run} ;\n'
            f'        {prop} {obj} .'
        )

    body = '\n\n'.join(sorted(run_triples) + sorted(output_triples) + sorted(state_triples))
    return f"""# Generated from SMA result CSV.
{format_prefixes(profile.prefixes)}

INSERT DATA {{
  GRAPH <{result_graph}> {{
{body}
  }}
}}
"""


def generate_insert_from_csv(profile_path: Path, csv_path: Path, result_graph: str = DEFAULT_RESULT_GRAPH) -> str:
    profile = load_profile(profile_path)
    return generate_insert_from_rows(profile, read_result_rows(csv_path), result_graph)


def write_results_insert(profile_path: Path, csv_path: Path, out_path: Path, result_graph: str = DEFAULT_RESULT_GRAPH) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(generate_insert_from_csv(profile_path, csv_path, result_graph), encoding='utf-8')
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description='Convert SMA result CSV to SPARQL INSERT DATA.')
    parser.add_argument('--profile', type=Path, required=True, help='Path to a fe:SimulationProfile TTL file')
    parser.add_argument('--csv', type=Path, required=True, help='Path to simulator result CSV')
    parser.add_argument('--out', type=Path, required=True, help='Output SPARQL INSERT file')
    parser.add_argument('--result-graph', default=DEFAULT_RESULT_GRAPH, help='Named graph receiving simulation results')
    args = parser.parse_args()

    try:
        path = write_results_insert(args.profile, args.csv, args.out, args.result_graph)
    except Exception as exc:
        raise SystemExit(str(exc)) from exc
    print(f'Generated {path}')


if __name__ == '__main__':
    main()
