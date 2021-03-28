#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:58:54 2021

@author: ram
"""
from sklearn import preprocessing
import pandas as pd
from datetime import timedelta
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import contingency_matrix
from sklearn.metrics import confusion_matrix
from scipy.stats import entropy
#from sklearn.preprocessing import Imputer


def calcSSE(df):
    sse = 0
    for key, item in df:
        #print(df.get_group(key)[0])
        
        d = 0
        m1 = df.get_group(key)[0].mean()
        m2 = df.get_group(key)[0].mean()
        
        for j,i in df.get_group(key).iterrows():
            #print(i['feat1'])
            d = ((i[0] - m1) **2 + (i[0] - m2) **2)
        sse += d
    return sse
def calcEntropy(cf, ent):
    s = []
    for i in range(len(cf)):
        s.append(cf[i].sum())
    print(s)
    tot = cf.sum()
    
    tote = 0
    for i in range(len(s)):
        tote += (s[i]/tot) * e[i]
    return tote
        

df2 = pd.read_csv("InsulinData.csv", usecols=["Date", "Time", "BWZ Carb Input (grams)"])
df2['DT'] = df2['Date'] + ' ' +df2['Time']
df2['DT'] =pd.to_datetime(df2['DT'])
df2 = df2.dropna()
df2 = df2[df2['BWZ Carb Input (grams)'] > 0]
#df2 = df2.sort_values(by=['BWZ Carb Input (grams)'])
#df2['bin_label'] = 1
df = []
updatedf = pd.DataFrame()
l = 1
a = df2['BWZ Carb Input (grams)'].min()
for i in range(int(df2['BWZ Carb Input (grams)'].min()),int(df2['BWZ Carb Input (grams)'].max()), 20):
    tempdf = pd.DataFrame
    if a+40 > df2['BWZ Carb Input (grams)'].max():
        tempdf = df2[(df2['BWZ Carb Input (grams)'] >= a) & (df2['BWZ Carb Input (grams)'] <=  df2['BWZ Carb Input (grams)'].max())]
        del tempdf['Date']
        del tempdf['DT']
        del tempdf['Time']
        tempdf['bin_label'] = l
        updatedf  = updatedf.append(tempdf)
        df.append(tempdf)
        break
    tempdf = df2[(df2['BWZ Carb Input (grams)'] >= a) & (df2['BWZ Carb Input (grams)'] < a+20 )]
    del tempdf['Date']
    del tempdf['DT']
    del tempdf['Time']
    tempdf['bin_label'] = l
    updatedf =updatedf.append(tempdf)
    df.append(tempdf)
    a += 20
    l += 1
print(updatedf)

df3 = pd.read_csv("CGMData.csv", usecols=["Date", "Time", "Sensor Glucose (mg/dL)"])

df3['DT'] = df3['Date'] + ' ' +df3['Time']
df3['DT'] =pd.to_datetime(df3['DT'])

tm = df2
#tm['hrs'] = tm['DT'][::-1].diff().astype('timedelta64[h]')
#tm = tm[tm['hrs'] >=2]
tm = tm.reset_index()
mealData = pd.DataFrame()
for j,i in tm.iterrows():
    #print(i['DT'])   
    dataF = df3[(df3['DT'] >= (i['DT'] - timedelta(minutes=30))) & (df3['DT'] <= (i['DT'] + timedelta(minutes=120)))]
    a = dataF['Sensor Glucose (mg/dL)'].tolist()
    mealData = mealData.append([a])

mealData = mealData[mealData.columns[range(24)]]
#mealData = mealData.dropna()
mealData.to_csv('mealData.csv')
X = mealData

fm1 = pd.DataFrame()
fm1['feat1'] = (X.max(axis =1) - X.min(axis=1))
fm1['feat2'] = ((X.max(axis =1) - X.min(axis=1))/X.min(axis=1))



fm1['feat1'] = fm1['feat1'].fillna(0)
fm1['feat2'] = fm1['feat2'].fillna(0)
#df['DataFrame Column'] = df['DataFrame Column'].fillna(0)
print(fm1)
ss = preprocessing.StandardScaler()
X2 = ss.fit_transform(fm1)
X3 = pd.DataFrame(X2)

X5 = fm1['feat2']
ss = preprocessing.StandardScaler()
X4 = ss.fit_transform(X5.values.reshape(-1,1))
X4 = pd.DataFrame(X4)

clustering = DBSCAN(eps=0.1, min_samples=5).fit(X4)
#core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
#core_samples_mask[clustering.core_sample_indices_] = True
labels = clustering.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_noise_)
print(n_clusters_)

X4['lbl'] = labels
a = X4.groupby(by='lbl')
print(X4)
dbsse = calcSSE(a)
print(dbsse)
X4['lbl'] = labels+2


X1 = updatedf
kmeans = KMeans(n_clusters=6, max_iter=200).fit(X3)
X3["clusters"] = kmeans.labels_+1
sse = kmeans.inertia_ 
print(sse)
print(X3)
means = KMeans(n_clusters=6, max_iter=200).fit(X1)
X1["clusters"] = kmeans.labels_+1
print(X1)
m1 = X3['clusters']
m2 = X1['bin_label']


#print(createCM())
cm = confusion_matrix(m2,m1)
print(cm)
e = entropy(cm)
#print(e)
entropyk = calcEntropy(cm, e)
print(calcEntropy(cm, e))

m3= X4['lbl']
cm1 = confusion_matrix(m2,m3)
print(cm1)
e1 = entropy(cm1)
#print(e1)

entropyd = calcEntropy(cm1, e1)
print(entropyd)


purity1=np.amax(cm,axis=1).sum()/cm.sum()
print(purity1)
purity2 = np.amax(cm1,axis=1).sum()/cm1.sum()
print(purity2)

result = [[sse,dbsse,entropyk, entropyd, purity1,purity2] ]

resuldf = pd.DataFrame(result)
resuldf.to_csv("Result.csv",index = False, header=None)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    