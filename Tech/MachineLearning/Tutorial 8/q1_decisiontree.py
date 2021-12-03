#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:35:25 2020

@author: justinkek
"""

from sklearn import datasets
from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt

#%% Generate 2 class dataset

def gen_sample_grid(npx=200, npy=200, limit=1):
  x1line = np.linspace(-limit, limit, npx)
  x2line = np.linspace(-limit, limit, npy)
  x1grid, x2grid = np.meshgrid(x1line, x2line)
  Xgrid = np.array([x1grid, x2grid]).reshape([2,npx*npy]).T
  return Xgrid,x1line,x2line

X, y = datasets.make_classification(n_samples=100, n_features=2,                                    
				n_informative=2, n_redundant=0)

#%% Fit with decision tree

clf = tree.DecisionTreeClassifier() 
clf = clf.fit(X, y)

#%% Generate sample predictions
Xgrid,x1line,x2line = gen_sample_grid(200,200,4)
pred = clf.predict(Xgrid).reshape(200,200)

# plot
fig, ax = plt.subplots()
plt.contourf(x1line,x2line,pred)
ax.scatter(X[y == 0, 0], X[y == 0, 1])
ax.scatter(X[y == 1, 0], X[y == 1, 1])

# decision tree very blocky, 