# -*- coding: utf-8 -*-
"""

"""

# %% CLASSIFICATION ON XOR DATASET (either this or that, noth both or null)
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

# %% GENERATE DATASET AND PLOT  

X, y = gen_xor_distribution(n = 400)

# set up figure and axes
fig, ax = plt.subplots()
plt.title("2-Degree Polynomial SVC Plot for XOR Dataset")
ax.set_xlabel("x1")
ax.set_ylabel("x2")

# scatter plot on axes ax
# plot feature 2 values where y = 0 against feature 1 values where y = 0
ax.scatter(X[y == 0, 0], X[y == 0, 1]) 

# plot again for y = 1
ax.scatter(X[y == 1, 0], X[y == 1, 1]) 

# %% DEFINE SVM

# polynomial basis functions, degree 2
svm = SVC(C=10000,gamma='auto',kernel='poly',degree=2)
# try kernel = 
    # 'linear', decision boundary only exists as a line
    # 'poly', decision boundary exists as two curves
    # 'rbf', 
# try degree = 
    # 2, 
    # 4, 
    # increasing degree causes decision boundary to to conform more to data
    # reduce bias increase variance!
# try C (how hard boundary is) = 
    # 0.01, some support vectors cross margin
        # increase bias reduce variance
    # 1000, very little support vectors crossing margin
        # opposite is true
    
# fit SVM to XOR dataset
svm.fit(X, y)

#%% GENERATE GRID OF PREDICTIONS & PLOT WITH TRAINING DATA
# 1. no of nodes for meshgrid
npx = 200
npy = 200

# 2. define 1D vectors 
x1 = np.linspace(-4, 4, npx)
x2 = np.linspace(-4, 4, npy)

# 3. generate 2D arrays
x1grid, x2grid = np.meshgrid(x1, x2)

# 4. create 3D grid
Xgrid = np.array([x1grid, x2grid])

# 5. revert back to 2D vector for generating y(x) values!
Xgrid = Xgrid.reshape([2, npx * npy]).T

y_pred = svm.predict(Xgrid)

# PREDICTED
# plot feature 2 values where y = 0 against feature 1 values where y = 0
ax.scatter(Xgrid[y_pred == 0, 0], Xgrid[y_pred == 0, 1]) 

# plot again for y = 1
ax.scatter(Xgrid[y_pred == 1, 0], Xgrid[y_pred == 1, 1]) 

# TRAINING
ax.scatter(X[y == 0, 0], X[y == 0, 1]) 
# plot again for y = 1
ax.scatter(X[y == 1, 0], X[y == 1, 1]) 

# can use this too
# CS = plt.contourf(x1_linear, x2_linear, y_pred, 200, cmap = "Spectral")
# cbar = fig.colorbar(CS)

#%% PLOT DECISION FUNCTION
# shows decision boundary (equivalent to previous cell) and margins

ax.scatter(X[y == 0, 0], X[y == 0, 1])
ax.scatter(X[y == 1, 0], X[y == 1, 1])


Z = np.reshape(svm.decision_function(Xgrid), [npx, npx])

ax.contour(x1, x2, Z, colors = 'k', levels = [-1, 0, 1], alpha = 1, 
           linestyles = ["--", "-", "--"])

#%% PLOT SUPPORT VECTORS
sv = svm.support_vectors_
ax.scatter(sv[:, 0], sv[:, 1], marker = "x", color = "k")

#%% 



plt.show()




# ---

# svm = SVC(C=0.01, gamma='auto', kernel='poly', degree=2)

# ---

# Z = np.reshape(svm.decision_function(Xgrid), [npx, npy])
# ax.contour(x1line, x2line, Z, colors='k', levels=[-1, 0, 1], 
# 			alpha=0.5, linestyles=['--', '-', '--'])

# ---

# sv = svm.support_vectors_

# ---

# from sklearn.model_selection import KFold

# kf = KFold(n_splits=5, shuffle=True)
# ---
# for train_index, test_index in kf.split(X):
# 	X_train = X[train_index]
# 	y_train = y[train_index]
# 	X_test = X[test_index]
# 	y_test = y[test_index]

# 	#use X_train, y_train to train the SVM
# 	#...
# 	#use svm.predict() to predict the output for the test data set
# 	#...
# 	#loop through to compare the test data output to what it should be 
# 	#	and obtain the fraction of correct classifications)
# 	#...
# 	#do the same prediction and performance assessment performance 
# 	#	with the training data
# 	#...

# ---
# C_array = np.power(10, np.linspace(-1.5, 1.5, 8))
