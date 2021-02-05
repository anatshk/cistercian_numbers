"""
This file contains function that creates a mapping of the available values to their symbol instances
"""
from copy import deepcopy

from symbol_generation.symbol_classes import CistercianSymbol, TOP, TOP_THIRD, RIGHT


def create_symbols(symbol_height: int, symbol_width: int) -> dict:
    # 1
    one = CistercianSymbol(height=symbol_height, width=symbol_width)
    one.add_horizontal_line(location_str=TOP, direction_str=RIGHT)

    # 2
    two = CistercianSymbol(height=symbol_height, width=symbol_width)
    two.add_horizontal_line(location_str=TOP_THIRD, direction_str=RIGHT)

    # 3
    three = CistercianSymbol(height=symbol_height, width=symbol_width)
    three.add_diagonal_line(start_height_on_middle=TOP, end_height=TOP_THIRD, direction_str=RIGHT)

    # 4
    four = CistercianSymbol(height=symbol_height, width=symbol_width)
    four.add_diagonal_line(start_height_on_middle=TOP_THIRD, end_height=TOP, direction_str=RIGHT)

    # 5
    five = deepcopy(four)  # 5 is 4 with an additional horizontal line
    five.add_horizontal_line(location_str=TOP, direction_str=RIGHT)

    # 6
    six = CistercianSymbol(height=symbol_height, width=symbol_width)
    six.add_vertical_line(width_str=RIGHT, start_str=TOP, end_str=TOP_THIRD)

    # 7
    seven = deepcopy(six)  # 7 is 6 with an additional horizontal line
    seven.add_horizontal_line(location_str=TOP, direction_str=RIGHT)

    # 8
    eight = deepcopy(six)  # 8 is 6 with an additional horizontal line
    eight.add_horizontal_line(location_str=TOP_THIRD, direction_str=RIGHT)

    # 9
    nine = deepcopy(eight)  # 9 is 8 with an additional horizontal line
    nine.add_horizontal_line(location_str=TOP, direction_str=RIGHT)

    # 10-90 are flips left to right of 1-9
    ten = one.fliplr()
    twenty = two.fliplr()
    thirty = three.fliplr()
    forty = four.fliplr()
    fifty = five.fliplr()
    sixty = six.fliplr()
    seventy = seven.fliplr()
    eighty = eight.fliplr()
    ninety = nine.fliplr()

    # 100-900 are flips up-down of 1-9
    hundred = one.flipud()
    two_hundred = two.flipud()
    three_hundred = three.flipud()
    four_hundred = four.flipud()
    five_hundred = five.flipud()
    six_hundred = six.flipud()
    seven_hundred = seven.flipud()
    eight_hundred = eight.flipud()
    nine_hundred = nine.flipud()

    # 1000-9000 are flips left-right of 10-90
    thousand = ten.flipud()
    two_thousand = twenty.flipud()
    three_thousand = thirty.flipud()
    four_thousand = forty.flipud()
    five_thousand = fifty.flipud()
    six_thousand = sixty.flipud()
    seven_thousand = seventy.flipud()
    eight_thousand = eighty.flipud()
    nine_thousand = ninety.flipud()

    number_to_symbol = {
        0: CistercianSymbol(height=symbol_height, width=symbol_width, is_zero=True),
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        20: twenty,
        30: thirty,
        40: forty,
        50: fifty,
        60: sixty,
        70: seventy,
        80: eighty,
        90: ninety,
        100: hundred,
        200: two_hundred,
        300: three_hundred,
        400: four_hundred,
        500: five_hundred,
        600: six_hundred,
        700: seven_hundred,
        800: eight_hundred,
        900: nine_hundred,
        1000: thousand,
        2000: two_thousand,
        3000: three_thousand,
        4000: four_thousand,
        5000: five_thousand,
        6000: six_thousand,
        7000: seven_thousand,
        8000: eight_thousand,
        9000: nine_thousand,
    }

    return number_to_symbol
