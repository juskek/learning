#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:10:22 2020

@author: justinkek
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

#%% IMAGE PROPERTIES
# load in the image
img = mpimg.imread('window.png')

#just extract one channel - technically this is red, but 
#it doesn't matter since they are all equal
# squeeze eliminates 3rd dimension of array (BW image, other channels redundant)
imgBw = np.squeeze(img[:, :, 0])

#get size of image
npy, npx = imgBw.shape

plt.figure() 
plt.imshow(imgBw, cmap=plt.cm.gray) 
plt.axis('off')
#%% 3.1 FOURIER PROCESSING

# FOURIER TRANSFORM OF IMAGE
fim = np.fft.fft2(imgBw)

# PLOT FT
plt.figure() 
# frequency components for (0,0) in the corner by default 
# fftshift shifts it to the centre
plt.imshow(np.fft.fftshift(np.abs(fim)))
#show the colour scale:
plt.colorbar()
#set the colour limits to something so we can see the image better
plt.clim(0, 1e3)

# MAKE SEPARATE COPY FOR SHOWING VERTICAL COMPONENTS
fim2 = fim.copy() 
#set everything in all except the first row to zero
fim2[1:npy, :] = 0 
#set everything in the first row to zero except the first 61 points and the last 60
fim2[0, 61:npx - 60] = 0

img2 = np.real(np.fft.ifft2(fim2))
plt.figure() 
plt.imshow(img2, cmap=plt.cm.gray) 
plt.axis('off')

# MAKE SEPARATE COPY FOR SHOWING HORIZONTAL COMPONENTS
fim3 = fim.copy() 
#set everything in all except the first row to zero
fim3[:, 1:npx] = 0 
#set everything in the first row to zero except the first 61 points and the last 60
fim3[61:npy - 60, 0] = 0

img3 = np.real(np.fft.ifft2(fim3))
plt.figure() 
plt.imshow(img3, cmap=plt.cm.gray) 
plt.axis('off')

#%% 3.2 EDGE DETECTION

diffx = np.diff(imgBw, axis=1) 
diffy = np.diff(imgBw, axis=0)

# reduce size of each differential result 
# to ...
diffx = diffx[0:npy - 1,:]
diffy = diffy[:,0:npx - 1]

# combine diffx and diff using sqrt(diffx^2) + (diffy^2))
edgeIm = np.sqrt(np.power(diffx,2)+np.power(diffy,2))

# show edges
plt.figure() 
plt.imshow(edgeIm, cmap=plt.cm.gray) 
plt.axis('off')
plt.colorbar()

#%% 3.3 THRESHOLDING

# threshold too
    # low, too much noise
    # high, too little detail

t = 0.1
edgeThresh = (edgeIm > t).astype('int')

plt.figure() 
plt.imshow(edgeThresh, cmap=plt.cm.gray) 
plt.axis('off')
plt.colorbar()
