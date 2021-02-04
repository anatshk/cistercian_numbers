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
        order = int(np.log10(symbol_value))

        if self.order_used[order]:
            raise Exception(f'Cannot add this symbol, already using order {order}, current value is {self.value}, '
                            f'attempting to add {symbol_value}')

        # no exception - we can add the symbol
        self.symbol.set_symbol(np.maximum(self.symbol.get_symbol(), symbol.get_symbol()))
        self.order_used[order] = True
        self.value += symbol_value


def arabic_to_cistercian(arabic_number: int) -> CistercianNumber:
    cistercian_number = CistercianNumber(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH) 
    order = 0
    while arabic_number > 0:
        value = arabic_number % 10 * pow(10, order)
        arabic_number = arabic_number // 10
        order += 1
        symbol_for_value = SYMBOL_MAPPING[value]
        cistercian_number.add_symbol(symbol_for_value)
        
    return cistercian_number
