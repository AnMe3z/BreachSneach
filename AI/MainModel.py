import tensorflow as tf
import pandas as pd
import numpy as np
import tensorflowjs as tfjs

trainDataset = pd.read_csv('Data/trustWorthy-database.csv', names = ['id', 'entity', 'year', 'records', 'type', 'method']).head(10)
testDataset = pd.read_csv('Data/trustWorthy-database(Test).csv', names = ['id', 'entity', 'year', 'records', 'type', 'method'])

# TODO: check in csv for ""
# TODO: remove head 10
# TODO: output
# TODO: convert nparray to
types = [' ',
        'Orphanage', 
        'Hospital', 
        'Bank', 
        'Supermarket', 
        'Hardware Store', 
        'School', 
        'Shooting Range', 
        'Kindergarden', 
        'Government', 
        'Non-Profit',
        'Train Station',
        'Small Business',
        'Local Shop',
        'Pizzeria',
        'Sandwitch Shop',
        'Burget Franchaise']

t = trainDataset['type'].apply(lambda x: np.isin(types, x).astype(int))
o = trainDataset['method'].apply(lambda x: np.isin(types, x).astype(int))

print(type(t))


model = tf.keras.models.Sequential([
    tf.keras.layers.Input(17),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(25, activation='relu'),
    tf.keras.layers.Dense(19)
])

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam', 
              loss=loss, 
              metrics=['accuracy'])

model.fit(t, o, epochs=5)

# model.evaluate(organizationTypeTest, methodsTest)


