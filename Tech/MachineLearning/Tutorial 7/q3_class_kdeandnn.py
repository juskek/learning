#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:22:42 2020

@author: justinkek
"""

#%% IMPORT
import numpy as np
import matplotlib.pyplot as plt

#  for parzen windows
from sklearn.neighbors import KernelDensity 

# for knn
from sklearn.neighbors import KNeighborsClassifier

#%% Generate cicular distribution with 200 points

def gen_circular_distribution(n=500, scale=1):
    a = np.round(n / 7).astype('int')
    b = np.round(2*n / 7).astype('int')
    c = n - a - b
    r1 = np.concatenate(
        [np.random.normal(loc=2, scale=scale, size=[a, 1]), np.random.normal(loc=8, scale=scale, size=[c, 1])])
    r2 = np.random.normal(loc=5, scale=scale, size=[b, 1])

    th1 = np.random.uniform(low=0, high=2 * np.pi, size=[a+c, 1])
    th2 = np.random.uniform(low=0, high=2 * np.pi, size=[b, 1])

    x1a = r1 * np.cos(th1)
    x2a = r1 * np.sin(th1)

    x1b = r2 * np.cos(th2)
    x2b = r2 * np.sin(th2)

    X = np.concatenate([np.concatenate([x1a.reshape([a+c, 1]), x1b.reshape([b, 1])]),
                        np.concatenate([x2a.reshape([a+c, 1]), x2b.reshape([b, 1])])], axis=1)

    y = np.concatenate([np.zeros([a+c, 1]), np.ones([b, 1])]).squeeze()
    return X, y

# split into 2 classes
X, y = gen_circular_distribution(200) 
X1 = X[y == 0, :] 
X2 = X[y == 1, :]

#%% Fit with gaussian kernels with bw 1

b = 1
#b = 0.2 
# smaller bw overfitting
kde1 = KernelDensity(kernel='gaussian', bandwidth=b).fit(X1)
kde2 = KernelDensity(kernel='gaussian', bandwidth=b).fit(X2)

#%% Define image grid 200x200 from -10 to 10
def gen_sample_grid(npx=200, npy=200, limit=1):
    x1line = np.linspace(-limit, limit, npx)
    x2line = np.linspace(-limit, limit, npy)
    x1grid, x2grid = np.meshgrid(x1line, x2line)
    Xgrid = np.array([x1grid, x2grid]).reshape([2,npx*npy]).T
    return Xgrid,x1line,x2line

Xgrid,x1line,x2line = gen_sample_grid(200,200,10)


p1_grid = np.exp(kde1.score_samples(Xgrid)).reshape(200,200)
p2_grid = np.exp(kde2.score_samples(Xgrid)).reshape(200,200)

# take max probability for classifiction
state_of_nature = np.zeros([200,200])
state_of_nature[p1_grid < p2_grid] = 1

#plot
fig, ax = plt.subplots(1,2)
ax[0].contourf(x1line,x2line,state_of_nature)

#%% k-Nearest neighbour classification
# increase k to reduce variance
k = 2
neigh = KNeighborsClassifier(n_neighbors=k) 
neigh.fit(X, y)

son = neigh.predict(Xgrid).reshape(200,200)
ax[1].contourf(x1line,x2line,son)
ax[1].scatter(X[y == 0, 0], X[y == 0, 1])
ax[1].scatter(X[y == 1, 0], X[y == 1, 1])

