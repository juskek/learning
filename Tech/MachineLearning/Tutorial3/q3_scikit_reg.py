#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:23:58 2020

@author: justinkek
"""

# REGRESSION BASED ON FREQUENCY AND TEMPERATURE

# %% IMPORT PACKAGES

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from mpl_toolkits.mplot3d import Axes3D

# %% READ DATA

df = pd.read_csv('http://pogo.software/me4ml/hdpeVel.csv')
# set index to temperature
df = df.set_index('T/C f/MHz')
print(df)

# %% EXTRACT VALUES & SCALE FREQUENCY
freq = df.columns.values.astype(np.float) * 1e6
temp = df.index.values.astype(np.float)

# convert DF to NP velocity values
vel = df.to_numpy()

# calculate total values for generating grid
tot_values = len(freq) * len(temp)

# %% GENERATE GRID OF FREQ AND TEMP
x1grid, x2grid = np.meshgrid(freq, temp)
Xgrid = np.concatenate([x1grid.reshape([tot_values, 1]), x2grid.reshape([tot_values, 1])], axis = 1)
ygrid = vel.reshape([tot_values, 1])


# X_train, X_test, y_train, y_test = train_test_split(Xgrid, ygrid, test_size = 0.33, random_state = 69)

# %% LEARN REGRESSION WITH LINEAR PREDICTORS
reg = LinearRegression()
reg.fit(Xgrid, ygrid)
y_lin = reg.predict(Xgrid)


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(Xgrid[:, 0], Xgrid[:, 1], ygrid, marker = 'x', color = '#000000')
ax.scatter(Xgrid[:, 0], Xgrid[:, 1], y_lin, marker = 'o', color = '#ff0000')

# %% INTERACIVE PLOT IN JUPYTER NOTEBOOK
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter3d(x = Xgrid[:, 0], y = Xgrid[:, 1], z = ygrid[:, 0], mode = 'markers', 
                           marker = dict(size = 2, color = '#000000', symbol = 'x')))
fig.add_trace(go.Scatter3d(x = Xgrid[:, 0], y = Xgrid[:, 1], z = y_lin[:, 0], mode = 'markers', 
                           marker = dict(size = 3, color = '#ff0000', symbol = 'circle')))


# %% LINEAR REGRESSION WITH POLYNOMIAL PREDICTORS
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 2)
X_poly = poly.fit_transform(Xgrid)

print(X_poly.shape)
print(poly.powers_)



reg_poly = LinearRegression()
reg_poly.fit(X_poly, ygrid)
y_poly = reg_poly.predict(X_poly)


# %% INTERACIVE PLOT IN JUPYTER NOTEBOOK
fig = go.Figure()
fig.add_trace(go.Scatter3d(x = Xgrid[:, 0], y = Xgrid[:, 1], z = ygrid[:, 0], mode = 'markers', 
                           marker = dict(size = 2, color = '#000000', symbol = 'x')))
fig.add_trace(go.Scatter3d(x = Xgrid[:, 0], y = Xgrid[:, 1], z = y_lin[:, 0], mode = 'markers', 
                           marker = dict(size = 3, color = '#ff0000', symbol = 'circle')))
fig.add_trace(go.Scatter3d(x = Xgrid[:, 0], y = Xgrid[:, 1], z = y_poly[:, 0], mode = 'markers', 
                           marker = dict(size = 3, color = '#00ff00', symbol = 'diamond')))

