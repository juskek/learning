#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:16:51 2020

@author: justinkek
"""

# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% DEFINE 5 LDFs

# point classified to class which has largest g value 

# %%
# LDF surface requires meshgrid
# 1. no of nodes for meshgrid
npx = 200
npy = 200

# 2. define 1D vectors 
x1 = np.linspace(0, 1, npx)
x2 = np.linspace(0, 1, npy)

# 3. generate 2D arrays
x1grid, x2grid = np.meshgrid(x1, x2)

# 4. create 3D grid
Xgrid = np.array([x1grid, x2grid])

# 5. revert back to 1D vector for generating y(x) values!
Xgrid = Xgrid.reshape([2, npx * npy])

# %%

# Append Xgrid vector to vector of 1s for bias
Ygrid = np.concatenate([np.ones([npx * npy, 1]), Xgrid.T], axis = 1)

# weighting terms (bias, x1, x2)
a1 = np.array([1.3, -1, -3])
a2 = np.array([-2, 1, 2])
a3 = np.array([0.3, 0.1, -0.1])
a4 = np.array([0, -1, 1])
a5 = np.array([-0.2, 1.5, -1])

# define LDFs g = aT.y
# 1D vectors
g1 = np.matmul(a1 , Ygrid .T)
g2 = np.matmul(a2 , Ygrid .T)
g3 = np.matmul(a3 , Ygrid .T)
g4 = np.matmul(a4 , Ygrid .T)
g5 = np.matmul(a5 , Ygrid .T)

#combine all five functions together to form 2D array 5 x 40000
gconc = np.concatenate([ [g1] , [g2] , [g3] , [g4] , [g5] ])

#define an array of 0s which will ultimately contain all of the class numbers
omega = np.zeros([1 , npx * npy ])

# %%


# 5 LDFs,
# for LDF i,
for i in range (5):
    # assume all points in space belong to this class (LDF i = 1 at this point)
    
    omhere = np.ones([1 , npx * npy ])
    
    # comparing it with all the other classes,
    for j in range (5):
        #if there is another class with a higher value , set it to zero :
            # syntax here: comparing first row of values (0),
            # element-wise conditional operation, if true, it doesnt belong
            # in that category
        omhere[0 , gconc[i, :] < gconc[j, :]] = 0
        
    #set values in omega which correspond to omhere == 1 to that
    #particular category number (1 to 5)
    
    omega[omhere == 1] = i + 1
    
# #put back onto 2D grid so it can easily be plotted
omega = np.reshape(omega , [npx , npy ])

# %% PLOT
fig, ax = plt.subplots()
CS = plt.contourf(x1, x2, omega, 200)
cbar = fig.colorbar(CS)

ax.set_xlabel("x1")
ax.set_ylabel("x2")


# Check https://stackoverflow.com/questions/14777066/matplotlib-discrete-colorbar for discrete color bar

# %% HIGHER ORDER FUNCTIONS

x1x2 = np.multiply(Xgrid.T[:, 0], Xgrid.T[:, 1])

Ygrid = np.concatenate([np.ones([npx * npy, 1]), Xgrid.T, np.array([x1x2]).T], axis = 1)

a1 = np.array([1.3, -1, -3, -10])
a2 = np.array([-1, 1, 3, -1])
a3 = np.array([0.4, -0.1, -0.1, 3])
a4 = np.array([0.5, -1, 1, -0.1])
a5 = np.array([-0.2, 1.5, -1, 0.4])

g1 = np.matmul(a1 , Ygrid .T)
g2 = np.matmul(a2 , Ygrid .T)
g3 = np.matmul(a3 , Ygrid .T)
g4 = np.matmul(a4 , Ygrid .T)
g5 = np.matmul(a5 , Ygrid .T)

# combine all five functions together
gconc = np.concatenate([ [g1] , [g2] , [g3] , [g4] , [g5] ])

#define an array which will ultimately contain all of the class numbers
omega = np.zeros([1 , npx * npy ])


# %%

for i in range (5):
    #define an array which is one if it belongs to class i ,
    #and zero otherwise − set it to ones throughout to start with :
    
    omhere = np.ones([1 , npx * npy ])
    #loop through all of the classes
    
    for j in range (5):
        #if there is another class with a higher value , set it to zero :
        omhere[0 , gconc[i, :] < gconc[j, :]] = 0
        
    #set values in omega which correspond to omhere == 1 to that
    #particular category number ( i + 1 − remember python is zero indexed ).
    
    omega[ omhere == 1] = i + 1
    
#put back onto 2D grid so it can easily be plotted
omega = np.reshape(omega , [npx , npy ])

# %%


fig, ax = plt.subplots()
CS = plt.contourf(x1, x2, omega, 200)
cbar = fig.colorbar(CS)

ax.set_xlabel("x1")
ax.set_ylabel("x2")

plt.show()