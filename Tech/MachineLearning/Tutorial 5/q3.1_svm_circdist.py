#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:15:00 2020

@author: justinkek
"""

# %% CLASSIFICATION ON CIRCULAR DATASET 
# Dataset cannot be classified by simple LDF
# %% IMPORT PACAKAGES 

# IMPORT ALL FUNCTIONS FROM tool.py
from tools import *

# Import SVM from sklearn
from sklearn.svm import SVC

from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score


import matplotlib.pyplot as plt
import numpy as np

# set random seed to zero; same numbers everytime code is run
np.random.seed(0)

#%% GENERATE CIRCULAR DISTRIBUTION

X, y = gen_circular_distribution(500)

#%% SPLIT TRAINING DATA AND SHUFFLE
n_splits = 5
kf = KFold(n_splits = n_splits, shuffle = True)


#%% FIT RBF SVM

score_c_test = []
score_c_train = []
C_array = np.power(10, np.linspace(-1.5, 1.5, 8))
for C in C_array:
    scores_test = []
    scores_train = []
    
    # K FOLD TRAINING
    for train_index, test_index in kf.split(X):
        X_train = X[train_index]
        y_train = y[train_index]
        X_test = X[test_index]
        y_test = y[test_index]

        # initialise iteration of svm
        svm_eval = SVC(C = C, gamma = 'auto', kernel = 'rbf')
        
        # train svm with X_train and y_train
        svm_eval.fit(X_train, y_train)

        # generate test predictions
        y_pred = svm_eval.predict(X_test)
        
        # check accuracy of test predictions against and store
        accuracy = accuracy_score(y_test, y_pred)
        scores_test.append(accuracy)

        # generate training predictions
        y_pred = svm_eval.predict(X_train)

        # check accuracy of training predictions against and store
        accuracy = accuracy_score(y_train, y_pred)
        scores_train.append(accuracy)
    
    # average test and training scores
    score_c_test.append((sum(scores_test)/len(scores_test)))
    score_c_train.append((sum(scores_train)/len(scores_train)))


#%% GENERATE PREDICTIONS
fig, ax = plt.subplots()
ax.plot(C_array, score_c_test)
ax.plot(C_array, score_c_train)
ax.set_ylim([0, 1])

plt.title("Plot of Accuracy against C-value")
ax.set_xlabel("C-Value")
ax.set_ylabel("Accuracy")

fig.legend(handles = (ax.get_children() ), labels = ('Test Set', 
                                                     'Training Set'), 
           loc = "center right")

# plot shows increasing discrepancy between training and data set with 
# increasing C value (more conformity to bounadries, higher variance)
# decreasing C value (mor wiggle room, lower variance)
# too low C value shows negligible discrepancy between training and test data,
# but low accuracy in both cases (wrong assumption, high bias)
plt.show()