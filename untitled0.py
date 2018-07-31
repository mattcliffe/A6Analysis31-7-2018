
import MJC_Functions as MJC
import glob
import os
import datetime as datetime
import numpy as np 
import matplotlib.pyplot as plt 

fname = 'Gov_Data_31-7-2018.csv'

data = np.genfromtxt(fname,delimiter=',',skip_header=7,usecols=2)