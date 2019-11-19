# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:04:39 2019

@author: Kaushik Acharya
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
from collections import Counter
from sklearn.metrics import confusion_matrix
import warnings


warnings.filterwarnings("ignore")

no_name = pd.read_csv("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/test-set_copy - Copy.csv")
print(no_name.shape)

[rows,cols]= no_name.shape
print("rows:",rows,"cols:",cols)


for i in range(rows):
    if no_name['predicted'][i] <= 3:
        no_name['predicted'][i] = 1
    else:
        no_name['predicted'][i] = 5

no_name['predicted'] = no_name['predicted'].astype(int)

# print(no_name.head())

bin = [1,5]

print(Counter(no_name['predicted']))

# Separting the accuracies of 1's and 5's
for p in bin:
    correct = 0
    total = 0

    for i in range(rows):
        if ((no_name.iloc[i]['predicted']== p) and (no_name.iloc[i]['actual']== p)):
            correct +=1
    total = (no_name['actual']==p).sum()

    accuracy = (correct/total)*100
    print("############# ",p," #############")
    print("Number of Instaces of",p,":",total)
    print("predicted correctly", p,":", correct)
    print("Accuracy :", accuracy)

# creating confusion matrix

correct = 0
for i in range(rows):
    if (no_name.iloc[i]['predicted']== no_name.iloc[i]['actual']):
        correct +=1
accuracy = (correct/ rows)*100
print("############# TOTAL #############")
print("Total Instances :", rows)
print("Instances classified properly :", correct)
print("Accuracy :",accuracy)

# confusion matrix
cf = confusion_matrix(no_name['actual'],no_name['predicted'], labels=[1,5])

print("########### CONFUSION MATRIX ###########")
print(np.transpose(cf))