#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:54:04 2018

@author: mjayk
"""


import MJC_Functions as MJC
import glob
import os
import datetime as datetime
import numpy as np 
import matplotlib.pyplot as plt 

fname = 'Gov_Data_31-7-2018.csv'

pmr = np.genfromtxt(fname,delimiter=',',skip_header=1,usecols=2)
date = np.genfromtxt(fname,dtype=str,delimiter=',',skip_header=1,usecols=0)
time = np.genfromtxt(fname,dtype=str,delimiter=',',skip_header=1,usecols=1)

date_dt=[]
for lmn in np.linspace(0,len(date)-1,len(date)):
    lmn = int(lmn)
    date_dt.append(datetime.datetime.strptime(date[lmn],'%d/%m/%Y'))    
    
time_dt = []
for lmn in np.linspace(0,len(date)-1,len(date)):
    lmn = int(lmn)
    time_dt.append(datetime.datetime.strptime(time[lmn],'%H:%M:%S').time())    
    
dt = [] 

for lmn in np.linspace(0,len(time_dt)-1,len(time_dt)):
    lmn = int(lmn)
    dt.append(datetime.datetime.combine(date_dt[lmn],time_dt[lmn]))
    
plt.figure(1)
plt.clf()
plt.plot_date(dt,pmr)