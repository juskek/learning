#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:11:25 2020

@author: justinkek
"""

# %% 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%

df_raw = pd.read_csv('tensile_strength.csv')
df_raw.columns = ['temp', 'uts']

# %% SCALE

t_mean = np.mean(df_raw['temp']) 
t_std = np.std(df_raw['temp'])

s_mean = np.mean(df_raw['uts']) 
s_std = np.std(df_raw['uts'])

t_scaled = (df_raw['temp'] - t_mean) / t_std
s_scaled = (df_raw['uts'] - s_mean) / s_std

df_scaled = np.array([t_scaled, s_scaled])



fig, ax = plt.subplots(1,2) 
ax[0].hist(df_raw['uts'], bins = 30) xw
ax[1].hist(s_scaled, bins = 30)

ax[0].set_title("Histogram of Stress")
ax[1].set_title("Histogram of Normalized Stress")

plt.subplots_adjust(wspace = 10)
fig.tight_layout()
plt.show()

# %% SAVE SCALING VALUES FOR OTHER DATASET

scArray = np.array([[t_mean, s_mean],[t_std, s_std]]) 
np.savetxt('scaleParams.txt',scArray)

# download it from the Colab interface:
from google.colab import files 
files.download('scaleParams.txt')

# %%
plt.tight_layout()
plt.show()


# ---
# loadedScales = np.loadtxt('scaleParams.txt')
# ---
# #Ygrid is defined as the same as Xgrid, except it has 1 
# #at the beginning - this therefore adds a column of ones to the left
# Ygrid = np.concatenate([np.ones([npx * npy,1]), Xgrid],axis=1) 

# #calculate each of the five functions as before
# g1 = np.matmul(a1, Ygrid.T) 
# g2 = np.matmul(a2, Ygrid.T) 
# g3 = np.matmul(a3, Ygrid.T) 
# g4 = np.matmul(a4, Ygrid.T) 
# g5 = np.matmul(a5, Ygrid.T)
# #combine all five functions together
# gconc = np.concatenate([g1, g2, g3, g4, g5])

# #define an array which will ultimately contain all of the class numbers
# omega = np.zeros([1, npx * npy]) 
# for i in range(5):
# 	#define an array which is one if it belongs to class i, 
# 	#and zero otherwise - set it to ones throughout to start with:
# 	omhere = np.ones([1, npx*npy]) 
# 	
# 	#loop through all of the classes
# 	for j in range(5):
# 		#if there is another class with a higher value, set it to zero:
# 		omhere[0,gconc[i,:]<gconc[j,:]] = 0

# 	#set values in omega which correspond to omhere == 1 to that 
# 	#particular category number (i + 1 - remember python is zero indexed). 
# 	omega[omhere == 1] = i + 1
# #put back onto 2D grid so it can easily be plotted
# omega = np.reshape(omega, [npx, npy]) 