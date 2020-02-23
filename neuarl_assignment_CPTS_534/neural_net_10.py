# -*- coding: utf-8 -*-
"""
Created on Mon Nov  18 15:04:39 2019

@author: Kaushik Acharya
"""

import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


glass = pd.read_csv("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/glass data short.csv", header = None)
# print(glass.shape)



inputs = glass.iloc[:,0:9]

[rows,cols]= inputs.shape
print("rows:",rows,"cols:",cols)

# inputdf = pd.DataFrame(data = input)

###################### Co-Variance Calculation ########################
sig = inputs.cov()

# sig = np.cov(inputs)
# print("############## covariance matrix #################")
# print(sig)

D, V = np.linalg.eig(sig)
# # print("################ V #############")
# print(V)
print("################ D (in descending order) - CoVariance #############")
# print(D)



# print("################ D #############")
# diag = np.diagonal(D)
diag = sorted(D,reverse=True )
print(diag)

pov = np.cumsum(diag)/np.sum(diag)
# print(pov)

plt.plot(pov)
plt.title('PoV : PCs of covariance matrix')
plt.savefig("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/Assignment_10_KKR_11632490/Co-Variance.png")
plt.close()

# plt.plot(D)
# plt.title('Eigen Values of Covariance matrix')
# plt.savefig("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/Assignment_10_KKR_11632490/Co-Variance_Eigen.png")
# plt.close()


########################## Co-relation matrix #########################

sig_cr = inputs.corr()

D_cr, V_cr = np.linalg.eig(sig_cr)
diag_cr = sorted(D_cr, reverse=True)
pov_cr = np.cumsum(diag_cr)/np.sum(diag_cr)

print("################ D (in descending order) - CoRelation #############")
print(diag_cr)


plt.plot(pov_cr)
plt.title('PoV : PCs of correlation matrix')
plt.savefig("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/Assignment_10_KKR_11632490/Co-Relation.png")
plt.close()

# plt.plot(D_cr)
# plt.title('Eigen Values of Correlation matrix')
# plt.savefig("C:/Users/Kaushik Acharya/Documents/3rd sem/Neural Network/Assignment/Assignment_10_KKR_11632490/Co-Relation_Eigen.png")
# plt.close()