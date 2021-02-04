import unittest
import numpy as np

from symbol_generation.symbol_classes import CistercianSymbol


class TestCistercianSymbol(unittest.TestCase):
    def test_init_non_zero(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=False)
        expected_symbol_array = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.symbol, expected_symbol_array)

    def test_init_zero(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        expected_symbol_array = np.zeros(shape=(4, 5))
        np.testing.assert_array_equal(symbol.symbol, expected_symbol_array)

    def test_add_vertical_line_private(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        symbol._add_vertical_line(1, 3, 3)
        expected_symbol_array = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.symbol, expected_symbol_array)

    def test_add_horizontal_line_private(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        symbol._add_horizontal_line(1, 3, 2)
        expected_symbol_array = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.symbol, expected_symbol_array)



