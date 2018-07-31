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







path = r'/run/media/mjayk/Media_1/Documents/AirXD/A6'
os.chdir(path)

fnames = glob.glob('*.CSV')

plt.figure(1)
plt.clf()


for lmn in np.linspace(0,len(fnames)-1,len(fnames)):
    lmn = int(lmn)
    fname = fnames[lmn]
    date = datetime.datetime.strptime(fname[0:6],'%y%m%d')
    
    
    datet = [] 
    bindata, sfr, sampletime, dt, volume, density, xx, pmr = MJC.LoadFile(fname,path)
    
    for prq in np.linspace(0,len(dt)-1,len(dt)):
        prq= int(prq)
        datet.append(datetime.datetime.combine(date,dt[prq]))
        
    window = 6*60
    averagepmr = MJC.running_mean(pmr,window)
    
    
    plt.figure(1)
    plt.plot_date(datet,pmr,marker='.',c='r',alpha=0.25,markersize=1)
    plt.plot_date(datet,averagepmr,linestyle='solid',marker=',',c='r')
    plt.grid(True)
    


    
    

    plt.pause(0.00001)
    plt.show()
    