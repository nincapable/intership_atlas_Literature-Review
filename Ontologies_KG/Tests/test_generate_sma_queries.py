#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'Scripts' / 'generate_sma_queries.py'
spec = importlib.util.spec_from_file_location('generate_sma_queries', MODULE_PATH)
generator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules['generate_sma_queries'] = generator
spec.loader.exec_module(generator)


class GenerateSMAQueriesTest(unittest.TestCase):
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

    def test_write_queries_keeps_existing_file_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = generator.write_queries(
                ROOT / 'Profiles' / 'evacuation_sma_profile.ttl',
                Path(tmp),
                ROOT / 'Request' / 'Templates',
            )
            names = [path.name for path in paths]
            self.assertEqual(
                names,
                [
                    'evacuation_sma_init_construct.sparql',
                    'evacuation_sma_init_select.sparql',
                    'evacuation_sma_result_insert.sparql',
                ],
            )
            construct = paths[0].read_text(encoding='utf-8')
            self.assertIn('VALUES ?class', construct)
            self.assertIn('fe:Zone', construct)
            self.assertIn('fe:Input_evacuation_sma', construct)

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


if __name__ == '__main__':
    unittest.main()
