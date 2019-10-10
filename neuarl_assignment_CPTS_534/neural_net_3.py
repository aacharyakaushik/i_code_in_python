# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:04:39 2019

@author: Kaushik Acharya
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import math

glass = pd.read_csv("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/glass data short.csv", header = None)
#print(glass.shape)

[rows,cols]= glass.shape
print("rows:",rows,"cols:",cols)

inputs = glass.iloc[:,0:9]
minputs = 9
labels = glass.iloc[:,9]
V = np.ones((rows,10))
V[:,1:10] = inputs
A = np.dot(V.T, V) 
b = np.dot(V.T, labels)
w = np.linalg.solve(A,b)
print("############# w #############")
print(w)


ybar = sum(labels)/rows
dely = labels - ybar
SST = np.dot(dely.T, dely) 
print("SST:", SST)   
fit = np.dot(V,w)
resid = labels - fit
SSE = np.dot(resid.T, resid)
print("SSE:", SSE)
MSE = SSE/ (rows-minputs-1)
print("MSE:", MSE)
SSR = SST-SSE
print("SSR:",SSR)
rsq = SSR/SST
see = math.sqrt(MSE)
print("rsq:",rsq,"see:",see)

n1tot= n2tot = n6tot = 0
n1corect = n2corect = n6corect = 0
n1assign2 = n2assign1 = n6assign1 = 0


for i in range(rows):
    mass = labels[i]
    if(mass == 1):
        n1tot = n1tot+1
    if(mass == 2):
        n2tot = n2tot+1
    if(mass == 6):
        n6tot = n6tot+1
    bin = 2
    if(fit[i] < 1.5):
        bin = 1
    if(fit[i] > 4):
        bin = 6
    if(bin == 1 and mass == 1):
        n1corect = n1corect+1
    if(bin == 2 and mass == 1):
        n1assign2 = n1assign2+1
    if(bin == 2 and mass == 2):
        n2corect = n2corect+1
    if(bin == 1 and mass == 2):
        n2assign1 = n2assign1+1
    if(bin == 6 and mass == 6):
        n6corect = n6corect+1
    if(bin == 1 and mass == 6):
        n6assign1 = n6assign1+1
        
        
confMat = np.zeros((3,3))
confMat[0,0] = n1corect
confMat[1,1] = n2corect
confMat[2,2] = n6corect
confMat[1,0] = n1assign2
confMat[2,0] = n1tot - n1corect-n1assign2
confMat[0,1] = n2assign1
confMat[2,1] = n2tot-n2corect-n2assign1
confMat[0,2] = n6assign1
confMat[1,2] = n6tot-n6corect-n6assign1
print("############## Confusion Matrix ################")
print(confMat)
