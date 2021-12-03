#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:00:15 2020

@author: justinkek
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

#%% Generate test data
n_samples = 1500
blobs = 3
X, y = make_blobs(n_samples=n_samples, centers=blobs, cluster_std=1)

fig, ax = plt.subplots(2,2)
ax[0,0].scatter(X[y == 0, 0], X[y == 0, 1])
ax[0,0].scatter(X[y == 1, 0], X[y == 1, 1])
ax[0,0].scatter(X[y == 2, 0], X[y == 2, 1])
ax[0,0].scatter(X[y == 3, 0], X[y == 3, 1])
ax[0,0].scatter(X[y == 4, 0], X[y == 4, 1])
ax[0,0].scatter(X[y == 5, 0], X[y == 5, 1])
#%% Apply KMeans Clustering

kmeans = KMeans(n_clusters=6)
kmeans = kmeans.fit(X)
km_centers = kmeans.cluster_centers_
km_inertia = kmeans.inertia_
kmeans = kmeans.fit_predict(X)

ax[0,1].scatter(X[kmeans == 0, 0], X[kmeans == 0, 1])
ax[0,1].scatter(X[kmeans == 1, 0], X[kmeans == 1, 1])
ax[0,1].scatter(X[kmeans == 2, 0], X[kmeans == 2, 1])
ax[0,1].scatter(X[kmeans == 3, 0], X[kmeans == 3, 1])
ax[0,1].scatter(X[kmeans == 4, 0], X[kmeans == 4, 1])
ax[0,1].scatter(X[kmeans == 5, 0], X[kmeans == 5, 1])

#%% AffinityPropagation

# aprop = AffinityPropagation()

#%% DBSCAN




# km.cluster_centers_
# km.inertia_
# from sklearn.decomposition import PCA
# ...
# pca = PCA(n_components=2)
# pca.fit(X