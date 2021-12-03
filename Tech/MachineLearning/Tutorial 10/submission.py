#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:53:32 2020

@author: justinkek
"""

#%% PROBLEM

# object
    # mass, m
# forces
    # f1 N @ f1_ang
    # f2 N @ f2_ang
    # angle CCW from x-axis
# will object slip under these forces?

#%% IMPORT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC

from keras.models import Sequential 
from keras.models import load_model
from keras.layers import Dense
from keras.utils import *
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

import math 

np.random.seed(0)

#%% DATA

slip_data = pd.read_csv('slip_data.csv')

y = (slip_data.to_numpy())[:,5]
f1 = (slip_data.to_numpy())[:,0:2]
f2 = (slip_data.to_numpy())[:,2:4]

# visualise
fig, ax = plt.subplots(3,2)
# Set common labels
plt.setp(ax[:, :], xlabel='f2')
plt.setp(ax[:, :], ylabel='f2ang')
plt.tight_layout()

ax[0,0].plot(f2[y == 0, 0], f2[y == 0, 1], '.') # no slip inside
ax[0,0].plot(f2[y == 1, 0], f2[y == 1, 1], '.') # slip outside
ax[0,0].set_title('Scatter Plot of Raw Data')

# NN or SVM?
# SVM as dataset looks 

#%% A. FIND DECISION BOUNDARY FOR SLIP/NO SLIP

#%% FIT RBF SVM
svm_rbf_circle = SVC(C=1000, gamma = "scale", kernel = "rbf")
# try kernel = 
    # 'linear', decision boundary only exists as a line
    # 'poly', decision boundary exists as single enclosure
    # 'rbf', multiple enclosures
# try degree = 
    # no degree for rbf, it is an infinite poly?
# try C (how hard boundary is) = 
    # 0.01, some support vectors cross margin
        # increase bias reduce variance
    # 1000, very little support vectors crossing margin
        # opposite is true


svm_rbf_circle.fit(f2, y)

# GENERATE PREDICTIONS
npx = 200
x1_linear = np.linspace(0, 40, npx)
x2_linear = np.linspace(0, 360, npx)
x1_grid, x2_grid = np.meshgrid(x1_linear, x2_linear)
Xgrid = np.array([x1_grid, x2_grid]).reshape([2, npx * npx]).T

y_svm = svm_rbf_circle.predict(Xgrid)
y_svm = np.reshape(y_svm, [npx, npx])


# # PLOT
# underlying data
# ax[0,1].plot(f2[y == 0, 0], f2[y == 0, 1], '.')
# ax[0,1].plot(f2[y == 1, 0], f2[y == 1, 1], '.')
pred_contour = np.reshape(svm_rbf_circle.decision_function(Xgrid), [npx, npx])
# ax[0,1].contour(x1_linear, x2_linear, pred_contour, colors = 'k', levels = 0, 
#                 alpha = 1, linestyles = "-")
ax[0,1].contourf(x1_linear, x2_linear, pred_contour, levels=0) # polka dot z-values here are 0s and 1s
proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) 
    for pc in ax[0,1].collections]
ax[0,1].legend(proxy, ["no slip", "slip"])
ax[0,1].set_title('SVM RBF, f1=18, f1ang=20')

# sv = svm_rbf_circle.support_vectors_
# ax[0,1].scatter(sv[:, 0], sv[:, 1], marker = "x", color = "w")



#%% FIT NN
# # DENSE SEQUENTIAL NN
#     # 3 layers:
#             # input: 2 inputs
#             # hidden: 1 tanh, 4 units ea
#             # output: softmax, 2 units

# model = Sequential()

# model.add(Dense(units=4, activation='tanh', input_dim=2)) 
# model.add(Dense(units=2, activation='softmax')) 
# # softmax ensures outputs sum to one so values are treated as P

# # categorical crossentropy w1 = 1 or 0, w2 = 1 or 0
# model.compile(loss='categorical_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'])


# # convert 2 output to 1 output (w = 1 or 0)
# y_binary = to_categorical(y)
# scaler = StandardScaler().fit(f2)
# f2_scaled = scaler.transform(f2)

# model.fit(f2_scaled, y_binary, epochs=1200, batch_size=32)

# scaler = StandardScaler().fit(Xgrid)
# Xgrid_scaled = scaler.transform(Xgrid)
# y_nn = model.predict(Xgrid_scaled)

# # select appropriate output (should sum to 1)
# # reshape to grid for plotting 
# y_nn = np.reshape(y_nn[:, 0], [200, 200])


# # # PLOT
# ax[1,0].contourf(x1_linear,x2_linear,y_nn)

# ax[1,0].plot(f2[y == 0, 0], f2[y == 0, 1], '.')
# ax[1,0].plot(f2[y == 1, 0], f2[y == 1, 1], '.')

#%% C. TRADITIONAL APPROACH TO SLIP/NOSLIP
# mass = (slip_data.to_numpy())[:,4]
mass = 3
mu = 0.5 
friction = mu * 9.81 * mass

npc = 200
# f1_lin = np.zeros([npc])
# f1_lin[:] = 18
# f1ang_lin = np.zeros([npc])
# f1ang_lin[:] = 20 

f1_lin = 18
f1ang_lin = 20


f2_lin = np.linspace(0, 40, npc)
f2ang_lin = np.linspace(0, 360, npc)

f2_lin_grid, f2ang_lin_grid = np.meshgrid(x1_linear, x2_linear)
f2grid = np.array([f2_lin_grid, f2ang_lin_grid])

Fx = f1_lin*(np.cos(np.deg2rad(f1ang_lin))) + f2_lin_grid*np.cos(
    np.deg2rad(f2ang_lin_grid))
Fy = f1_lin*np.sin(np.deg2rad(f1ang_lin)) + f2_lin_grid*np.sin(
   np.deg2rad(f2ang_lin_grid))
Fr = np.sqrt(Fx**2 + Fy**2)

y_theo = np.zeros([npc,npc])

y_theo[Fr>=friction] = 1

ax[1,1].contourf(f2_lin,f2ang_lin,y_theo)
proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) 
    for pc in ax[1,1].collections]
ax[1,1].legend(proxy, ["no slip", "slip"])
ax[1,1].set_title('Theoretical Approach, f1=18, f1ang = 20')
#%% D. VARYING f1
f1_lin = 10
f1ang_lin = 30


f2_lin = np.linspace(0, 40, npc)
f2ang_lin = np.linspace(0, 360, npc)

f2_lin_grid, f2ang_lin_grid = np.meshgrid(x1_linear, x2_linear)
f2grid = np.array([f2_lin_grid, f2ang_lin_grid])

Fx = f1_lin*(np.cos(np.deg2rad(f1ang_lin))) + f2_lin_grid*np.cos(
    np.deg2rad(f2ang_lin_grid))
Fy = f1_lin*np.sin(np.deg2rad(f1ang_lin)) + f2_lin_grid*np.sin(
   np.deg2rad(f2ang_lin_grid))
Fr = np.sqrt(Fx**2 + Fy**2)

y_theo = np.zeros([npc,npc])

y_theo[Fr>=friction] = 1

ax[2,0].contourf(f2_lin,f2ang_lin,y_theo)
proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) 
    for pc in ax[1,1].collections]
ax[2,0].legend(proxy, ["no slip", "slip"])
ax[2,0].set_title('Theoretical Approach, f1=10, f1ang=30')
#%% D. VARYING f1

slip_data_full = pd.read_csv('slip_data_full.csv')
y = (slip_data_full.to_numpy())[:,5]
f1 = (slip_data_full.to_numpy())[:,0:2]
f2 = (slip_data_full.to_numpy())[:,2:4]

X = (slip_data_full.to_numpy())[:,0:4]
# cannot visualise 4D
# only plot for f1 = 10 and f1ang = 30


# FIT RBF SVM
svm_rbf_circle = SVC(C=1000, gamma = "scale", kernel = "rbf")

svm_rbf_circle.fit(X, y)

# GENERATE PREDICTIONS
npd = 200
# f1 grids
f1_grid = np.full((npd, npd), 10)
f1a_grid = np.full((npd, npd), 30)

f2_linear = np.linspace(0, 40, npd)
f2a_linear = np.linspace(0, 360, npd)
# f2 grids
f2_grid, f2a_grid = np.meshgrid(f2_linear, f2a_linear)

Xgrid = np.array([f1_grid, f1a_grid, f2_grid, f2a_grid]).reshape([4, npx * npx]).T

y_svm = svm_rbf_circle.predict(Xgrid)
y_svm = np.reshape(y_svm, [npx, npx])


# # PLOT

pred_contour = np.reshape(svm_rbf_circle.decision_function(Xgrid), [npx, npx])

ax[2,1].contourf(x1_linear, x2_linear, pred_contour, levels=0) # polka dot z-values here are 0s and 1s
proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) 
    for pc in ax[0,1].collections]
ax[2,1].legend(proxy, ["no slip", "slip"])
ax[2,1].set_title('SVM RBF, f1=10, f1ang=30')
