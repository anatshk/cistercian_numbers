"""
This file contains manually created 2D numpy arrays that represent the Cistercian symbols

see https://github.com/anatshk/cistercian_numbers/blob/main/cistercian_symbols.jpeg

available "strokes" in the symbols -
vertical lines -
 - center of image, full image height
 - top and left of image, 0 to third-of-image height
 - top and right of image, 0 to third-of-image height
 - bottom and left of image, two-third-of-image to end-of-image height
 - bottom and right of image, two-third-of-image to end-of-image height

horizontal lines -
 - top of image, half-width, right of image
 - top of image, half-width, left of image
 - third-height of image, half-width, right of image
 - third-height of image, half-width, left of image
 - two-third-height of image, half-width, right of image
 - two-third-height of image, half-width, left of image
 - bottom of image, half-width, right of image
 - bottom of image, half-width, left of image

diagonal lines, starting from central line | -
 - from top > down, right of image |\
 - from top > down, left of image /|
 - from bottom > up, right of image |/
 - from bottom > up, left of image \|
 - from third-height > up, right of image
 - from third-height > up, left of image
 - from two-third-height > down, right of image
 - from two-third-height > down, left of image
"""
from copy import deepcopy

import matplotlib.pyplot as plt
import numpy as np

TOP = 'top'
BOTTOM = 'bottom'
TOP_THIRD = 'top_third'
BOTTOM_THIRD = 'bottom_third'
LEFT = 'left'
RIGHT = 'right'
MIDDLE = 'mid'
UP = 'up'
DOWN = 'down'


class CistercianSymbol:
    def __init__(self, height, width, is_zero=False):
        self.height = height
        self.width = width
        self.third_height = height // 3
        self.mid_width = width // 2
        self.symbol = np.zeros(shape=(height, width))
        if not is_zero:  # all symbols have a central line
            self.add_central_full_vertical_line()

    def __repr__(self):
        return f"CistercianSymbol({self.height}, {self.width})"

    def show(self):
        plt.imshow(1 - self.symbol, cmap='gray')
        plt.show()

    def _add_vertical_line(self, start, end, x):
        self.symbol[start:end, x] = 1

    def _add_horizontal_line(self, start, end, y):
        self.symbol[y, start:end] = 1

    def _add_diagonal_line(self, start_h, end_h, start_v, end_v):
        step_h = int((int(start_h < end_h) - 1 / 2) * 2)  # convert 0/1 to -1/1
        step_v = int((int(start_v < end_v) - 1 / 2) * 2)  # convert 0/1 to -1/1
        range_h = range(start_h, end_h, step_h)
        range_v = range(start_v, end_v, step_v)
        for h, v in zip(range_h, range_v):
            self.symbol[v, h] = 1
        self.symbol[end_v, max(0, end_h-1)] = 1

    def _get_height(self, height_str: str) -> int:
        if height_str == TOP:
            return 0
        if height_str == BOTTOM:
            return self.height
        if height_str == TOP_THIRD:
            return self.third_height
        if height_str == BOTTOM_THIRD:
            return 2 * self.third_height
        raise Exception(f'Unexpected height string {height_str}')

    def _get_width(self, width_str: str):
        if width_str == LEFT:
            return 0
        if width_str == RIGHT:
            return self.width
        if width_str == MIDDLE:
            return self.mid_width
        raise Exception(f'Unexpected width string {width_str}')

    def add_vertical_line(self, width_str=MIDDLE, start_str=TOP, end_str=BOTTOM):
        start = self._get_height(start_str)
        end = self._get_height(end_str)
        start, end = (start, end) if start < end else (end, start)  # vertical axis is confusing
        location = self._get_width(width_str)
        location = min(location, self.width - 1)  # to take care of location on end index
        self._add_vertical_line(start, end, location)

    def add_central_full_vertical_line(self):
        self.add_vertical_line(width_str=MIDDLE, start_str=TOP, end_str=BOTTOM)

    def add_horizontal_line(self, location_str=TOP, direction_str=LEFT):
        """ add a horizontal line at 'height', starting from central vertical line, going in 'direction'"""
        location = self._get_height(location_str)
        location = min(location, self.height - 1)  # to take care of location on bottom index
        start_str, end_str = (MIDDLE, RIGHT) if direction_str == RIGHT else (LEFT, MIDDLE)
        start, end = self._get_width(start_str), self._get_width(end_str)
        self._add_horizontal_line(start, end, location)

    def add_diagonal_line(self, start_height_on_middle=TOP, end_height=TOP_THIRD, direction_str=LEFT):
        """ diagonals start from center and go outwards """
        start_h = self._get_width(MIDDLE)
        end_h = self._get_width(direction_str)
        start_v = self._get_height(start_height_on_middle)
        end_v = self._get_height(end_height)
        self._add_diagonal_line(start_h, end_h, start_v, end_v)

    def get_value(self):
        # TODO: return the value of a symbol from mapping
        pass

    def fliplr(self):
        """ flip the symbol left-right - return a copy """
        flipped = deepcopy(self)
        flipped.symbol = np.fliplr(flipped.symbol)
        return flipped

    def flipud(self):
        """ flip the symbol up-down - return a copy """
        flipped = deepcopy(self)
        flipped.symbol = np.flipud(flipped.symbol)
        return flipped


class CistercianNumber:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.symbol = CistercianSymbol(height=height, width=width, is_zero=True)
        self.order_used = [False, False, False, False]
        self.value = 0

    def add_symbol(self, symbol):
        # TODO:
        #  check if we can add this symbol
        #  update symbol by max on self
        pass

