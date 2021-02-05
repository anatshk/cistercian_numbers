"""
CLI script to create Cistercian number symbols
"""
import argparse

from symbol_generation.translating_cistercian_symbols import CistercianNumber, arabic_to_cistercian


def main(symbol_height: int, symbol_width: int, number: int):
    cistercian = arabic_to_cistercian(number)

if __name__ == "__main__":
