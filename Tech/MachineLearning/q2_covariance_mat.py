#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAKE FUNCTION TO GENERATE A SUITABLE COVARIANCE MATRIX

Created on Fri Oct  9 16:23:17 2020

@author: justinkek
"""


# %% SETUP

import numpy as np
np.random.seed(0)

import matplotlib.pyplot as plt




# %% FUNCTION TO GENERATE COVARIANCE MATRIX
# Defind by std dev in 2 directions and a rotation

def get_cov(sdx, sdy, rotangdeg):
    
    # initialise covar matrix
    stddev = np.array([[sdx, 0], [0, sdy]])
    # angle in radian
    rot_ang = rotangdeg / 360 * 2 * np.pi
    
    rot_mat = np.array([[np.cos(rot_ang), -np.sin(rot_ang)],
                       [np.sin(rot_ang), np.cos(rot_ang)]])

    # covar matrix is product of rotated matrix and original matrix
    covar = np.matmul(np.matmul(rot_mat, stddev), rot_mat.T)
    return covar

# %% DEFINE MESHGRID FOR PLOTTING

x1line = np.linspace(-1, 1, 200)
x2line = np.linspace(-1, 1, 200)

# generate 2d array for each
x1grid, x2grid = np.meshgrid(x1line, x2line)

# pair up 2d arrays to create 3d matrix
# reshape to 2d array with 2 features and 40000 data points
# transpose to match vertical data format
Xgrid = np.array([x1grid, x2grid]).reshape([2,40000]).T

# %% PRODUCE COVARIANCE MATRIX & PROBABILITY DISTRIBUTION

# xSamp = np.linspace(-1, 1, 40000)

covar = get_cov(1.0, 0.1, 30) 

# produce probability distribution and reshape into grid
p = 1 / (2 * np.pi * np.sqrt(np.linalg.det(covar))) * np.exp(
    -1 / 2 * (np.matmul(Xgrid, np.linalg.inv(covar)) * Xgrid).sum(-1)).reshape(
        [200,200])

# %% PLOT DISTRIBUTION

plt.contourf(x1line, x2line, p)

# %% COMPARE TO NORMAL DISTRIBUTION

test = np.random.multivariate_normal([0, 0], covar, 100)

plt.scatter(test[:,0], test[:,1])

