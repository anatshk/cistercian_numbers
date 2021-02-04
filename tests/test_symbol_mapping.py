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
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

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
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_2(self):
        symbol = self.mapping[2]
        expected_symbol = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_3(self):
        symbol = self.mapping[3]
        expected_symbol = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_4(self):
        symbol = self.mapping[4]
        expected_symbol = np.array([
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_5(self):
        symbol = self.mapping[5]
        expected_symbol = np.array([
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_6(self):
        symbol = self.mapping[6]
        expected_symbol = np.array([
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_7(self):
        symbol = self.mapping[7]
        expected_symbol = np.array([
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_8(self):
        symbol = self.mapping[8]
        expected_symbol = np.array([
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)

    def test_9(self):
        symbol = self.mapping[9]
        expected_symbol = np.array([
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol)
