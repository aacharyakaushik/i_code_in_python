import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier,AdaBoostClassifier
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

curr_dir = os.getcwd()
os.chdir(curr_dir) 

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

data = pd.concat([x_train, x_test, x_dev])
data_ohe = pd.get_dummies(data)
x_train_ohe = data_ohe[:len(x_train)]
x_test_ohe = data_ohe[len(x_train):len(x_test) + len(x_train)]
x_dev_ohe = data_ohe[len(x_test) + len(x_train):]

y_train_ohe = y_train.replace([' <=50K', ' >50K'], [-1, 1])
y_test_ohe = y_test.replace([' <=50K', ' >50K'], [-1, 1])
y_dev_ohe = y_dev.replace([' <=50K', ' >50K'], [-1, 1])


def Bagging(max_depth,n_estimators):
    global x_train_ohe,y_train_ohe,x_dev_ohe,y_dev_ohe
    Bag =  BaggingClassifier(DecisionTreeClassifier(max_depth=int(max_depth)), n_estimators=int(n_estimators))
    Bag.fit(x_train_ohe,y_train_ohe)
    return Bag.score(x_dev_ohe,y_dev_ohe)

def Boosting(max_depth,n_estimators):
    global x_train_ohe,y_train_ohe,x_dev_ohe,y_dev_ohe
    Boost = AdaBoostClassifier(DecisionTreeClassifier(max_depth=int(max_depth)), n_estimators=int(n_estimators))
    Boost.fit(x_train_ohe,y_train_ohe)
    return Boost.score(x_dev_ohe,y_dev_ohe)

flag = 0
for objective in [Bagging,Boosting]:
    Bayesian = BayesianOptimization(objective, {'max_depth': (1, 10), 'n_estimators': (10, 100)})
    Bayesian.maximize(init_points=2, n_iter=48, acq='ei')
    plt.plot(range(50),Bayesian.Y)
    plt.xlabel('iteration')
    plt.ylabel('Accuracy')
    if flag == 0:
        plt.title('Bagging')
    else:
        plt.title('Boosting')
    plt.show()
    #plt.savefig(str(flag)+'.png')
    flag = flag+1
