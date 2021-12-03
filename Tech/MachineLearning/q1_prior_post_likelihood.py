#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:32:39 2020

@author: justinkek
"""

# %% SETUP

import numpy as np
import matplotlib.pyplot as plt

# set random seed to zero; same numbers everytime code is run
np.random.seed(5)

# %% GAUSSIAN FUNCTION

def gaussian(x, mu, sig):
    expo = np.exp(-((x - mu)/sig)**2/2)
    return (1/(np.sqrt(2*np.pi)*sig)) * expo
            
print(gaussian(1, 0, 0.5))

# %% DEFINE 2 DISTRIBUTIONS FOR STATE OF NATURES

x = np.linspace(-10, 20, 200)
p_x_w1 = gaussian(x, 2, 1.5) + gaussian(x, 7, 0.5)
p_x_w2 = gaussian(x, 8, 2.5) + gaussian(x, 3.5, 1)

# %% NORMALISE SO THEY INTEGRATE TO 1

p_x_w1_norm = p_x_w1/np.trapz(p_x_w1, x)
p_x_w2_norm = p_x_w2/np.trapz(p_x_w2, x)

# %% PLOT DISTRIBUTIONS OF LIKELIHOOD
fig, ax = plt.subplots()
plt.plot(x, p_x_w1)
plt.plot(x, p_x_w2)
plt.plot(x, p_x_w1_norm)
plt.plot(x, p_x_w2_norm)
fig.legend(handles = (ax.get_children() ), labels = ('P(x|w1)', 'P(x|w2)',
                                                     'P(x|w1_norm)', 
                                                     'P(x|w2_norm)'), 
           loc = "upper right")
plt.title("Probability Distributions")
ax.set_xlabel("x-values")
ax.set_ylabel("Probability")

# %% CALCULATE POSTERIOR

# PRIOR
p_w1 = 0.9
p_w2 = 0.1

# EVIDENCE
p_x = p_w1 * p_x_w1_norm + p_w2 * p_x_w2_norm

# POSTERIOR: BAYES FORMULA
# element wise division and multiplication
p_w1_x = np.divide((np.multiply(p_w1, p_x_w1_norm)), p_x)
p_w2_x = np.divide((np.multiply(p_w2, p_x_w2_norm)), p_x)

# PLOT
fig, ax = plt.subplots()
plt.plot(x, p_w1_x)
plt.plot(x, p_w2_x)
fig.legend(handles = (ax.get_children() ), labels = ('P(w1|x)', 'P(w2|x)'), loc = "upper right")
plt.title("Probability Distributions")
ax.set_xlabel("x-values")
ax.set_ylabel("Probability")
