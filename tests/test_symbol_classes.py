import unittest
import numpy as np

from symbol_generation.symbol_classes import CistercianSymbol, TOP, BOTTOM, TOP_THIRD, BOTTOM_THIRD, LEFT, RIGHT, MIDDLE
from symbol_generation.symbol_mapping import create_symbols


class TestCistercianSymbol(unittest.TestCase):
    def test_init_non_zero(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=False)
        expected_symbol_array = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol_array)

    def test_init_zero(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        expected_symbol_array = np.zeros(shape=(4, 5))
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol_array)

    def test_add_vertical_line_private(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        symbol._add_vertical_line(1, 3, 3)
        expected_symbol_array = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol_array)

    def test_add_horizontal_line_private(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        symbol._add_horizontal_line(1, 3, 2)
        expected_symbol_array = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol_array)

    def test_add_diagonal_line_private_up(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        symbol._add_diagonal_line(start_h=0, end_h=3, start_v=2, end_v=0)
        expected_symbol_array = np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol_array)

    def test_add_diagonal_line_private_down(self):
        symbol = CistercianSymbol(height=4, width=5, is_zero=True)
        symbol._add_diagonal_line(start_h=1, end_h=5, start_v=0, end_v=3)
        expected_symbol_array = np.array([
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
        ])
        np.testing.assert_array_equal(symbol.get_symbol(), expected_symbol_array)

    def test_get_height(self):
        symbol = CistercianSymbol(height=14, width=5, is_zero=True)
        self.assertEqual(symbol._get_height(TOP), 0)
        self.assertEqual(symbol._get_height(BOTTOM), 14)
        self.assertEqual(symbol._get_height(TOP_THIRD), 4)
        self.assertEqual(symbol._get_height(BOTTOM_THIRD), 8)

        with self.assertRaisesRegex(Exception, 'Unexpected height string'):
            symbol._get_height('no such')

    def test_get_width(self):
        symbol = CistercianSymbol(height=14, width=5, is_zero=True)
        self.assertEqual(symbol._get_width(LEFT), 0)
        self.assertEqual(symbol._get_width(RIGHT), 5)
        self.assertEqual(symbol._get_width(MIDDLE), 2)

        with self.assertRaisesRegex(Exception, 'Unexpected width string'):
            symbol._get_width('no such')

    def test_get_value(self):
        symbol_mapping = create_symbols(symbol_height=7, symbol_width=5)
        for val in [5, 70, 300, 6000, 0]:
            self.assertEqual(symbol_mapping[val].get_value(symbol_mapping), val)
