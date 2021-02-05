"""
CLI script to create Cistercian number symbols
"""
import argparse

from symbol_generation.symbol_mapping import create_symbols
from symbol_generation.translating_cistercian_symbols import arabic_to_cistercian

DEFAULT_HEIGHT = 17
DEFAULT_WIDTH = 15


def main(number_to_convert):
    symbol_mapping = create_symbols(symbol_height=height, symbol_width=width)
    cistercian = arabic_to_cistercian(arabic_number=number_to_convert, symbol_height=height, symbol_width=width,
                                      symbol_mapping=symbol_mapping)

    cistercian.show(title=f'Cistercian representation of {number_to_convert}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--height', '-hh', type=int, help="height of symbols in pixels")
    parser.add_argument('--width', '-ww', type=int, help="width of symbols in pixels")
    args = parser.parse_args()

    height = args.height
    width = args.width

    height = height if height is not None else DEFAULT_HEIGHT
    width = width if width is not None else DEFAULT_WIDTH

    stop_ui = False
    while not stop_ui:
        number = int(input("Enter a number to convert to Cistercian representation (int, [0, 9999]):"))
        main(number_to_convert=number)
        stop_ui = input("Do you want to try another number? (y/n)") == 'n'

    print("Thanks for playing!")
