#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:24:04 2020

@author: justinkek
"""

# %% IMPORT PACKAGES

import pandas as pd
import numpy as np

# %% READ FILE

# df = pd.read_csv('xray.csv')
# OR
df = pd.read_csv('http://pogo.software/me4ml/xray.csv')

x = np.array(df['Distance (mm)'][:]) 
y = np.array(df['Total absorption'][:])


# %% SCATTER PLOT RAW DATA

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.scatter(x, y, marker = '.')
plt.title("Absorption vs. Distance")
ax.set_xlabel("Distance")
ax.set_ylabel("Absorption")

# %% TRANSFORM DATA

# Log transform does not linearise data
# ln_x = np.log(x)
# fig, ax = plt.subplots()
# plt.scatter(ln_x, y, marker = '.')
# plt.title("Total Absorption against Distance Travelled")
# ax.set_xlabel("Distance (mm)")
# ax.set_ylabel("Total Absorption")
# plt.show()

# %% FIT LINEAR MODEL (MATRIX FORMULATION)
# Find terms
x_sum = np.sum(x)
x_sum_2 = np.sum(x**2)
m = len(x)
yx_sum = np.matmul(x, y).sum()
y_sum = np.sum(y)

# delcare rhs and change from 1x2 to 2x1
rhs = np.array([yx_sum, y_sum]).T

# declare lhs and inverse to bring over to rhs
lhs = np.array([[x_sum, x_sum_2], [m, x_sum]])
lhs = np.linalg.inv(lhs)

# solve for beta
beta1 = np.matmul(lhs,rhs)

# OR 
# beta = np.linalg.solve(lhs,rhs)

# plot

line_x = np.linspace(0, 6, 200)
line_y = beta1[0] + beta1[1] * line_x

plt.plot(line_x, line_y, 'k.')


# %% FIT LINEAR MODEL (NORMAL EQUATION)

# generate vector of ones for beta_0
x0 = np.ones(len(x))

# add to first column 
X = np.array([x0, x]).T

# solve for beta
term_1 = np.matmul(X.T, X)
term_2 = np.matmul(X.T,y)
beta2 = np.linalg.solve(term_1,term_2)

# beta2 = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), y)
# display(beta)
line_y = beta2[0] + beta2[1] * line_x

plt.plot(line_x, line_y, color = 'g')

# %% FIT QUADRATIC MODEL (NORMAL EQUATION)
X = np.array([x0, x, x**2]).T

term_1 = np.matmul(X.T, X)
term_2 = np.matmul(X.T,y)
beta3 = np.linalg.solve(term_1,term_2)

line_y = beta3[0] + beta3[1] * line_x + beta3[2] * line_x**2

plt.plot(line_x, line_y, 'r')   
fig.legend(handles = (ax.get_children() ), labels = ('Raw Data', 
                                                     'Linear Fit (Matrix)',
                                                     'Linear Fit (Normal)',
                                                     'Quadratic Fit (Normal)'),
           loc = "lower right")


# %% Show plots
plt.text(0.5, 100, 'Justin Kek', size = 20, zorder = 0., color = '#aaaaaa')
plt.show()


# # set the 'index' column as the one containing the temperature values
# df = df.set_index('T/C f/MHz')

# # extract the frequency values (and scale since they are MHz)
# freq = df.columns.values.astype(np.float) * 1e6
# # extract the temperature values
# temp = df.index.values.astype(np.float)

# # extract the main part - the velocity values
# vel = df.to_numpy()
# # calculate the total number of values
# tot_values = len(freq) * len(temp)

# ---

# x1grid, x2grid = np.meshgrid(freq, temp) 
# Xgrid = np.concatenate([x1grid.reshape([tot_values, 1]), 
# 	x2grid.reshape([tot_values, 1])], axis=1) 
# ygrid = vel.reshape([tot_values, 1])

# ---

# from sklearn.linear_model import LinearRegression

# reg = LinearRegression()
# reg.fit(Xgrid, ygrid)

# ---

# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure() 
# ax = fig.add_subplot(111, projection='3d') 
# ax.scatter(Xgrid[:, 0], Xgrid[:, 1], ygrid, marker='x', color='#000000') 
# ax.scatter(Xgrid[:, 0], Xgrid[:, 1], y_lin, marker='o', color='#ff0000')

# ---

# import plotly.graph_objects as go

# fig = go.Figure()
# fig.add_trace(go.Scatter3d(x=Xgrid[:, 0], y=Xgrid[:, 1], z=ygrid[:, 0], mode='markers',
#                                        marker=dict(size=2, color='#000000', symbol='x')))

# fig.add_trace(go.Scatter3d(x=Xgrid[:, 0], y=Xgrid[:, 1], z=y_lin[:, 0], mode='markers',
#                                        marker=dict(size=3, color='#ff0000', symbol='circle')))

# ---

# from sklearn.preprocessing import PolynomialFeatures
# ...
# poly = PolynomialFeatures(degree = 2)
# X_poly = poly.fit_transform(Xgrid)

# print(X_poly.shape)
# print(poly.powers_)
# ---

# reg_poly = LinearRegression()
# reg_poly.fit(X_poly, ygrid)







