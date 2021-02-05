import unittest
import numpy as np

from symbol_generation.symbol_classes import CistercianSymbol
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
        number = 0
        cistercian = arabic_to_cistercian(number)
        expected_symbol = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        self.assertEqual(cistercian.value, number)
        np.testing.assert_array_equal(cistercian.get_symbol(), expected_symbol)

    def test_number_out_of_range(self):
        with self.assertRaisesRegex(Exception, "Number out of range"):
            arabic_to_cistercian(-5)

        with self.assertRaisesRegex(Exception, "Number out of range"):
            arabic_to_cistercian(10342)

    def test_number_not_an_int(self):
        with self.assertRaisesRegex(Exception, "Unsupported input, only int supported, got"):
            arabic_to_cistercian(5.3)


class TestCistercianToArabic(unittest.TestCase):
    def test_1_symbol(self):
        # single symbol - 1000
        symbol = np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
        ])
        symbol_instance = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        symbol_instance.set_symbol(symbol)
        number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        number.add_symbol(symbol_instance)

        expected_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        expected_number.add_symbol(SYMBOL_MAPPING[1000])
        self.assertEqual(expected_number, number)

    def test_2_symbols(self):
        # two symbols - 1000 + 30
        symbol = np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
        ])
        symbol_instance = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        symbol_instance.set_symbol(symbol)
        number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        number.add_symbol(symbol_instance)

        expected_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        expected_number.add_symbol(SYMBOL_MAPPING[1000])
        expected_number.add_symbol(SYMBOL_MAPPING[30])
        self.assertEqual(expected_number, number)

    def test_3_symbols(self):
        # 3 symbols - 1000 + 30 + 700
        symbol = np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
        ])
        symbol_instance = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        symbol_instance.set_symbol(symbol)
        number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        number.add_symbol(symbol_instance)

        expected_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
        expected_number.add_symbol(SYMBOL_MAPPING[1000])
        expected_number.add_symbol(SYMBOL_MAPPING[30])
        expected_number.add_symbol(SYMBOL_MAPPING[700])
        self.assertEqual(expected_number, number)

    def test_4_symbols(self):
        # TODO: select 4 symbols combination and test
        # 5 symbols - 1000 + 30 + 700 + 5
        self.assertTrue(False)

    def test_unknown_symbol(self):
        # TODO: create an unsupported symbol and test - raise exception
        self.assertTrue(False)

    def tezt_zero(self):
        # TODO: test with zero symbol (empty array)
        self.assertTrue(False)
