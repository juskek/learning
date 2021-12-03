#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATE AND PLOT A TEST DATASET

Created on Fri Oct  9 15:50:29 2020

@author: justinkek
"""

# %% SETUP

import numpy as np

# set random seed to zero; same numbers everytime code is run
np.random.seed(0)

from sklearn import datasets

import matplotlib.pyplot as plt


# %% MAKE TEST DATASET

# set feature (X) and classification (y) vector
# 100 samples, 2 features (2 informative, zero redundant)
X, y = datasets.make_classification(100, 2, 2, 0)


# %% CHANGE EXAMPLE DATA

# First feature = defect length
# halve std dev and centre around 5 mm
X[:, 0] = X[:, 0] * 0.5 + 5 

# Second feature = brightness
# scale std dev by 30 and mean of 160
X[:, 1] = X[:, 1] * 30 + 160

# %% GENERATE PLOT

# set up figure and axes
fig, ax = plt.subplots()

# scatter plot on axes ax
# plot feature 2 values where y = 0 against feature 1 values where y = 0
ax.scatter(X[y == 0, 0], X[y == 0, 1]) 

# plot again for y = 1
ax.scatter(X[y == 1, 0], X[y == 1, 1]) 

# separate values with predefined curve x2 = -280x1 + 1400
x1 = np.linspace(3, 7.5, 100)
x2 = -100 * x1 + 620
plt.plot(x1,x2)

# show plot
plt.xlim([3,7.5])
plt.ylim([50,250])
plt.show()

