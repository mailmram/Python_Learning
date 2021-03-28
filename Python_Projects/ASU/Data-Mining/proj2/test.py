#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:13:33 2021

@author: ram
"""
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pickle

df = pd.read_csv("test.csv", header=None)
df = df[df.columns[range(24)]]
#print(df)

clf = pickle.load(open('model.pickle', 'rb'))
result = clf.predict(df)
resuldf = pd.DataFrame(result)
resuldf.to_csv("Result.csv",index = False, header=None)