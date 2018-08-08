#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:09:35 2018

@author: mjayk
"""

import MJC_Functions as MJC
import glob
import os
import datetime as datetime
import numpy as np 
import matplotlib.pyplot as plt 

def running_mean(x, N):
    if len(x) >=N:
        cumsum = np.cumsum(np.insert(x, 0, 0)) 
        avg = np.zeros(len(x))
        avg[N-2:len(x)-1]=(cumsum[N:] - cumsum[:-N]) / float(N)
        avg[0:N] = np.cumsum(x[0:N])/N

    else:
        avg = np.cumsum(x)/N
    return avg


def LoadGovData():
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
        
    return dt,pmr

def LoadTrolexData(plot,scatter):
    path = r'C:\Users\mattj\OneDrive - trolex\AirXD\A6Analysis31-7-2018'
    os.chdir(path)
    
    fnames = glob.glob('*.CSV')
    
   
    
    
    for lmn in np.linspace(0,len(fnames)-1,len(fnames)):
        lmn = int(lmn)
        fname = fnames[lmn]
        date = datetime.datetime.strptime(fname[0:6],'%y%m%d')
        
        
        datet = [] 
        bindata, sfr, sampletime, dt, volume, density, xx, pmr = MJC.LoadFile(fname,path)
        
        for prq in np.linspace(0,len(dt)-1,len(dt)):
            prq= int(prq)
            datet.append(datetime.datetime.combine(date,dt[prq]))
            
        window = 6*60*2
        averagepmr = running_mean(pmr,window)
        
        if plot == 1:
        
            plt.figure(1)
            if scatter == 1:
                plt.plot_date(datet,pmr/1.65,marker='.',c='r',alpha=0.25,markersize=1)
            
            plt.plot_date(datet,averagepmr,linestyle='solid',marker=',',c='r')
            plt.grid(True)
        

plt.figure(1)
plt.clf()
LoadTrolexData(1,1)   
dt,govpmr = LoadGovData()
plt.plot_date(dt,govpmr)
plt.plot_date()
plt.xlabel('Date / Time')
plt.ylabel('PM 10')
plt.title('2 Hour TWA for Trolex data')
plt.ylim([0,200])
    
    
plt.show()
    