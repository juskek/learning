#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:24:35 2020

@author: justinkek
"""

import numpy as np
import matplotlib.pyplot as plt
import tools
# from math import arc1tan
from sklearn.decomposition import PCA

np.random.seed(0)

#%% Generate distribution

sdx = 0.3
sdy = 0.1
rot = 23

covar = tools.get_cov(sdx, sdy, rot)
X = np.random.multivariate_normal([0, 0], covar, size=500)

fig, ax = plt.subplots()
ax.plot(X[:,0], X[:,1], '.')
plt.xlabel('X0')
plt.ylabel('X1')
ax.set_xlim([-1.5,1.5])
ax.set_ylim([-1.5,1.5])

#%% PCA

pca = PCA(n_components=2)
pca.fit(X)

# show components
comp = pca.components_
origin = np.array([[0, 0],[0, 0]]) # origin point
plt.quiver(*origin, -comp[:,0], -comp[:,1], color=['r','b'], scale=5)
plt.show()

# calc angle of 1st pc
pc0_x0 = comp[0,0]
pc0_x1 = comp[0,1]

angle = np.arctan(pc0_x1/pc0_x0)
print(angle)