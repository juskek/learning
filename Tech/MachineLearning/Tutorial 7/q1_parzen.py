#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:14:20 2020

@author: justinkek
"""

#%% IMPORT

import numpy as np
import matplotlib.pyplot as plt

#  for parzen windows
from sklearn.neighbors import KernelDensity 

#%% Define 40 samples from normal with mean 0 sd 1


mu = 0
sigma = 1
X = np.random.normal(loc=mu, scale=sigma, size = [40,1])

#%% Estimate dist using Parzen windows
# bw = 2h
# centre unit window (kernel) at each data point 
# generate kernel density by superimposition of windows
kde = KernelDensity(kernel='tophat', bandwidth=1).fit(X)


#%% Scale KDE to pdf at a set of test points

x_sample = np.linspace(-5, 5, 1000)
# reshape samples to 2D array for score_samples()
x_sample = x_sample.reshape(len(x_sample), -1)
# convert from score_samples log probability output    
p = np.exp(kde.score_samples(x_sample))

fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].set_title('TopHat Kernel')
ax[0].plot(x_sample,p,label='bw=1')

# repeat for bw = 0.2 and 4.0
kde = KernelDensity(kernel='tophat', bandwidth=0.2).fit(X)
p = np.exp(kde.score_samples(x_sample.reshape(len(x_sample), -1)))
ax[0].plot(x_sample,p,label='bw=0.2')

kde = KernelDensity(kernel='tophat', bandwidth=4.0).fit(X)
p = np.exp(kde.score_samples(x_sample.reshape(len(x_sample), -1)))
ax[0].plot(x_sample,p,label='bw=4.0')


# Plot theoretical dist for comparison
def gen_gaussian(x, mu, sig):
    return 1 / np.sqrt(2 * np.pi) / sig * np.exp(-((x - mu) / sig) ** 2 / 2)
p_true =  gen_gaussian(x = x_sample, mu = mu, sig = sigma)
ax[0].plot(x_sample,p_true,'k--', label='theoretical')
ax[0].legend()

#%% Repeat for gaussian kernels (window)
kde = KernelDensity(kernel='gaussian', bandwidth=1).fit(X)

x_sample = np.linspace(-5, 5, 1000)
p = np.exp(kde.score_samples(x_sample.reshape(len(x_sample), -1)))
ax[1].set_title('Gaussian Kernel')
ax[1].plot(x_sample,p,label='bw=1')

kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
p = np.exp(kde.score_samples(x_sample.reshape(len(x_sample), -1)))
ax[1].plot(x_sample,p,label='bw=0.2')

kde = KernelDensity(kernel='gaussian', bandwidth=4.0).fit(X)
p = np.exp(kde.score_samples(x_sample.reshape(len(x_sample), -1)))
ax[1].plot(x_sample,p,label='bw=4.0')

p_true =  gen_gaussian(x = x_sample, mu = mu, sig = sigma)
ax[1].plot(x_sample,p_true,'k--',label='theoretical')

ax[1].legend()



#%% WINDOW PLOTTING VISUALISATION
# generate exponential window centred at 0
X_vis = np.array([[0]])
kde = KernelDensity(kernel='exponential', bandwidth=0.5).fit(X_vis)
p_vis = np.exp(kde.score_samples(x_sample.reshape(len(x_sample), -1)))
fig2, ax2 = plt.subplots()
ax2.plot(x_sample,p_vis)