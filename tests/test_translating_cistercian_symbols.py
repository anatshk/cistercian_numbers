import unittest
import numpy as np

from symbol_generation.symbol_mapping import create_symbols
from translating_cistercian_symbols import CistercianNumber, SYMBOL_WIDTH, SYMBOL_HEIGHT, arabic_to_cistercian

SYMBOL_MAPPING = create_symbols(symbol_height=7, symbol_width=5)


class TestCistercianNumber(unittest.TestCase):
    def test_sanity(self):
        cistercian_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        self.assertEqual(cistercian_number.height, SYMBOL_HEIGHT)
        self.assertEqual(cistercian_number.width, SYMBOL_WIDTH)
        self.assertEqual(cistercian_number.value, 0)
        self.assertEqual(cistercian_number.order_used, [False, False, False, False])

    def test_add_symbol_sanity(self):
        one = SYMBOL_MAPPING[1]
        twenty = SYMBOL_MAPPING[20]
        final_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        final_number.add_symbol(twenty)
        self.assertEqual(final_number.value, 20)
        self.assertEqual(final_number.order_used, [False, True, False, False])

        final_number.add_symbol(one)
        expected_symbol = np.array([
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        self.assertEqual(final_number.value, 21)
        self.assertEqual(final_number.order_used, [True, True, False, False])
        np.testing.assert_array_equal(final_number.get_symbol(), expected_symbol)

    def test_add_symbol_exception(self):
        one = SYMBOL_MAPPING[1]
        two = SYMBOL_MAPPING[2]
        final_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        final_number.add_symbol(one)

        expected_exception = 'Cannot add this symbol, already using order 0, current value is 1, attempting to add 2'
        with self.assertRaisesRegex(Exception, expected_exception):
            final_number.add_symbol(two)


class TestArabicToCistercian(unittest.TestCase):
    def test_4_digits(self):
        number = 1993
        cistercian = arabic_to_cistercian(number)
        expected_symbol = np.array([
            [1, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
        ])
        self.assertEqual(cistercian.value, number)
        np.testing.assert_array_equal(cistercian.get_symbol(), expected_symbol)

    def test_3_digits(self):
        number = 2047
        cistercian = arabic_to_cistercian(number)
        expected_symbol = np.array([
            [1, 0, 1, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ])
        self.assertEqual(cistercian.value, number)
        np.testing.assert_array_equal(cistercian.get_symbol(), expected_symbol)

    def test_2_digits(self):
        number = 6002
        cistercian = arabic_to_cistercian(number)
        expected_symbol = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
        ])
        self.assertEqual(cistercian.value, number)
        np.testing.assert_array_equal(cistercian.get_symbol(), expected_symbol)

    def test_zero(self):
        # TODO: number = 0
        self.assertTrue(False)

    def test_number_out_of_range(self):
        # TODO: number < 0 or number > 9999 - raise exception
        self.assertTrue(False)


class TestCistercianToArabic(unittest.TestCase):
    def test_2_symbol(self):
        # TODO: select single symbol and test
        self.assertTrue(False)

    def test_2_symbols(self):
        # TODO: select 2 symbols combination and test
        self.assertTrue(False)

    def test_3_symbols(self):
        # TODO: select 3 symbols combination and test
        self.assertTrue(False)

    def test_4_symbols(self):
        # TODO: select 4 symbols combination and test
        self.assertTrue(False)

    def test_unknown_symbol(self):
        # TODO: create an unsupported symbol and test - raise exception
        self.assertTrue(False)
