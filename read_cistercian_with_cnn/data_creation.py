"""
Create a generator of different sized images for model training

see https://colab.research.google.com/drive/1Ndb6zrHXraAstwQV1ws67XbnF88nZ9Hf
for tf  examples

based on example in https://www.tensorflow.org/api_docs/python/tf/keras/utils/Sequence
"""
import tensorflow as tf
from skimage.transform import resize
import numpy as np
import math

from read_cistercian_with_cnn import consts


class CistercianImageGenerator(tf.keras.utils.Sequence):
    def __init__(self, batch_size,
                 min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                 min_height=consts.DATA_MIN_HEIGHT, max_height=consts.DATA_MAX_HEIGHT,
                 min_width=consts.DATA_MIN_WIDTH, max_width=consts.DATA_MAX_WIDTH):

        self.batch_size = batch_size
        self.min_value = min_value
        self.max_value = max_value
        self.min_height = min_height
        self.max_height = max_height
        self.min_width = min_width
        self.max_width = max_width

        self.total_length = (self.max_value - self.min_value + 1) * (self.max_height - self.min_height + 1) \
            * (self.max_width - self.min_width + 1)

    def __len__(self):
        return math.ceil(self.total_length / self.batch_size)
