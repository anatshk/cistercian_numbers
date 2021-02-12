"""
based on TF MNIST beginners tutorial
https://www.tensorflow.org/tutorials/quickstart/beginner
"""
import tensorflow as tf

from read_cistercian_with_cnn import consts

# MNIST-like model
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

