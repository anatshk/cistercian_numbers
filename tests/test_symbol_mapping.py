import unittest
import numpy as np

from symbol_generation.symbol_mapping import create_symbols


class TestSymbolMapping(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mapping = create_symbols(symbol_height=7, symbol_width=5)

    def test_0(self):
        symbol = self.mapping[0]
        expected_symbol = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.symbol, expected_symbol)

    def test_1(self):
        symbol = self.mapping[1]
        expected_symbol = np.array([
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.symbol, expected_symbol)

