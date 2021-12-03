#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:48:45 2020

@author: justinkek
"""
import keras
from keras import layers
from keras import regularizers

#%% Create trial Keras model - Gets about 90% for trial 1
inputs = keras.Input(shape = (5, ))
optimizer = keras.optimizers.SGD(
    learning_rate=0.01, 
    momentum=0.0
    )

dense = layers.Dense(
    units = 64,
    activation = 'elu',
    kernel_regularizer=regularizers.l2(0.01)
    )
x = dense(inputs)
x = layers.Dropout(0.2)(x)
x = layers.Dense(
    units = 64,
    activation = 'elu',
    kernel_regularizer=regularizers.l2(0.01)
    )(x)
x = layers.Dropout(0.2)(x)
x = layers.Dense(
    units = 64,
    activation = 'elu',
    kernel_regularizer=regularizers.l2(0.01)
    )(x)
x = layers.Dropout(0.2)(x)
outputs = layers.Dense(
    units = 2,
    activation = 'softmax'
    )(x)

model = keras.Model(
    inputs = inputs, 
    outputs = outputs, 
    name = "classification_set1"
    )
model.compile(
    loss = "categorical_crossentropy", 
    optimizer = optimizer, 
    metrics = ["accuracy"]
    )

#%% Train model
model.fit(
    x = X_train_c,
    y = y_train_bin,
    batch_size = 64,
    epochs = 200,
    )

#%% Check 
accuracy = model.evaluate(X_test_c, y_test_bin)
print(accuracy)