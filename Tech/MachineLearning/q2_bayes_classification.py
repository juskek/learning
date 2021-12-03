#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:14:22 2020

@author: justinkek
"""
# %% SETUP

import numpy as np
import matplotlib.pyplot as plt

# affects
np.random.seed(5)

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# %% MAKE DATASET 
# 1000 samples, 2 informative features


X, y = make_classification(n_samples = 1000, n_features = 2, n_informative = 2,
                           n_redundant = 0) # 1000x2, 1000

# %% SPLIT DATASET INTO TRAINING AND TESTING
# 33% IN TEST SET 
    # 
# 66% IN TRAINING SET
    # X_train : parametric
    # y_train : classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)

# %% FIT NAIVE BAYES MODEL TO TRAINING DATA

# Define classifier and train
clf = GaussianNB()
clf.fit(X_train, y_train)

# %% SHOW CLASSIFICATION AREAS OF TWO PARAMETERS

# Generate grid of x for showing areas
x1 = np.linspace(-3, 3, 200) # 200x
x2 = np.linspace(-3, 3, 200) # 200x
x1grid, x2grid = np.meshgrid(x1, x2)
Xgrid = np.array([x1grid, x2grid]).reshape([2, 40000]).T # 40000x2

# Predict y based on trained model for arbitrary x
classVals = clf.predict(Xgrid) # 40000
classVals = np.reshape(classVals, [200, 200]) # 200x200

# Plot
fig, ax = plt.subplots()
CS = plt.contourf(x1, x2, classVals)
cbar = fig.colorbar(CS)

# Show training data
plt.scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1])
plt.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1])
#Too lazy to label (Siew)

# %% CHECK MODEL PERFORMANCE WITH TEST SET

# Predict y based on trained model for test values of x
y_test_model = clf.predict(X_test)

# Check if correct

nTot = len(y_test) # loop counter
nMatch = 0 # correct counter

for i in range(len(y_test)):
    if y_test[i] == y_test_model[i]:
        nMatch += 1

print(nMatch/nTot)

# %% SHOW IMAGE OF POSTERIOR PROBABILITY

# predicted/posterior probability for arb x
probVals = clf.predict_proba(Xgrid) # in 40000 x 2

# reshape to match x1,x2
probGrid_w1 = np.reshape(probVals[:, 0], [200, 200]) # 200x200
probGrid_w2 = np.reshape(probVals[:, 1], [200, 200]) # 200x200

# plot
fig, ax = plt.subplots(1, 2, sharex=True, sharey = True)

# contour plot w1 
CS = ax[0].contourf(x1, x2, probGrid_w1)
# contour plot w2
ax[1].contourf(x1, x2, probGrid_w2)

# show legend
cbar = fig.colorbar(CS)

# label
ax[0].set_title("Probability of w1")
ax[1].set_title("Probability of w2")
fig.text(0.5, 0.02, "x1", ha = "center", va = "center")
fig.text(0.02, 0.5, "x2", ha = "center", va = "center")

