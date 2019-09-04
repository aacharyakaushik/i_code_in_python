#niraries required
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading data
from keras.datasets import mnist

(train_x, train_y), (test_x, test_y) = mnist.load_data()
#training data frame using Keras
train_df = keras.utils.to_categorical(train_y, num_classes=10)
#test data frame from Keras
test_df = keras.utils.to_categorical(test_y, num_classes=10)
#reshaping the train data
train_x = train_x.reshape(len(train_x), 28, 28, 1)
#reshaping the test data
= test_x.reshape(len(test_x), 28, 28, 1)
model = Sequential()
model.add(Convolution2D(32,3,data_format='channels_last',activation='relu', input_shape=(28,28,1)))
