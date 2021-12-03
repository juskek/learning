#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:29:35 2020

@author: justinkek
"""


nx = 20
#nx = 40
#nx = 10
r = 10
gridDim = np.linspace(-r, r, nx)

dx = gridDim[1] - gridDim[0]
minx = np.min(gridDim)

X, y = gen_circular_distribution(2000)

Xuse = X[y == 1, :]

Xgrid = (np.round((Xuse[:, 0] - minx) / dx * 0.99)).astype('int')
Ygrid = (np.round((Xuse[:, 1] - minx) / dx * 0.99)).astype('int')
density = np.zeros([nx, nx])

for i in range(len(Xgrid)):
    density[Xgrid[i], Ygrid[i]] += 1

totDen = np.sum(density[:])
density /= totDen * dx * dx

fig, ax = plt.subplots()
plt.contourf(gridDim, gridDim, density.T)

ax.scatter(X[y == 1, 0], X[y == 1, 1], marker='x', s=2)
plt.colorbar()
plt.xlim(-r, r)
plt.ylim(-r, r)
plt.show()