

#Created on Tue Feb 26 15:04:24 2019

#@author: preranaparthasarathy

import numpy as np
import pandas as pd
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn import neighbors
from sklearn import naive_bayes
import time
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import random
from bayes_opt import BayesianOptimization
#import iris dataset
#iris= datasets.load_iris()
#X=iris.data[:,:2]
#Y=iris.target
#split dataset
#X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

#import income dataset

def read_data():
    train = pd.read_csv('income.train.csv', header = None)
    test = pd.read_csv('income.test.csv',header = None)
    #concat data
    dataset=pd.concat([train,test],keys=[0,1])
    #columns = ['age','workclass','education','marital-status','occupation','race','sex','hours-per-week','native-country','income']
    return (dataset,train,test)        


def separate(dataset):
    train= dataset.xs(0)
    test=dataset.xs(1)
    return train,test


def encode_y(train_y,test_y):
    labelencoder_y=LabelEncoder()
    train_y=labelencoder_y.fit_transform(train_y)
    test_y=labelencoder_y.fit_transform(test_y)
    train_y[train_y==0]=-1
    test_y[test_y==0]=-1
    return train_y,test_y


(income,train_income,test_income)=read_data()
#only the prediction column
income_y=income[[9]]
Y_train,Y_test = separate(income_y)
#drop the y from x set
income=income.drop([9], axis = 1)
encoded_income = pd.get_dummies(income,columns=[1,2,3,4,5,6,8])
Y_train,Y_test = encode_y(Y_train,Y_test)
X_train,X_test = separate(encoded_income)
X_train = X_train.iloc[:,:].values
X_test = X_test.iloc[:,:].values

list_rand=[]
while len(list_rand)<5:
    r=random.randint(1,5)
    if r not in list_rand: 
        list_rand.append(r)  

#SVM
def testing_svm():
    model=svm.SVC(kernel="linear")
    model.fit(X_train,Y_train)
    predictions=model.predict(X_test)
    correct_classifications = 0
    for i in range(len(Y_test)):
        if predictions[i] == Y_test[i]:
            correct_classifications +=1
    accuracy= 100*correct_classifications/len(Y_test)
    return accuracy
#creating the model for SVM
def run_svm():
    start_svm= time.time()
    accuracy_test_svm=testing_svm()
    end_svm=time.time()
    print(">SVM Accuracy")
    print("{} %".format(accuracy_test_svm))
    print(">SVM Time(s)")
    print(end_svm-start_svm)
    print(" ")

#decision tree
def testing_decision_tree(model=None):
    classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
    classifier.fit(X_train,Y_train)
    predictions=classifier.predict(X_test)
    correct_classifications=0
    for i in range(len(Y_test)):
        if predictions[i] ==Y_test[i]:
            correct_classifications +=1
    accuracy_test_decision_tree = 100*correct_classifications/len(Y_test)
    return accuracy_test_decision_tree
#creating model DT
def run_dt():
    start_dt=time.time()
    accuracy_test_DT=testing_decision_tree()
    end_dt=time.time()
    print(">Decision Tree Accuracy")
    print("{} %".format(accuracy_test_DT))
    print(">Decsion Tree Time(s) ")
    print(end_dt-start_dt)
    print(" ")
    
    

#logistic Regression
def logisticReg():
    model_lm=linear_model.LogisticRegression()
    model_lm.fit(X_train,Y_train)
    predictions=model_lm.predict(X_test)
    correct_classifications=0
    for i in range(len(Y_test)):
        if predictions[i] ==Y_test[i]:
            correct_classifications +=1
    accuracy = 100*correct_classifications/len(Y_test)
    return accuracy
def run_lm():
    start_lm=time.time()
    accuracy_lm=logisticReg()
    end_lm=time.time()
    print(">Logostic Regression Accuracy")
    print("{} %".format(accuracy_lm))
    print(">Logistic Regresion Time(s)")
    print(end_lm-start_lm)
    print(" ")

#KNN
def knn():
    model_knn=neighbors.KNeighborsClassifier()
    model_knn.fit(X_train,Y_train)
    predictions=model_knn.predict(X_test)
    correct_classifications=0
    for i in range(len(Y_test)):
        if predictions[i] ==Y_test[i]:
            correct_classifications +=1
    accuracy = 100*correct_classifications/len(Y_test)
    return accuracy

def run_knn():
    start_knn=time.time()
    accuracy_knn=knn()
    end_knn=time.time()
    print(">KNN Accuracy")
    print("{} %".format(accuracy_knn))
    print(">KNN Time(s)")
    print(end_knn-start_knn)
    print(" ")

#NB
def nb():
    model_nb=naive_bayes.GaussianNB()
    model_nb.fit(X_train,Y_train)
    predictions=model_nb.predict(X_test)
    correct_classifications=0
    for i in range(len(Y_test)):
        if predictions[i] ==Y_test[i]:
            correct_classifications +=1
    accuracy = 100*correct_classifications/len(Y_test)
    return accuracy

def run_nb():
    start_nb=time.time()
    accuracy_nb=nb()
    end_nb=time.time()
    print(">Naive Bayes Accuracy")
    print("{} %".format(accuracy_nb))
    print(">Naive Bayes Time(s)")
    print(end_nb-start_nb)
    print(" ")
    
    

for j in range(len(list_rand)):
    if list_rand[j]==1:
        run_svm()
    elif list_rand[j]==2:
        run_dt()
    elif list_rand[j]==3:
        run_lm()
    elif list_rand[j]==4:
        run_knn()
    elif list_rand[j]==5:
        run_nb()