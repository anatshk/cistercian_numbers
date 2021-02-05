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

    def show(self, **kwargs):
        self.symbol.show(**kwargs)

    def get_symbol(self):
        return self.symbol.get_symbol()

    def set_symbol(self, new_symbol: np.ndarray):
        self.symbol.set_symbol(new_symbol)

    def add_symbol(self, symbol: CistercianSymbol, symbol_mapping: dict = SYMBOL_MAPPING):
        """ Assumption - the symbol here is a valid singular symbol from mapping and not a combined symbol"""
        symbol_value = symbol.get_value(symbol_mapping)
        if symbol_value:  # skip zeroes
            order = int(np.log10(symbol_value))

            if self.order_used[order]:
                raise Exception(f'Cannot add this symbol, already using order {order}, current value is {self.value}, '
                                f'attempting to add {symbol_value}')

            # no exception - we can add the symbol
            self.symbol.set_symbol(np.maximum(self.symbol.get_symbol(), symbol.get_symbol()))
            self.order_used[order] = True
            self.value += symbol_value


def arabic_to_cistercian(arabic_number: int, symbol_height: int = SYMBOL_HEIGHT, symbol_width: int = SYMBOL_WIDTH,
                         symbol_mapping: dict = None) -> CistercianNumber:
    assert isinstance(arabic_number, int) or arabic_number == int(arabic_number), \
        f"Unsupported input, only int supported, got {arabic_number}"

    assert 0 <= arabic_number <= 9999, f"Number out of range, supported range is [0, 9999], got {arabic_number}"

    if symbol_mapping is None:
        symbol_mapping = SYMBOL_MAPPING

    cistercian_number = CistercianNumber(height=symbol_height, width=symbol_width)
    order = 0
    while arabic_number > 0:
        value = arabic_number % 10 * pow(10, order)
        arabic_number = arabic_number // 10
        order += 1
        symbol_for_value = symbol_mapping[value]
        cistercian_number.add_symbol(symbol_for_value, symbol_mapping)
        
    return cistercian_number


def _validate_cistercian_number_size(cistercian: CistercianNumber, symbol_mapping: dict):
    symbol_shape = cistercian.get_symbol().shape
    mapping_shape = symbol_mapping[0].get_symbol().shape
    assert symbol_shape == mapping_shape, \
        f"Size mismatch between symbol and mapping, symbol shape: {symbol_shape}, mapping shape: {mapping_shape}"


def _find_symbols_contained_in_given_symbol(given_symbol: np.ndarray, symbol_mapping: dict) -> list:
    symbol_candidates = [None, None, None, None]
    for value, symbol in symbol_mapping.items():
        current_symbol = symbol.get_symbol()
        # get an overlap of current symbol with the given symbol
        symbol_overlap = given_symbol * current_symbol
        # if the overlap is complete - the current symbol is contained in the given symbol
        curr_symbol_size = current_symbol.sum()
        # some symbols are contained within others (1000 and 9000), in these cases we want to make sure that
        # we take the candidate with the larger overlap of the original symbol
        if symbol_overlap.sum() == curr_symbol_size and curr_symbol_size > 0:
            candidate_order = int(np.log10(value))
            if symbol_candidates[candidate_order] is None or symbol_candidates[candidate_order][1] < curr_symbol_size:
                # first candidate of this order --> save value and size of current candidate
                # OR, candidate of this order already exists - override if current candidate is larger
                symbol_candidates[candidate_order] = (value, curr_symbol_size)

    return [candidate[0] for candidate in symbol_candidates if candidate is not None]


def cistercian_to_arabic(cistercian: CistercianNumber, symbol_mapping: dict) -> int:
    """
    convert cistercian number to arabic number by comparing symbol, without using 'value' property
    assumption: the given cistercian number is of the same shape as the mapping
    """
    _validate_cistercian_number_size(cistercian, symbol_mapping)

    given_symbol = cistercian.get_symbol()
    symbol_candidate_values = _find_symbols_contained_in_given_symbol(given_symbol, symbol_mapping)

    # sum all candidate values
    number = np.sum(symbol_candidate_values)

    return number
