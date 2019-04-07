import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier,AdaBoostClassifier
import matplotlib.pyplot as plt

curr_dir = os.getcwd()
os.chdir(curr_dir) 

#standarizing the data
column_names =  ["age", "workclass", "education", "relationship", "profession", "race", "gender", "workhours",
                 "nationality", "income"]
data_train = pd.read_csv('income.train.csv', names = column_names)
data_test = pd.read_csv('income.test.csv',  names = column_names)
data_dev= pd.read_csv('income.dev.csv',  names = column_names)

numerical_col = ["age", "workhours"]
scaler = StandardScaler()
data_train[numerical_col] = scaler.fit_transform(data_train[numerical_col])
data_test[numerical_col] = scaler.transform(data_test[numerical_col])
data_dev[numerical_col] = scaler.transform(data_dev[numerical_col])

#split data
#training data
y_train = data_train["income"]
x_train = data_train.drop("income",axis=1)

#test data
y_test = data_test["income"]
x_test = data_test.drop("income",axis=1)

#dev data
y_dev = data_dev["income"]
x_dev = data_dev.drop("income",axis=1)

#one hot encoding for binary conversion
data = pd.concat([x_train, x_test, x_dev])
data_ohe = pd.get_dummies(data)
x_train_ohe = data_ohe[:len(x_train)]
x_test_ohe = data_ohe[len(x_train):len(x_test) + len(x_train)]
x_dev_ohe = data_ohe[len(x_test) + len(x_train):]

y_train_ohe = y_train.replace([' <=50K', ' >50K'], [-1, 1])
y_test_ohe = y_test.replace([' <=50K', ' >50K'], [-1, 1])
y_dev_ohe = y_dev.replace([' <=50K', ' >50K'], [-1, 1])

#Bagging
depth=[1,2,3,5,10]
trees=[10,20,40,60,80,100]

#n=1
for x in depth:
    train_bag=[]
    test_bag=[]
    dev_bag=[]
    for y in trees:
        bagging = BaggingClassifier(DecisionTreeClassifier(max_depth=x),max_samples=0.5,max_features=1.0,n_estimators=y)
        bagging = bagging.fit(x_train_ohe,y_train_ohe)
        train_bag_score = bagging.score(x_train_ohe,y_train_ohe)
        test_bag_score = bagging.score(x_test_ohe,y_test_ohe)
        dev_bag_score = bagging.score(x_dev_ohe,y_dev_ohe)
        train_bag.append(train_bag_score)
        test_bag.append(test_bag_score)
        dev_bag.append(dev_bag_score)
        
        print("Bagging results")
        print("Depth = "+ str(x)+"\tNumber of trees="+str(y))
        print("Accuracy")
        print("Train ="+str(train_bag_score))
        print("Test ="+str(test_bag_score))
        print("Dev ="+str(dev_bag_score))
        
    plt.plot(trees, train_bag, color='orange', label='Train')
    plt.plot(trees, test_bag, color='black', label='Test')
    plt.plot(trees, dev_bag, color='red', label='Dev')
    plt.ylabel("Accuracy of Bagging")
    plt.xlabel("Depth")
    plt.title("Accuracy vs Depth")
    plt.show()

#Boosting
boost_depth = [1,2,3]
boost_iterations = [10,20,40,60,80]

#n=1
for p in boost_depth:
    train_boost = []
    test_boost = []
    dev_boost = []
    for q in boost_iterations:
        ada_boost = AdaBoostClassifier(DecisionTreeClassifier(max_depth=p),n_estimators=q,learning_rate=1)
        ada_boost = ada_boost.fit(x_train_ohe,y_train_ohe)
        train_boost_score = ada_boost.score(x_train_ohe,y_train_ohe)
        test_boost_score = ada_boost.score(x_test_ohe,y_test_ohe)
        dev_boost_score = ada_boost.score(x_dev_ohe,y_dev_ohe)
        train_boost.append(train_boost_score)
        test_boost.append(test_boost_score)
        dev_boost.append(dev_boost_score)
        
        print("Boosting results")
        print("Depth = "+ str(p)+"\tIterations="+str(q))
        print("Accuracy")
        print("Train ="+str(train_boost_score))
        print("Test ="+str(test_boost_score))
        print("Dev ="+str(dev_boost_score))

    plt.plot(boost_iterations, train_boost, color='orange', label='Train')
    plt.plot(boost_iterations, test_boost, color='black', label='Test')
    plt.plot(boost_iterations, dev_boost, color='red', label='Dev')
    plt.ylabel("Accuracy of Boosting")
    plt.xlabel("iterations")
    plt.title("Accuracy vs iterations")
    plt.show()
    #plt.savefig(str(n)+'boost.png')
    #n=n+1