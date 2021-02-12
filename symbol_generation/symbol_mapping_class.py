"""
A class replacing cistercian_numbers/symbol_generation/symbol_mapping.py file

Lazy class - only creates (and saves) missing symbols when asked
"""
import numpy as np

from symbol_generation.symbol_classes import CistercianSymbol, TOP, TOP_THIRD, RIGHT, UP

# assuming we want to keep all previous usages of "symbol_mapping" as dicts,
#   create relevant dict-like methods - https://stackoverflow.com/questions/4014621/a-python-class-that-acts-like-dict
from symbol_generation.symbol_mapping import show_mapping


class CistercianMapping:
    def __init__(self, symbol_height: int, symbol_width: int):
        self.height = symbol_height
        self.width = symbol_width
        self.mapping = {
            0: CistercianSymbol(height=self.height, width=self.width, is_zero=True),
        }

    def _add_basic_mappings(self, key: int):
        """
        This method creates the basic mappings of digits 1-9 in self.mapping
        It uses 3 "if" steps - the second and third steps add lines to the symbols created in previous steps,
        as, for example, the symbol for 5 contains the symbol for 4, plus an additional line.
        Same for 7 and 8, which contain 6 plus an additional line, and 9, which contains 8 plus an additional line.
        :param key: int
        :return: None
        """
        assert 1 <= key <= 9, 'this method is only used for digits 1-9'

        symbol = CistercianSymbol(height=self.height, width=self.width)
        # create the basic symbols
        if key == 1:
            symbol.add_horizontal_line(location_str=TOP, direction_str=RIGHT)
        elif key == 2:
            symbol.add_horizontal_line(location_str=TOP_THIRD, direction_str=RIGHT)
        elif key == 3:
            symbol.add_diagonal_line(start_height_on_middle=TOP, end_height=TOP_THIRD, direction_str=RIGHT)
        elif key in [4, 5]:
            symbol.add_diagonal_line(start_height_on_middle=TOP_THIRD, end_height=TOP, direction_str=RIGHT)
        elif key in [6, 7, 8, 9]:
            symbol.add_vertical_line(width_str=RIGHT, start_str=TOP, end_str=TOP_THIRD)

        # create additional lines for symbols that contain previous symbols (5, 7, 8, 9)
        if key == 5:
            symbol.add_horizontal_line(location_str=TOP, direction_str=RIGHT)
        elif key == 7:
            symbol.add_horizontal_line(location_str=TOP, direction_str=RIGHT)
        elif key in [8, 9]:
            symbol.add_horizontal_line(location_str=TOP_THIRD, direction_str=RIGHT)

        # another additional step, for 9 only
        if key == 9:
            symbol.add_horizontal_line(location_str=TOP, direction_str=RIGHT)

        self.mapping[key] = symbol

    @staticmethod
    def _multiply_symbol_by_10(symbol: CistercianSymbol):
        # 10-90 are flips left to right of 1-9
        return symbol.fliplr()

    @staticmethod
    def _multiply_symbol_by_100(symbol: CistercianSymbol):
        # 100-900 are flips up-down of 1-9
        return symbol.flipud()

    @staticmethod
    def _multiply_symbol_by_1000(symbol: CistercianSymbol):
        # 1000-9000 are flips up-down of 10-90
        # so, 1-9 --> fliplr --> flipud --> 1000-9000
        lr = symbol.fliplr()
        return lr.flipud()

    def _flip_symbol_to_order(self, symbol: CistercianSymbol, order: int) -> CistercianSymbol:
        if order == 1:
            key_symbol = self._multiply_symbol_by_10(symbol)
        elif order == 2:
            key_symbol = self._multiply_symbol_by_100(symbol)
        elif order == 3:
            key_symbol = self._multiply_symbol_by_1000(symbol)
        else:
            raise Exception(f'Unsupported order {order}, expecting 1 / 2 / 3')

        return key_symbol

    def _add_advanced_mappings(self, key: int):
        """
        This method creates advanced mappings for symbols 10-90, 100-900, 1000-9000, which can all be generated
        by flipping the symbols for 1-9.
        """
        order = int(np.log10(key))
        digit = key // pow(10, order)
        digit_symbol = self.__getitem__(digit)
        key_symbol_instance = self._flip_symbol_to_order(digit_symbol, order)
        self.mapping[key] = key_symbol_instance

    def __setitem__(self, key: int, item: CistercianSymbol):
        self.mapping[key] = item

    def create_full(self):
        for digit in range(1, 10):
            self._add_basic_mappings(digit)
            self._add_advanced_mappings(digit * 10)
            self._add_advanced_mappings(digit * 100)
            self._add_advanced_mappings(digit * 1000)

    def _create_missing_key(self, key: int):
        if key < 10:
            self._add_basic_mappings(key=key)
        else:
            self._add_advanced_mappings(key)

    def __getitem__(self, key):
        assert isinstance(key, int), f'Unsupported number {key}, expecting an integer'
        assert key in range(0, 11) or key in range(10, 100, 10) or key in range(100, 1000, 100) \
               or key in range(1000, 10000, 1000), f'Unsupported number {key}, number should be 0-9 or a ' \
                                                   f'multiplication of 10/100/1000 of 1-9'
        item = self.mapping.get(key)
        if item is None:
            self._create_missing_key(key)
        return self.mapping[key]

    def __repr__(self):
        return self.mapping.__repr__()

    def __len__(self):
        return self.mapping.__len__()

    def __delitem__(self, key):
        del self.mapping[key]

    def has_key(self, k):
        return k in self.mapping

    def keys(self):
        return self.mapping.keys()

    def values(self):
        return self.mapping.values()

    def items(self):
        return self.mapping.items()

    def __contains__(self, item):
        return self.mapping.__contains__(item)

    def __iter__(self):
        return iter(self.mapping)

    def show_mapping(self):
        show_mapping(self)
