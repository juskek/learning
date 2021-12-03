#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: justinkek
"""

#%% IMPORT

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

from keras.models import Sequential 
from keras.layers import Dense
from keras.utils import to_categorical
from keras.optimizers import SGD

# from statistics import mean

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
# np.random.seed(0)

#%% 1. DATA PROCESSING
# 1.1 RETRIEVE DATA
# df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

npa = np.array(df2)

X = npa[:, 0:6]
 
y = npa[:,6]

# 1.2 PLOT 6 by 6 grid to show data distribution

row = 6
col = row

fig, ax = plt.subplots(row,col)

labels = ['Arm Length','Ball Weight','Ball Radius','Temperature',
          'Elastic Const.','Device Weight']

label_row = ['Row {}'.format(i) for i in labels]
label_col = ['Column {}'.format(j) for j in labels]


# for each row
for i in range(row):
    # each col in each row
    for j in range(col):
        
        # leading diagonal
        if i == j:
            # generate 1D of feature against output
            ax[i,j].plot(npa[:,i],y, '.')
            
            if (i == 0) & (j == 0):
                ax[i,j].set_title(labels[j])
                ax[i,j].set_ylabel(labels[1], size='large')


        # everywhere else
        else:
            # generate 2D plot of feature against feature
            # and colored output
            # scatter(x,y), plot row against col,
            # e.g., row 1 col 2, armlength against ballweight 
            # therefore scatter(col, row)
            ax[i,j].plot(npa[y == 0, j], npa[y == 0, i], 'g.')
            ax[i,j].plot(npa[y == 1, j], npa[y == 1, i], 'r.')
            # ax[i,j].set_title(f'{i} vs. {j} and output')
            if (j == 0) & (i != 0):
                ax[i,j].set_ylabel(labels[i],size='large')
            if (j != 0) & (i == 0):
                ax[i,j].set_title(labels[j])

                
# fig.tight_layout()
plt.show()

# if data looks linearly separable, hidden layers not necessary, i.e., NN not necessary



#%% 2. CREATE MODEL
# 2.1 DENSE SEQUENTIAL NN
    # layers:
        # input: 1 layer, 6 features (nodes)
        # hidden:
            # choices: 
                # ReLU
                # sigmoid
                # softmax
                # softplus
                # softsign
                # tanh
                # selu
                # elu
                # exponential
            # layer 1
                
        # output: softmax (ensure outputs sum to one for Probability)
            # one node per class label
            # therefore 2 nodes (hit, miss)

model = Sequential()
model.add(Dense(units=12, activation='relu', input_dim=6)) 
model.add(Dense(units=6, activation='relu')) 
# model.add(Dense(units=6, activation='relu')) 
model.add(Dense(units=2, activation='softmax')) 
# softmax ensures outputs sum to one so values are treated as P

# categorical crossentropy w1 = 1 or 0, w2 = 1 or 0
opt = SGD(lr=0.01)
model.compile(loss='categorical_crossentropy',
                optimizer=opt,
              metrics=['accuracy'])


#%% 3. TRAIN MODEL
# data points = 2000

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 0)



# # convert 2 output to 1 output (w = 1 or 0)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# SCALE BEFORE TRAINING
# X_train = scale(X_train)
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)

# TRAIN MODEL
model.fit(X_train, y_train, epochs=2000
          , batch_size=32)

#%% TEST CORRECT OUTPUT FORMAT
# X_pred = np.array([mean(X[:,0]), mean(X[:,1]), mean(X[:,2]), 
#                    mean(X[:,3]), mean(X[:,4]), mean(X[:,5])])

# model.predict expects iterable input, 
# change shape from (6,) to (1,6)
# X_pred = np.expand_dims(X_pred, 0) 
# y_pred = model.predict(X_pred)

# print(X_train.mean(axis=0))
# print(X_train.std(axis=0))

#%% 4. TEST MODEL
# SCALE BEFORE TESTING
# X_test = scale(X_test)

X_test = scaler.transform(X_test)
print("Test Set Accuracy:")
model.evaluate(X_test, y_test)
#%% 5. SAVE MODEL & SCALING PARAMETERS
scArray = np.array([scaler.mean_,scaler.scale_]) 
np.savetxt('Kek-Justin-2.txt',scArray)
model.save('Kek-Justin-2.h5')

# newModel = load_model('model.h5')

# [ 2.97234459e-15  6.16822565e-15  1.21264110e-15 -2.00534034e-16
#  -2.43693954e-16  2.86631829e-15]
# [1. 1. 1. 1. 1. 1.]