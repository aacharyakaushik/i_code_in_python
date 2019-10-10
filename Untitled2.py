#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


x = np.arange(10)


# In[9]:


y = np.arange(9, -1, -1)


# In[5]:


x


# In[10]:


y


# In[ ]:





# In[32]:


import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

## (1) Data preparation
df=pd.read_csv('C:/Users/Kaushik Acharya/Documents/Python Scripts/i_code_in_python/winequality-white.csv', sep = ';')
df
X = df.values[:, :11]
Y = df.values[:, 11]
print('Data shape:', 'X:', X.shape, 'Y:', Y.shape)

# data normalization
min_vals = np.min(X, axis = 0)
max_vals = np.max(X, axis = 0)
X1 = (X-min_vals)/(max_vals-min_vals)

##(2) Assume a linear mode that y = w0*1 + w_1*x_1 +w_2*x_2+...+ w_11*x_11
def predict(X, w):
    '''
    X: input feature vectors:m*n
    w: weights
    
    return Y_hat
    '''
    # Prediction
    Y_hat = np.zeros((X.shape[0]))
    for idx, x in enumerate(X):          
        y_hat = w[0] + np.dot(w[1:].T, np.c_[x]) # linear model
        Y_hat[idx] = y_hat    
    return Y_hat

## (3) Loss function: L = 1/2 * sum(y_hat_i - y_i)^2
def loss(w, X, Y):
    '''
    w: weights
    X: input feature vectors
    Y: targets
    '''
    Y_hat = predict(X, w)
    loss = 1/2* np.sum(np.square(Y - Y_hat))
    
    return loss

# Optimization: Gradient Descent
def GD(X, Y, lr = 0.001, delta = 0.01, max_iter = 100):
    '''
    X: training data
    Y: training target
    lr: learning rate
    max_iter: the max iterations
    '''
    
    m = len(Y)
    b = np.reshape(Y, [Y.shape[0],1])
    w = np.random.rand(X.shape[1] + 1, 1)
    A = np.c_[np.ones((m, 1)), X]
    gradient = A.T.dot(np.dot(A, w)-b)
    
    loss_hist = np.zeros(max_iter) # history of loss
    w_hist = np.zeros((max_iter, w.shape[0])) # history of weight
    loss_w = 0
    i = 0                  
    while(np.linalg.norm(gradient) > delta) and (i < max_iter):
        w_hist[i,:] = w.T
        loss_w = loss(w, X, Y)
        print(i, 'loss:', loss_w)
        loss_hist[i] = loss_w
        
        w = w - lr*gradient        
        gradient = A.T.dot(np.dot(A, w)-b) # update the gradient using new w
        i = i + 1
        
    w_star = w  
    return w_star, loss_hist, w_hist


# In[90]:


# Optimization: implement the minibatch Gradient Descent approach
def SGD(X, Y, lr = 0.001, batch_size = 32, epoch = 100):
    
    m = len(Y)
    w = np.random.rand(X.shape[1] + 1, 1)
    loss_hist = np.zeros(epoch)
    w_hist = np.zeros((epoch, w.shape[0]))

    #Your code here:
   
    for i in range(5):
        #shuffle the data
        np.random.shuffle(df)
        print(df)
        X = df.values[:, :11]
        print(X)
        Y = df.values[:, 11]
        print(Y)
    
    
    
        
        for b in range(int(m/batch_size)):
        
   

      #  w_hist[i,:] = w.T
       # print(i, loss_hist[i])
        
    #w_star = w  
    #return w_star, loss_hist, w_hist


# In[91]:


s = np.arange(X.shape[0])


# In[92]:


np.random.shuffle(s)


# In[93]:


X[s]


# In[94]:


p = np.arange(Y.shape[0])


# In[95]:


np.random.shuffle(p)


# In[96]:


Y[p]


# In[97]:


prediction = np.dot(X,batch_size)


# In[98]:


prediction = np.dot(X,batch_size)


# In[ ]:




