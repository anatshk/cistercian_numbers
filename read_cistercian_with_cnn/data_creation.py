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
    def __init__(self, batch_size, network_input_size=consts.INPUT_SIZE,
                 min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                 min_height=consts.DATA_MIN_HEIGHT, max_height=consts.DATA_MAX_HEIGHT,
                 min_width=consts.DATA_MIN_WIDTH, max_width=consts.DATA_MAX_WIDTH):

        self.batch_size = batch_size
        self.network_input_size = network_input_size
        self.min_value = min_value
        self.max_value = max_value
        self.min_height = min_height
        self.max_height = max_height
        self.min_width = min_width
        self.max_width = max_width

        self._create_all_permutations()

    def _create_all_permutations(self):
        numbers = np.arange(self.min_value, self.max_value + 1, 1)
        height = np.arange(self.min_height, self.max_height + 1, 1)
        width = np.arange(self.min_width, self.max_width + 1, 1)
        n, h, w = np.meshgrid(numbers, height, width)
        self.y = n.flatten()
        self.x_dims = list(zip(h.flatten(), w.flatten()))

    def __len__(self):
        return math.ceil(len(self.y) / self.batch_size)

    def _create_x_arrays_for_training(self, numbers, dimension_tuples):
        # TODO: create numbers on the fly
        pass

    def __getitem__(self, idx):
        batch_x_dims = self.x_dims[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]

        # time <> memory tradeoff - we can create all the symbol mappings in advance and save numpy files
        # (~36MB per 10K numbers of given size) or create the numpy arrays on the fly
        batch_x = self._create_x_arrays_for_training(numbers=batch_y, dimension_tuples=batch_x_dims)

        return batch_x, batch_y
