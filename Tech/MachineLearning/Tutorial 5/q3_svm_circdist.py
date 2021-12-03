#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:15:00 2020

@author: justinkek
"""

# %% CLASSIFICATION ON CIRCULAR DATASET 
# Dataset cannot be classified by simple LDF
# %% IMPORT PACAKAGES 

# IMPORT ALL FUNCTIONS FROM tool.py
from tools import *

# Import SVM from sklearn
from sklearn.svm import SVC

import matplotlib.pyplot as plt
import numpy as np

# set random seed to zero; same numbers everytime code is run
np.random.seed(0)

#%% GENERATE CIRCULAR DISTRIBUTION

X, y = gen_circular_distribution(200)


#%% FIT RBF SVM
svm_rbf_circle = SVC(C=10000, gamma = "auto", kernel = "rbf", degree = 2)
# try kernel = 
    # 'linear', decision boundary only exists as a line
    # 'poly', decision boundary exists as single enclosure
    # 'rbf', multiple enclosures
# try degree = 
    # no degree for rbf, it is an infinite poly?
# try C (how hard boundary is) = 
    # 0.01, some support vectors cross margin
        # increase bias reduce variance
    # 1000, very little support vectors crossing margin
        # opposite is true


svm_rbf_circle.fit(X, y)

#%% GENERATE PREDICTIONS
npx = 200
x1_linear = np.linspace(-10, 10, npx)
x2_linear = x1_linear
x1_grid, x2_grid = np.meshgrid(x1_linear, x2_linear)
Xgrid = np.array([x1_grid, x2_grid]).reshape([2, npx * npx]).T

y_pred = svm_rbf_circle.predict(Xgrid)
y_pred = np.reshape(y_pred, [npx, npx])


# %% PLOT
fig, ax = plt.subplots()
CS = plt.contourf(x1_linear, x2_linear, y_pred, 1)
cbar = fig.colorbar(CS)
ax.scatter(X[y == 0, 0], X[y == 0, 1])
ax.scatter(X[y == 1, 0], X[y == 1, 1])
ax.set_ylim([-10, 10])

plt.title("Rbf SVC Plot for Circular Dataset")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
Z = np.reshape(svm_rbf_circle.decision_function(Xgrid), [npx, npx])
ax.contour(x1_linear, x2_linear, Z, colors = 'k', levels = [-1, 0, 1], alpha = 1, linestyles = ["--", "-", "--"])
sv = svm_rbf_circle.support_vectors_
ax.scatter(sv[:, 0], sv[:, 1], marker = "x", color = "w")

plt.show()