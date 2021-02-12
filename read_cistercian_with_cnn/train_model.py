"""
based on TF MNIST beginners tutorial
https://www.tensorflow.org/tutorials/quickstart/beginner
"""
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split

from read_cistercian_with_cnn import consts
from read_cistercian_with_cnn.data_creation import CistercianImageGenerator

# split the data into train, validation and test - split manually to control different sizes in datasets
# TODO: if all permutations are too large, there may be a memory issue (SIGKILL, exit code 137)
#  - in that case, consider initializing the data generators with save_intermediate_mappings=False
#  (either just the largest train generator or all of them)

height_range = np.arange(consts.DATA_MIN_HEIGHT, consts.DATA_MAX_HEIGHT + 1)
width_range = np.arange(consts.DATA_MIN_WIDTH, consts.DATA_MAX_WIDTH + 1)


def split_datasets(array, test_size, train_size, random_state=90210):
    split = train_test_split(array, test_size=test_size, train_size=train_size, random_state=random_state, shuffle=True)
    return split[0], split[1]


train_height, non_train_height = split_datasets(height_range, test_size=0.4, train_size=0.6)
validation_height, test_height = split_datasets(non_train_height, test_size=0.5, train_size=0.5)
train_width, non_train_width = split_datasets(width_range, test_size=0.4, train_size=0.6)
validation_width, test_width = split_datasets(non_train_width, test_size=0.5, train_size=0.5)

# train data - on all numbers, but part of the available input sizes
train_data_generator = CistercianImageGenerator(batch_size=consts.BATCH_SIZE, network_input_size=consts.INPUT_SIZE,
                                                min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                                                list_of_heights=train_height, list_of_widths=train_width)

# validation data
validation_data_generator = CistercianImageGenerator(batch_size=consts.BATCH_SIZE, network_input_size=consts.INPUT_SIZE,
                                                     min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                                                     list_of_heights=validation_height, list_of_widths=validation_width)

# fit the MNIST-like model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(consts.INPUT_SIZE, consts.INPUT_SIZE)),
  tf.keras.layers.Dense(consts.DENSE_LAYER_UNITS, activation='relu'),
  tf.keras.layers.Dropout(consts.DROPOUT_RATE),
  tf.keras.layers.Dense(consts.NUMBER_OF_CLASSES)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

model.fit(x=train_data_generator, epochs=consts.EPOCHS, validation_data=validation_data_generator,
          shuffle=True, verbose=1)
model.save('cistercian_mnist')

# evaluate on train set - to see if there is over/under fit
performance_train = model.evaluate(x=train_data_generator, verbose=2, return_dict=True)

# evaluate model on remaining data
# create data generators for remaining height and width combinations
test_data_generator = CistercianImageGenerator(batch_size=consts.BATCH_SIZE, network_input_size=consts.INPUT_SIZE,
                                               min_value=consts.DATA_MIN_VALUE, max_value=consts.DATA_MAX_VALUE,
                                               list_of_heights=test_height, list_of_widths=test_width)

# perform evaluations on each of the test generators
performance_test_small = model.evaluate(test_data_generator, verbose=2, return_dict=True)
