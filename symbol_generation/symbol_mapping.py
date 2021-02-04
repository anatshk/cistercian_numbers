"""
This file contains function that creates a mapping of the available values to their symbol instances
"""

from symbol_generation.symbol_classes import CistercianSymbol, TOP, BOTTOM, TOP_THIRD, BOTTOM_THIRD, LEFT, RIGHT, MIDDLE

# symbol_height = 17
# symbol_width = 13


def create_symbols(symbol_height: int, symbol_width: int) -> dict:
    # 1
    one = CistercianSymbol(height=symbol_height, width=symbol_width)
    one.add_horizontal_line(height_str=TOP, direction_str=RIGHT)

    # 10
    ten = CistercianSymbol(height=symbol_height, width=symbol_width)
    ten.add_horizontal_line(height_str=TOP, direction_str=LEFT)

    # 100
    hundred = CistercianSymbol(height=symbol_height, width=symbol_width)
    hundred.add_horizontal_line(height_str=BOTTOM, direction_str=LEFT)

    # 1000
    thousand = CistercianSymbol(height=symbol_height, width=symbol_width)
    thousand.add_horizontal_line(height_str=BOTTOM, direction_str=RIGHT)

    number_to_symbol = {
        0: CistercianSymbol(height=symbol_height, width=symbol_width, is_zero=True),
        1: one,
        10: ten,
        100: hundred,
        1000: thousand,
    }

    return number_to_symbol
