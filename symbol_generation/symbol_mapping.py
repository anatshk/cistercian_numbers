
# 1
from symbol_generation.symbol_classes import CistercianSymbol

SYMBOL_HEIGHT = 17
SYMBOL_WIDTH = 13

ONE = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
ONE.add_top_horizontal_line_right()
ONE.show()

# 10
TEN = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
TEN.add_top_horizontal_line_left()
TEN.show()

# 100
HUNDRED = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
HUNDRED.add_bottom_horizontal_line_right()
HUNDRED.show()

# 1000
THOUSAND = CistercianSymbol(height=SYMBOL_HEIGHT, width=SYMBOL_WIDTH)
THOUSAND.add_bottom_horizontal_line_left()
THOUSAND.show()

a = 5
