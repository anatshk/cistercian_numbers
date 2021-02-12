import unittest

from symbol_generation.symbol_mapping import create_symbols
from symbol_generation.symbol_mapping_class import CistercianMapping


class TestCistercianMapping(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mapping_for_comparison = create_symbols(symbol_height=7, symbol_width=5)

    def test_init(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)
        self.assertEqual(cm.height, 7)
        self.assertEqual(cm.width, 5)
        self.assertEqual(list(cm.mapping.keys()), [0])

    def test_get_existing(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)
        zero = cm[0]
        self.assertEqual(zero, self.mapping_for_comparison[0])

    def test_get_non_existing(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)
        one = cm[1]
        self.assertEqual(one, self.mapping_for_comparison[1])
        self.assertEqual(list(cm.keys()), [0, 1])

    def test_get_non_existing_create_intermediate(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)
        ninety = cm[90]
        self.assertEqual(ninety, self.mapping_for_comparison[90])
        self.assertEqual(list(cm.keys()), [0, 9, 90])

    def test_get_unsupported_key(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)
        with self.assertRaisesRegex(AssertionError, 'Unsupported number'):
            value = cm[123]

        with self.assertRaisesRegex(AssertionError, 'Unsupported number'):
            value = cm['boom']

    def test_create_full(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)
        cm.create_full()
        self.assertEqual(cm.mapping, self.mapping_for_comparison)



    def test_multiply_symbol_by_10(self):
        cm = CistercianMapping(symbol_height=7, symbol_width=5)


