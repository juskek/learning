#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:57:56 2020

@author: justinkek
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

from sklearn import ensemble
from sklearn.neighbors import KNeighborsClassifier

#%% PROBLEM

# 2 outputs y1 y2
    # stateless (doesnt depend on what happened before)
    # 3 states, e.g.,:
        # [1 5] V
        # [2 7]
        # [8 1]
        
# 2 inputs x1 x2
    # continuous from 0 to 10V

#%% A. Find expected voltage for 3 states

# import data
df = pd.read_csv('volts.csv', sep=',')

# separate into input and output
temp = df.to_numpy()

X = temp[:,0:2]
y = temp[:,2:4]

# visualise data
fig, ax = plt.subplots(3,2)
ax[0,0].plot(X[:,0],X[:,1],'.')

ax[0,1].plot(y[:,0],y[:,1],'.')

# apply kmeans clustering
kmeans = KMeans(n_clusters=3)
kmeans = kmeans.fit(y)
km_centers = kmeans.cluster_centers_
print(km_centers)
km_inertia = kmeans.inertia_
# new variable to predict
y_new = kmeans.fit_predict(y)

# visualise predictions
ax[1,0].plot(y[y_new == 0, 0], y[y_new == 0, 1], '.')
ax[1,0].plot(y[y_new == 1, 0], y[y_new == 1, 1], '.')
ax[1,0].plot(y[y_new == 2, 0], y[y_new == 2, 1], '.')

#%% B. Train a random forest for predicting y_new based on X

# estimators = trees
# depth = number of tree branches
rf = ensemble.RandomForestClassifier(n_estimators=100,max_depth=20)
rf.fit(X,y_new)

# Visualise predictions
npx = 500
npy = npx

def gen_sample_grid(npx=200, npy=200, ulim=1, llim = -1):
    x1line = np.linspace(-llim, ulim, npx)
    x2line = np.linspace(-llim, ulim, npy)
    x1grid, x2grid = np.meshgrid(x1line, x2line)
    Xgrid = np.array([x1grid, x2grid]).reshape([2,npx*npy]).T
    return Xgrid,x1line,x2line

Xgrid,x1line,x2line = gen_sample_grid(npx,npy,10, 0)


rf_pred = rf.predict(Xgrid)
rf_pred_plot = rf_pred[:].reshape(npx,npy)

ax[1,1].contourf(x1line,x2line,rf_pred_plot)
# uncomment to check
# ax[1,1].plot(X[y_new == 0, 0], X[y_new == 0, 1],'.')
# ax[1,1].plot(X[y_new == 1, 0], X[y_new == 1, 1],'.')
# ax[1,1].plot(X[y_new == 2, 0], X[y_new == 2, 1],'.')

#%% C. USe nearest neighbour for predicting y_new based on X
# increase k to reduce variance
k = 1
neigh = KNeighborsClassifier(n_neighbors=k) 
neigh.fit(X, y_new)

son = neigh.predict(Xgrid).reshape(npx,npy)

ax[2,0].contourf(x1line,x2line,son)
# ax[2,0].scatter(X[y_new == 0, 0], X[y_new == 0, 1])
# ax[2,0].scatter(X[y_new == 1, 0], X[y_new == 1, 1])

