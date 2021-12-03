#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:37:53 2020

@author: justinkek
"""

#%% IMPORT

import numpy as np 
import matplotlib.pyplot as plt

from keras.models import Sequential 
from keras.models import load_model
from keras.layers import Dense
from keras.utils import *

from tools import *

#%% GENERATE CIRCULAR DISTRIBUTION

X, y = gen_simple_circular_distribution(200)


#%% DENSE SEQUENTIAL NN
    # 4 layers:
            # input: 2 inputs
            # hidden: 2 ReLU, 4 units ea
            # output: softmax, 2 units

model = Sequential()

model.add(Dense(units=4, activation='relu', input_dim=2)) 
model.add(Dense(units=4, activation='relu')) 
model.add(Dense(units=2, activation='softmax')) 
# softmax ensures outputs sum to one so values are treated as P

# categorical crossentropy w1 = 1 or 0, w2 = 1 or 0
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])


#overfitting example:
# X, y = gen_simple_circular_distribution(n=40,scale=2)
# model.add(Dense(units=6, activation='relu', input_dim=2)) 
# model.add(Dense(units=6, activation='relu')) 
# model.add(Dense(units=6, activation='relu')) 
# model.add(Dense(units=2, activation='softmax')) 


# convert 2 output to 1 output (w = 1 or 0)
y_binary = to_categorical(y)

model.fit(X, y_binary, epochs=250, batch_size=32)
#overfitting example:
#model.fit(X, y_binary, epochs=1000, batch_size=32)


#%% GRID

npx = 200

x1_linear = np.linspace(-10, 10, npx)
x2_linear = x1_linear
x1_grid, x2_grid = np.meshgrid(x1_linear, x2_linear)
Xgrid = np.array([x1_grid, x2_grid]).reshape([2, npx * npx]).T

y_pred = model.predict(Xgrid)

# select appropriate output (should sum to 1)
# reshape to grid for plotting 
y_pred = np.reshape(y_pred[:, 0], [200, 200])


# %% OR USE GRID FUNCTION
# lim = 10
# Xgrid,x1line,x2line = gen_sample_grid(limit=lim)

# def gen_sample_grid(npx=200, npy=200, limit=1):
#   x1line = np.linspace(-limit, limit, npx)
#   x2line = np.linspace(-limit, limit, npy)
#   x1grid, x2grid = np.meshgrid(x1line, x2line)
#   Xgrid = np.array([x1grid, x2grid]).reshape([2,npx*npy]).T
#   return Xgrid,x1line,x2line

# %% PLOT
fig, ax = plt.subplots()

plt.contourf(x1_linear,x2_linear,y_pred)
ax.scatter(X[y == 0, 0], X[y == 0, 1])
ax.scatter(X[y == 1, 0], X[y == 1, 1])
# plt.contourf(x1_linear,x2_linear,y_pred)

# ---
model.save('model.h5')

newModel = load_model('model.h5')
