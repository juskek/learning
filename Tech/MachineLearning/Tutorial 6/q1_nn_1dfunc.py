#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:39:43 2020

@author: justinkek
"""

#%% IMPORT


import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(0)

from keras.models import Sequential 
from keras.layers import Dense

#%% PLOT RAW FUNCTION
# x vector
x = np.linspace(0, 1, 200)

#set up a function of x 
y = x.copy() 
#^ note that we don't actually end up using y = x 
# anywhere, but it does set up the array

# initialise piecewise function for y 
#y = 0 for x < 0.1
#add a gradient of +0.5 if x >= 0.5
#^ gradient downwards from 0.6 to 0.8 (gradient 
y[x < 0.1] = 0 
y[x >= 0.1] = 0.5*(x[x >= 0.1]-0.1)
y[x >= 0.6] = 0.25-0.25/0.2*(x[x >= 0.6]-0.6) 
#calculated so that line goes from 
#(0.6, 0.25) -> (0.8, 0), i.e. joins up with the other segments)

y[x > 0.8] = 0 #y = 0 for x > 0.8

fig, ax = plt.subplots() 
plt.plot(x,y)
#%% FIT FUNCTION WITH KERAS


#set up a sequential neural network
model = Sequential()
    # ADD COMPLEXITY TO MODEL
        # 3 vs 150 nodes
        # 200 vs 2000 epochs

#add a layer of 3 nodes of ReLUs, taking a single parametric input
model.add(Dense(units=150, activation='relu', input_dim=1))
#add a linear node at the end to combine the nodes together
model.add(Dense(units=1, activation='linear'))

#compile the model, trying to minimise mean squared 
#error and using the Adam algorithm to fit this
model.compile(loss="mean_squared_error",
              optimizer='adam',
                metrics=['accuracy'])

#fit the data provided previously, using 200 epochs and a batch size of 32
model.fit(x, y, epochs=2000, batch_size=32)

#obtain a predicted set of values from the fitted function along its length
y_pred = model.predict(x)

# SET WEIGHTS MANUALLY FOR BETTER FIT
    # model.layers[0].set_weights([np.array([[0.5, -(-0.5-0.25/0.2), 0.25/0.2]],), np.array([-0.5*0.1, (-0.5-0.25/0.2)*0.6, -(0.25/0.2)*0.8],)]) 
    # model.layers[1].set_weights([np.array([[1],[-1],[1]],), np.array([0],)])
#%%
# PLOT
plt.plot(x,y_pred, '.')
fig.legend(handles = (ax.get_children() ), labels = ('Raw Data','Neural Net Fit',),loc = "lower right")


plt.show()


