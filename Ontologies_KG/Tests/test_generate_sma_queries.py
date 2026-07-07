#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / 'Scripts'
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
MODULE_PATH = SCRIPT_DIR / 'generate_sma_queries.py'
spec = importlib.util.spec_from_file_location('generate_sma_queries', MODULE_PATH)
generator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules['generate_sma_queries'] = generator
spec.loader.exec_module(generator)

export_spec = importlib.util.spec_from_file_location('export_sma_input_csv', SCRIPT_DIR / 'export_sma_input_csv.py')
exporter = importlib.util.module_from_spec(export_spec)
assert export_spec and export_spec.loader
sys.modules['export_sma_input_csv'] = exporter
export_spec.loader.exec_module(exporter)

import_spec = importlib.util.spec_from_file_location('import_sma_results_csv', SCRIPT_DIR / 'import_sma_results_csv.py')
importer = importlib.util.module_from_spec(import_spec)
assert import_spec and import_spec.loader
sys.modules['import_sma_results_csv'] = importer
import_spec.loader.exec_module(importer)


class GenerateSMAQueriesTest(unittest.TestCase):
    def test_all_shacl_constraints_parse_with_rdflib(self) -> None:
        constraint_files = sorted((ROOT / 'Constraints').glob('*.ttl'))
        self.assertGreater(len(constraint_files), 0)

        for path in constraint_files:
            with self.subTest(path=path.name):
                graph = Graph()
                graph.parse(path, format='turtle')
                self.assertGreater(len(graph), 0)

    def test_load_existing_profile_with_rdflib(self) -> None:
        profile = generator.load_profile(ROOT / 'Profiles' / 'evacuation_sma_profile.ttl')

        self.assertEqual(profile.identifier, 'evacuation_sma')
        self.assertEqual(profile.root_class, 'fe:Zone')
        self.assertIn('fe:Zone', profile.required_classes)
        self.assertIn('fe:Axis', profile.required_classes)
        self.assertIn('fe:hasPopulation', profile.required_properties)
        self.assertIn('fe:hasProtectionPriority', profile.optional_properties)
        self.assertIn('fe:producesOutput', profile.produced_properties)
        self.assertIn('fe', profile.prefixes)

    def test_write_queries_keeps_existing_file_names_and_adds_mappings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifacts = generator.write_queries(
                ROOT / 'Profiles' / 'evacuation_sma_profile.ttl',
                Path(tmp),
                ROOT / 'Request' / 'Templates',
            )
            names = [path.name for path in artifacts.__dict__.values()]
            self.assertEqual(
                names[:3],
                [
                    'evacuation_sma_init_construct.sparql',
                    'evacuation_sma_init_select.sparql',
                    'evacuation_sma_result_insert.sparql',
                ],
            )
            self.assertIn('evacuation_sma_input_mapping.json', names)
            self.assertIn('evacuation_sma_output_mapping.json', names)
            self.assertIn('evacuation_sma_results_example.csv', names)

            construct = artifacts.init_construct.read_text(encoding='utf-8')
            self.assertIn('VALUES ?class', construct)
            self.assertIn('fe:Zone', construct)
            self.assertIn('fe:Input_evacuation_sma', construct)

            mapping = json.loads(artifacts.input_mapping.read_text(encoding='utf-8'))
            self.assertEqual(mapping['profile'], 'evacuation_sma')
            self.assertIn('fe:Axis', mapping['required_classes'])
            self.assertIn('fe:hasPopulation', mapping['required_properties'])

    def test_deep_construct_profile_extension(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / 'deep_profile.ttl'
            profile_path.write_text(
                '@prefix fe: <http://example.org/fire_and_evacuation#> .\n\n'
                'fe:DeepProfile a fe:SimulationProfile ;\n'
                '    fe:profileIdentifier "deep" ;\n'
                '    fe:requiresClass fe:Zone ;\n'
                '    fe:requiresProperty fe:hasPopulation ;\n'
                '    fe:expandProperty fe:hasPopulation, fe:isConnectedTo ;\n'
                '    fe:maxDepth 2 .\n',
                encoding='utf-8',
            )
            profile = generator.load_profile(profile_path)
            query = generator.generate_deep_construct(profile, 'unused', 'fe:Input_deep')

            self.assertEqual(profile.max_depth, 2)
            self.assertIn('VALUES ?expandProperty', query)
            self.assertIn('?node2', query)
            self.assertIn('fe:isConnectedTo', query)

    def test_export_input_csv_preserves_rdf_value_types(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            data_path = Path(tmp) / 'kg.ttl'
            out_path = Path(tmp) / 'input.csv'
            data_path.write_text(
                '@prefix fe: <http://example.org/fire_and_evacuation#> .\n'
                '@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n'
                'fe:Axis_12 a fe:Axis ;\n'
                '    fe:maxFlowCapacity 150 ;\n'
                '    fe:hasWidth "3.5"^^xsd:double ;\n'
                '    fe:isConnectedTo fe:Axis_13 .\n'
                'fe:Zone_A a fe:Zone ;\n'
                '    fe:hasPopulation fe:Population_A .\n'
                'fe:Population_A a fe:Population .\n',
                encoding='utf-8',
            )

            exporter.write_input_csv(ROOT / 'Profiles' / 'evacuation_sma_profile.ttl', data_path, out_path)
            with out_path.open(encoding='utf-8') as handle:
                rows = list(csv.DictReader(handle))

            self.assertIn('entity', rows[0])
            by_property = {row['property']: row for row in rows}
            self.assertEqual(by_property['fe:maxFlowCapacity']['value'], '150')
            self.assertEqual(by_property['fe:maxFlowCapacity']['value_type'], 'xsd:integer')
            self.assertEqual(by_property['fe:hasWidth']['value_type'], 'xsd:double')
            self.assertEqual(by_property['fe:isConnectedTo']['value'], 'fe:Axis_13')
            self.assertEqual(by_property['fe:isConnectedTo']['value_type'], 'uri')

    def test_import_results_csv_generates_typed_insert(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / 'results.csv'
            csv_path.write_text(
                'run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type\n'
                'SimulationRun_001,Scenario_001,Input_evacuation_sma,Output_001,Zone_A,120,600.0,fe:hasEvacuationTime,540.0,xsd:double\n',
                encoding='utf-8',
            )
            query = importer.generate_insert_from_csv(
                ROOT / 'Profiles' / 'evacuation_sma_profile.ttl',
                csv_path,
                'http://example.org/results',
            )

            self.assertIn('INSERT DATA', query)
            self.assertIn('GRAPH <http://example.org/results>', query)
            self.assertIn('fe:SimulationRun_001 a fe:SimulationRun', query)
            self.assertIn('fe:hasEvacuationTime "540.0"^^xsd:double', query)
            self.assertIn('fe:hasSimulationStep "120"^^xsd:integer', query)


if __name__ == '__main__':
    unittest.main()
