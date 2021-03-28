#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:13:13 2021

@author: ram
"""

import pandas as pd
from datetime import datetime, date, time, timedelta
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pickle

#df = pd.read_csv("CGMData.csv", usecols=["Date", "Time", "Sensor Glucose (mg/dL)"])
csv_file_list = ["InsulinData.csv"]

list_of_dataframes = []
for filename in csv_file_list:
    list_of_dataframes.append(pd.read_csv(filename, usecols=["Date", "Time", "BWZ Carb Input (grams)"]))
df1 = pd.concat(list_of_dataframes, ignore_index=True)


df1['DT'] = df1['Date'] + ' ' +df1['Time']
df1['DT'] =pd.to_datetime(df1['DT'])
df2 = pd.read_csv("Insulin_patient2.csv", usecols=["Date", "Time", "BWZ Carb Input (grams)"])

#df['DT'] = df['Date'] + ' ' +df['Time']
#df['DT'] =pd.to_datetime(df['DT'])
tm = df1[df1["BWZ Carb Input (grams)"].notna()]
tm = df1[df1["BWZ Carb Input (grams)"] > 0]
#tm['DT'] = tm['Date'] + ' ' +tm['Time']
#tm['DT'] =pd.to_datetime(tm['DT'])
tm['hrs'] = tm['DT'][::-1].diff().astype('timedelta64[h]')
tm = tm[tm['hrs'] >=2]
tm = tm.reset_index()

tm1 = df2[df2["BWZ Carb Input (grams)"].notna()]
tm1 = df2[df2["BWZ Carb Input (grams)"] > 0]
tm1['DT'] = tm1['Date'] + ' ' +tm1['Time']
tm1['DT'] =pd.to_datetime(tm1['DT'])
tm1['hrs'] = tm1['DT'][::-1].diff().astype('timedelta64[h]')
tm1 = tm1[tm1['hrs'] >=2]
tm1 = tm1.reset_index()



csv_file_list = ["CGMData.csv"]
list_of_dataframes = []
for filename in csv_file_list:
    list_of_dataframes.append(pd.read_csv(filename, usecols=["Date", "Time", "Sensor Glucose (mg/dL)"]))

df = pd.concat(list_of_dataframes, ignore_index=True)

df3 = pd.read_csv("CGM_patient2.csv", usecols=["Date", "Time", "Sensor Glucose (mg/dL)"])

df['DT'] = df['Date'] + ' ' +df['Time']
df['DT'] =pd.to_datetime(df['DT'])

df3['DT'] = df3['Date'] + ' ' +df3['Time']
df3['DT'] =pd.to_datetime(df3['DT'])

mealData = pd.DataFrame()
tim = pd.DataFrame()
nonMealData = pd.DataFrame()
prevTime = None

for j,i in tm.iterrows():
    #print(i['DT'])   
    dataF = df[(df['DT'] >= (i['DT'] - timedelta(minutes=30))) & (df['DT'] <= (i['DT'] + timedelta(minutes=120)))]
    tim = tim.append(dataF.iloc[0])
    a = dataF['Sensor Glucose (mg/dL)'].tolist()
    mealData = mealData.append([a])

for j,i in tm1.iterrows():
    #print(i['DT'])
    dataF = df3[(df3['DT'] >= (i['DT'] - timedelta(minutes=30))) & (df3['DT'] <= (i['DT'] + timedelta(minutes=120)))]['Sensor Glucose (mg/dL)']
    a = dataF.tolist()
    mealData = mealData.append([a])
#mealData = mealData[mealData.columns[range(30)]]
#mealData = mealData.dropna()


for j,i in tm.iloc[1:].iterrows():
    dataF1 = df[(df['DT'] > (i['DT'] + timedelta(minutes=120))) & (df['DT'] < (tm.iloc[j-1]['DT'] - timedelta(minutes=30)))]
    dataF1 = dataF1.reset_index()
    if len(dataF1) > 1:
        if ((dataF1.iloc[0]['DT'] - dataF1.iloc[-1]['DT'])// pd.Timedelta(hours=1)) > 1:
            b = 0
            for i in range(((dataF1.iloc[0]['DT'] - dataF1.iloc[-1]['DT'])// pd.Timedelta(hours=1))//2):
                nm = dataF1[(dataF1['DT'] <= dataF1.iloc[b]['DT']) & (dataF1['DT'] >= dataF1.iloc[b]['DT'] - timedelta(minutes=120))]
                b += len(nm)
                a = nm['Sensor Glucose (mg/dL)'].tolist()
                nonMealData = nonMealData.append([a])

for j,i in tm1.iloc[1:].iterrows():
    dataF1 = df3[(df3['DT'] > (i['DT'] + timedelta(minutes=120))) & (df3['DT'] < (tm1.iloc[j-1]['DT'] - timedelta(minutes=30)))]
    dataF1 = dataF1.reset_index()
    if len(dataF1) > 1:
        if ((dataF1.iloc[0]['DT'] - dataF1.iloc[-1]['DT'])// pd.Timedelta(hours=1)) > 1:
            b = 0
            #print(dataF1)
            for i in range(((dataF1.iloc[0]['DT'] - dataF1.iloc[-1]['DT'])// pd.Timedelta(hours=1))//2):
                if b < len(dataF1):
                    nm = dataF1[(dataF1['DT'] <= dataF1.iloc[b]['DT']) & (dataF1['DT'] >= (dataF1.iloc[b]['DT']- timedelta(minutes=120)))]
                b += len(nm)
                a = nm['Sensor Glucose (mg/dL)'].tolist()
                nonMealData = nonMealData.append([a])
                
#nonMealData = nonMealData[nonMealData.columns[range(1,25)]]
nonMeal = nonMealData[nonMealData.columns[range(24)]]
nonMeal = nonMeal.dropna()
mealData = mealData[mealData.columns[range(24)]]
mealData = mealData.dropna()



mealData['val'] = 1
nonMeal['val'] = 0


da = mealData.append(nonMeal)


y = da['val']
x = da.drop(['val'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)

clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=500, alpha=0.0001,
                     solver='sgd', verbose=5,  random_state=21)

clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

pickle.dump(clf, open('model.pickle', 'wb'))
print(y_pred)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

