#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 06:49:33 2021

@author: ram
"""

import pandas as pd
from datetime import datetime

class calcHyp:

    def returnMean(dataf, timeStart: str, timeEnd: str, cgmL, cgmH, hl:str):
        temp = dataf.groupby("Date").count()
        dataf = dataf[dataf["Sensor Glucose (mg/dL)"].notna()]
        dataf['count'] = dataf.groupby('Date')['Date'].transform('count')
        
        dataf = dataf[dataf['count'] >= 231]
        if hl == "high":
            hyperglycemia = dataf[(dataf["Sensor Glucose (mg/dL)"] > cgmL) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S")) <= datetime.strptime(timeEnd, "%H:%M:%S")) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S"))  >= datetime.strptime(timeStart,  "%H:%M:%S"))].groupby('Date').count()*(100/288)
        elif hl == "low":
            hyperglycemia = dataf[(dataf["Sensor Glucose (mg/dL)"] < cgmH) &  (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S")) <= datetime.strptime(timeEnd, "%H:%M:%S")) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S"))  >= datetime.strptime(timeStart,  "%H:%M:%S"))].groupby('Date').count()*(100/288)
        elif hl == "range":
            if cgmH == 150:
                hyperglycemia = dataf[(dataf["Sensor Glucose (mg/dL)"] <= cgmH) &  (dataf["Sensor Glucose (mg/dL)"] >= cgmL) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S")) < datetime.strptime(timeEnd, "%H:%M:%S")) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S"))  >= datetime.strptime(timeStart,  "%H:%M:%S"))].groupby('Date').count()*(100/288)    
            elif cgmH == 180:
                hyperglycemia = dataf[(dataf["Sensor Glucose (mg/dL)"] <= cgmH) &  (dataf["Sensor Glucose (mg/dL)"] >= cgmL) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S")) < datetime.strptime(timeEnd, "%H:%M:%S")) & (dataf['Time'].apply(lambda x : datetime.strptime(x, "%H:%M:%S"))  >= datetime.strptime(timeStart,  "%H:%M:%S"))].groupby('Date').count()*(100/288)
        return hyperglycemia["Time"].sum()/len(temp)
    
    df = pd.read_csv("CGMData.csv", usecols=["Date", "Time", "Sensor Glucose (mg/dL)"])
    df1 = pd.read_csv("InsulinData.csv",usecols=["Date", "Time", "Alarm"])
    df['DT'] = df['Date'] + ' ' +df['Time']
    df['DT'] =pd.to_datetime(df['DT'])
    tm = df1[df1['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF']
    bp = tm.iloc[-1]["Date"]+ ' ' +tm.iloc[-1]["Time"]
    bp = pd.to_datetime(bp)
    manual = df[df["DT"] < bp]
    
    
    auto = df[df["DT"] >= bp]
    
    dataF  = pd.DataFrame( [[
    returnMean(manual,"00:00:00","05:59:59", 180 , 0, "high" ),
    returnMean(manual,"00:00:00","05:59:59", 250, 0, "high" ),
    returnMean(manual,"00:00:00","05:59:59", 70, 180, "range" ),
    returnMean(manual,"00:00:00","05:59:59", 70, 150, "range" ),
    returnMean(manual,"00:00:00","05:59:59", 0, 70, "low" ),
    returnMean(manual,"00:00:00","05:59:59", 0, 54, "low" ),
    
    returnMean(manual,"06:00:00","23:59:00", 180 , 0, "high" ),
    returnMean(manual,"06:00:00","23:59:00", 250, 0, "high" ),
    returnMean(manual,"06:00:00","23:59:00", 70, 180, "range" ),
    returnMean(manual,"06:00:00","23:59:00", 70, 150, "range" ),
    returnMean(manual,"06:00:00","23:59:00", 0, 70, "low" ),
    returnMean(manual,"06:00:00","23:59:00", 0, 54, "low" ),
    
    returnMean(manual,"00:00:00","23:59:00", 180 , 0, "high" ),
    returnMean(manual,"00:00:00","23:59:00", 250, 0, "high" ),
    returnMean(manual,"00:00:00","23:59:00", 70, 180, "range" ),
    returnMean(manual,"00:00:00","23:59:00", 70, 150, "range" ),
    returnMean(manual,"00:00:00","23:59:00", 0, 70, "low" ),
    returnMean(manual,"00:00:00","23:59:00", 0, 54, "low" )], 
     [
    returnMean(auto,"00:00:00","05:59:59", 180 , 0, "high" ),
    returnMean(auto,"00:00:00","05:59:59", 250, 0, "high" ),
    returnMean(auto,"00:00:00","05:59:59", 70, 180, "range" ),
    returnMean(auto,"00:00:00","05:59:59", 70, 150, "range" ),
    returnMean(auto,"00:00:00","05:59:59", 0, 70, "low" ),
    returnMean(auto,"00:00:00","05:59:59", 0, 54, "low" ),
    
    returnMean(auto,"06:00:00","23:59:59", 180 , 0, "high" ),
    returnMean(auto,"06:00:00","23:59:59", 250, 0, "high" ),
    returnMean(auto,"06:00:00","23:59:59", 70, 180, "range" ),
    returnMean(auto,"06:00:00","23:59:59", 70, 150, "range" ),
    returnMean(auto,"06:00:00","23:59:59", 0, 70, "low" ),
    returnMean(auto,"06:00:00","23:59:59", 0, 54, "low" ),
    
    returnMean(auto,"00:00:00","23:59:59", 180 , 0, "high" ),
    returnMean(auto,"00:00:00","23:59:59", 250, 0, "high" ),
    returnMean(auto,"00:00:00","23:59:59", 70, 180, "range" ),
    returnMean(auto,"00:00:00","23:59:59", 70, 150, "range" ),
    returnMean(auto,"00:00:00","23:59:59", 0, 70, "low" ),
    returnMean(auto,"00:00:00","23:59:59", 0, 54, "low" )
    
    ]])
    
    dataF.to_csv("Results.csv", index = False, header=False)
    
    
    


