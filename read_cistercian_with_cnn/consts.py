"""
Consts file for CNN training
"""
# Data consts
DATA_MIN_VALUE = 0
DATA_MAX_VALUE = 9   # 9999 is max, lower values selected for quicker training
DATA_MIN_HEIGHT = 7
DATA_MAX_HEIGHT = 100
DATA_MIN_WIDTH = 5
DATA_MAX_WIDTH = 100

# Classifier consts
NUMBER_OF_CLASSES = len(range(DATA_MIN_VALUE, DATA_MAX_VALUE)) + 1  # symbols representing 0-9999
INPUT_SIZE = 28
DENSE_LAYER_UNITS = 128
DROPOUT_RATE = 0.2

# Training consts
BATCH_SIZE = 512
EPOCHS = 100
