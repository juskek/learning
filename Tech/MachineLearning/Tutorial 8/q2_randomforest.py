#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:04:04 2020

@author: justinkek
"""
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble

#%% Generate 2 class dataset

def gen_sample_grid(npx=200, npy=200, limit=1):
  x1line = np.linspace(-limit, limit, npx)
  x2line = np.linspace(-limit, limit, npy)
  x1grid, x2grid = np.meshgrid(x1line, x2line)
  Xgrid = np.array([x1grid, x2grid]).reshape([2,npx*npy]).T
  return Xgrid,x1line,x2line

X, y = datasets.make_classification(n_samples=100, n_features=2,                                    
				n_informative=2, n_redundant=0)

#%% Fit with random forest

# estimators = trees
# depth = number of tree branches
rf = ensemble.RandomForestClassifier(n_estimators=200,max_depth=20)
rf.fit(X,y)

#%% Visualise predictions
Xgrid,x1line,x2line = gen_sample_grid(200,200,4)

prob = rf.predict_proba(Xgrid)
prob_plot = prob[:,0].reshape(200,200)

fig, ax = plt.subplots()
plt.contourf(x1line,x2line,prob_plot)
ax.scatter(X[y == 0, 0], X[y == 0, 1])
ax.scatter(X[y == 1, 0], X[y == 1, 1])


# generates probability instead of classification