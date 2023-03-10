import tensorflow as tf
import tensorflowjs as tfjs
import pandas as pd
import numpy as np

trainDataset = pd.read_csv('trustWorthy-database.csv')
testDataset = pd.read_csv('trustWorthy-database(Test).csv')

(x_train, y_train) = trainDataset.load_data()
(x_test, y_test) = testDataset.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam', 
              loss=loss, 
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test)

tfjs.converters.save_keras_model(model, "TensorflowJS")
