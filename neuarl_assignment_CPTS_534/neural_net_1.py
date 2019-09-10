# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:57:06 2019

@author: Kaushik Acharya
"""



# Assignment 1

import pandas as pd
import numpy as np
import statsmodels.api as sm
#import sys
#from sklearn.linear_model import LinearRegression

#sys.stdout = open("C:/Users/Kaushik Acharya/Documents/Python Scripts/i_code_in_python/neuarl_assignment_CPTS_534/output_neural_1.txt")

cereal = pd.read_csv("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/Cereals.csv")
#print(cereal.shape)

cereal = cereal.dropna()
#print(cereal.shape)

sugars = cereal['Sugars'].values
fibers = cereal['Fiber'].values
rating = cereal['Rating'].values


#sugars = sugars[~np.isnan(sugars)]
#fibers = fibers[~np.isnan(fibers)]
#rating = rating[~np.isnan(rating)]

#sugars = np.delete(sugars,57)
#rating = np.delete(rating, 57)
#fibers = np.delete(fibers, 57)


#cereal = cereal.drop(cereal.index[57])
#sugars2 = sm.add_constant(sugars)
X = cereal[['Sugars','Fiber']]
y = cereal['Rating']


X = sm.add_constant(X)
reg = sm.OLS(y,X).fit()
#reg_pred = reg.get_prediction(reg)
#print(reg_pred.summary_frame())


print("###################### Nutritional Rating Vs Sugar and Fiber ########################")
print("The Co-efficient of determination(R^2): ", reg.rsquared)
print("The bias: ", reg.params[0])
print("The Slope for sugar: ", reg.params[1])
print("The Slope for fiber: ", reg.params[2])
print("The Sum of Squares Residuals: ",reg.ssr)
print("The Standard Error of Estimation: ",np.sqrt(reg.scale))

#print(reg.ssr,reg.uncentered_tss, reg.centered_tss)


# Protein
proteins = cereal['Protein'].values

X1 = cereal[['Sugars','Fiber','Protein']]
y1 = cereal['Rating']


X1 = sm.add_constant(X1)
reg1 = sm.OLS(y1,X1).fit()

print("###################### Nutritional Rating Vs Sugar, Fiber and Protein ########################")
print("The Co-efficient of determination(R^2): ", reg1.rsquared)
print("The bias: ", reg1.params[0])
print("The Slope for sugar: ", reg1.params[1])
print("The Slope for fiber: ", reg1.params[2])
print("The Slope for protein: ", reg1.params[3])
print("The Standard Error of Estimation: ",np.sqrt(reg1.scale))

# with fat
X2 = cereal[['Sugars','Fiber','Fat']]
y2 = cereal['Rating']


X2 = sm.add_constant(X2)
reg2 = sm.OLS(y2,X2).fit()

print("###################### Nutritional Rating Vs Sugar, Fiber and Fat ########################")
print("The Co-efficient of determination(R^2): ", reg2.rsquared)
print("The bias: ", reg2.params[0])
print("The Slope for sugar: ", reg2.params[1])
print("The Slope for fiber: ", reg2.params[2])
print("The Slope for fat: ", reg2.params[3])
print("The Standard Error of Estimation: ",np.sqrt(reg2.scale))


# with sodium
X3 = cereal[['Sugars','Fiber','Sodium']]
y3 = cereal['Rating']


X3 = sm.add_constant(X3)
reg3 = sm.OLS(y3,X3).fit()

print("###################### Nutritional Rating Vs Sugar, Fiber and Sodium ########################")
print("The Co-efficient of determination(R^2): ", reg3.rsquared)
print("The bias: ", reg3.params[0])
print("The Slope for sugar: ", reg3.params[1])
print("The Slope for fiber: ", reg3.params[2])
print("The Slope for sodium: ", reg3.params[3])
print("The Standard Error of Estimation: ",np.sqrt(reg3.scale))

