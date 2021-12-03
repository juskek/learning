#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:53:56 2020

@author: justinkek
"""
# %% 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% DEFINE LINEAR DISCRIMINANT FUNCTION

# weight vector
w = np.array([-1, -3])

# bias
w0 = 1

# LDF surface requires meshgrid
# 1. no of nodes for meshgrid
npx = 200
npy = 200

# 2. define 1D vectors 
x1 = np.linspace(0, 1, npx)
x2 = np.linspace(0, 1, npy)

# 3. generate 2D arrays
x1grid, x2grid = np.meshgrid(x1, x2)

# 4. create 3D grid
Xgrid = np.array([x1grid, x2grid])

# 5. revert back to 1D vector for generating y(x) values!
Xgrid = Xgrid.reshape([2, npx * npy])

# # define LDF
g = np.matmul(w, Xgrid) + w0
# reshape to 2D array match surface
g = np.reshape(g, [npx, npy])

# %% PLOT 

# show decision contour
x1_lin = np.linspace(0, 1, npx)
x2_lin = -(1/3) * x1 + 1/3


fig, ax = plt.subplots()
CS = plt.contourf(x1, x2, g, 200)
cbar = fig.colorbar(CS)

plt.title("Linear Discriminant Function Plot")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.plot(x1_lin, x2_lin, color = 'k')

plt.show()