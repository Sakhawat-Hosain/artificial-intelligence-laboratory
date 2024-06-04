# -*- coding: utf-8 -*-
"""Assignment_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_m6n2XQ9SH_EqOTciPOIu72UEdWctVDo
"""

import pandas as pd
import numpy as np
import math

iris_data = pd.read_csv("/content/iris.csv")

X = iris_data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = iris_data['variety.class'].values


random_index = np.random.permutation(len(X))  #Shuffling
X = X[random_index]
y = y[random_index]


split_index = int(len(X) * 0.8) #split dataset

X_train, X_test = [], []
y_train, y_test = [], []

for eachdata in range(len(X)):
    if eachdata < split_index:
        X_train.append(X[eachdata])
        y_train.append(y[eachdata])
    else:
        X_test.append(X[eachdata])
        y_test.append(y[eachdata])

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)


k = 5
M_prime = len(X_test)

y_test_predicted = np.zeros(M_prime) #Initialize numpy arr

for i in range(M_prime):
    x_test = X_test[i]  #Current test case
    M = len(X_train)
    D = np.zeros(M)  #Initialize arr to store distances

    for j in range(M):  # Calculate Euclidean distances
        D[j] = np.sqrt(np.sum((x_test - X_train[j])**2))

    sorted_index = np.argsort(D)  #Sort distance index
    min_dist_index = sorted_index[ : k]  #First k index
    y_neighbor = y_train[min_dist_index] #k nearest neighbors
    predicted_label = np.bincount(y_neighbor).argmax() #Predict the label among neighbors
    y_test_predicted[i] = predicted_label


correct_predictions = (y_test == y_test_predicted) #Calculate correct prediction
accuracy = np.mean(correct_predictions) * 100  # Calculate percentage accuracy


print(f"Accuracy: {accuracy :.2f}") #print accuracy