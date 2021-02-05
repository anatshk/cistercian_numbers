"""
script to create Cistercian symbols from Arabic numerals and back
"""
import numpy as np

from symbol_generation.symbol_classes import Symbol, CistercianSymbol
from symbol_generation.symbol_mapping import create_symbols

SYMBOL_HEIGHT = 7
SYMBOL_WIDTH = 5

SYMBOL_MAPPING = create_symbols(symbol_height=SYMBOL_HEIGHT, symbol_width=SYMBOL_WIDTH)


class CistercianNumber(Symbol):
    def __init__(self, height: int, width: int):
        super().__init__(height, width)
        self.symbol = CistercianSymbol(height=height, width=width, is_zero=True)
        self.order_used = [False, False, False, False]
        self.value = 0

    def __eq__(self, other):
        return \
            self.height == other.height and \
            self.width == other.width and \
            self.order_used == other.order_used and \
            self.value == other.value and \
            self.symbol == other.symbol

    def __str__(self):
        return f"CistercianNumber({self.value})"

    def show(self):
        self.symbol.show()

    def get_symbol(self):
        return self.symbol.get_symbol()

    def set_symbol(self, new_symbol: np.ndarray):
        self.symbol.set_symbol(new_symbol)

    def add_symbol(self, symbol: CistercianSymbol):
        """ Assumption - the symbol here is a valid singular symbol from mapping and not a combined symbol"""
        symbol_value = symbol.get_value(SYMBOL_MAPPING)
        if symbol_value:  # skip zeroes
            order = int(np.log10(symbol_value))

            if self.order_used[order]:
                raise Exception(f'Cannot add this symbol, already using order {order}, current value is {self.value}, '
                                f'attempting to add {symbol_value}')

            # no exception - we can add the symbol
            self.symbol.set_symbol(np.maximum(self.symbol.get_symbol(), symbol.get_symbol()))
            self.order_used[order] = True
            self.value += symbol_value


def arabic_to_cistercian(arabic_number: int) -> CistercianNumber:
    assert isinstance(arabic_number, int) or arabic_number == int(arabic_number), \
        f"Unsupported input, only int supported, got {arabic_number}"

    assert 0 <= arabic_number <= 9999, f"Number out of range, supported range is [0, 9999], got {arabic_number}"

    cistercian_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
    order = 0
    while arabic_number > 0:
        value = arabic_number % 10 * pow(10, order)
        arabic_number = arabic_number // 10
        order += 1
        symbol_for_value = SYMBOL_MAPPING[value]
        cistercian_number.add_symbol(symbol_for_value)
        
    return cistercian_number


def cistercian_to_arabic(cistercian: CistercianNumber, symbol_mapping: dict) -> int:
    """
    convert cistercian number to arabic number by comparing symbol, without using 'value' property
    assumption: the given cistercian number is of the same shape as the mapping
    """
    # TODO: validate assumption

    number = 0
    given_symbol = cistercian.get_symbol()
    for value, symbol in symbol_mapping.items():
        current_symbol = symbol.get_symbol()
        # get an overlap of current symbol with the given symbol
        symbol_overlap = given_symbol[current_symbol]
        # if the overlap is complete - the curent symbol is contained in the given symbol
        if symbol_overlap.sum() == current_symbol.sum():
            number += value

    return number
