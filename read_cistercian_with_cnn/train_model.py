"""
based on TF MNIST beginners tutorial
https://www.tensorflow.org/tutorials/quickstart/beginner
"""
import tensorflow as tf

from read_cistercian_with_cnn import consts

# MNIST-like model
from read_cistercian_with_cnn.data_creation import CistercianImageGenerator

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(consts.INPUT_SIZE, consts.INPUT_SIZE)),
  tf.keras.layers.Dense(consts.DENSE_LAYER_UNITS, activation='relu'),
  tf.keras.layers.Dropout(consts.DROPOUT_RATE),
  tf.keras.layers.Dense(consts.NUMBER_OF_CLASSES)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# model fit - with a Sequence generator
# train data - on all numbers, but part of the available input sizes
train_min_height = consts.DATA_MIN_HEIGHT + 5
train_max_height = consts.DATA_MAX_HEIGHT - 5
train_min_width = consts.DATA_MIN_WIDTH + 5
train_max_width = consts.DATA_MAX_WIDTH - 5
train_data_generator = CistercianImageGenerator(batch_size=32, network_input_size=consts.INPUT_SIZE,
                                                min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                                                min_height=train_min_height, max_height=train_max_height,
                                                min_width=train_min_width, max_width=train_max_width)

model.fit(x=train_data_generator, epochs=100, validation_split=0.2, shuffle=True, verbose=1)

# evaluate on train set - to see if there is over/under fit
performance_train = model.evaluate(x=train_data_generator, verbose=2, return_dict=True)

# evaluate model on remaining data
# create data generators for remaining height and width combinations
test_data_generator_small = CistercianImageGenerator(batch_size=32, network_input_size=consts.INPUT_SIZE,
                                                     min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                                                     min_height=consts.DATA_MIN_HEIGHT, max_height=train_min_height,
                                                     min_width=consts.DATA_MIN_WIDTH, max_width=train_min_width)

test_data_generator_large = CistercianImageGenerator(batch_size=32, network_input_size=consts.INPUT_SIZE,
                                                     min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                                                     min_height=train_max_height, max_height=consts.DATA_MAX_HEIGHT,
                                                     min_width=train_max_width, max_width=consts.DATA_MAX_WIDTH)

test_data_generator_small_height = CistercianImageGenerator(batch_size=32, network_input_size=consts.INPUT_SIZE,
                                                            min_value=consts.DATA_MIN_VALUE,
                                                            max_value=consts.DATA_MAX_VALUE,
                                                            min_height=consts.DATA_MIN_HEIGHT,
                                                            max_height=train_min_height,
                                                            min_width=train_max_width, max_width=consts.DATA_MAX_WIDTH)

test_data_generator_small_width = CistercianImageGenerator(batch_size=32, network_input_size=consts.INPUT_SIZE,
                                                           min_value=consts.DATA_MIN_VALUE,
                                                           max_value=consts.DATA_MAX_VALUE,
                                                           min_height=train_max_height,
                                                           max_height=consts.DATA_MAX_HEIGHT,
                                                           min_width=consts.DATA_MIN_WIDTH, max_width=train_min_width)

# perform evaluations on each of the test generators
performance_test_small = model.evaluate(test_data_generator_small, verbose=2, return_dict=True)
performance_test_large = model.evaluate(test_data_generator_large, verbose=2, return_dict=True)
performance_test_small_height = model.evaluate(test_data_generator_small_height, verbose=2, return_dict=True)
performance_test_small_width = model.evaluate(test_data_generator_small_width, verbose=2, return_dict=True)

# TODO: average the losses per test set and see conclusions
