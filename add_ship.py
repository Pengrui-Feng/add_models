# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:26:31 2020

@author: pengrui
"""

import pandas as pd
import numpy as np
import math
from datetime import datetime

r = 3   # the boat position that has gps position within (r) kilometers 
h = 3   # the ctd time that has gps time within (h) hours


def numSplit(num):

    hour=int(math.floor(num))
    minn = round((num-hour),2)
    mins= int(minn*60)
    time = '{0}:{1}:00'.format(str(hour).zfill(2),str(mins).zfill(2))
    return time



#ship1 = pd.read_csv('nefsc_hydro_for_erddap.csv') #4710692 rows

#ship= pd.read_csv('nefsc_hydro_for_erddap.csv',skiprows= 4520000)#,nrows=200,usecols=[0,2,3,4,5,6,7,8],header=None)
#ship.to_csv('ship_data.csv')
'''
ship= pd.read_csv('ship_data.csv',usecols=[2,3,4,5,6,7,8,9],header=None)


ship.columns=['vessel_num','dive_num','date','time','lat','lon','depth','temp']

for i in range(len(ship)):
    ship['time'][i] = numSplit(ship['time'][i])

ship['datetime']=pd.to_datetime(ship['date']+' '+ship['time'])
ship['lon']=-ship['lon']
ship=ship[['vessel_num','dive_num','datetime','lat','lon','depth','temp']]

#ship.to_csv('ship_data.csv')
'''
#turtle= pd.read_csv('')

s = pd.read_csv('ship.csv') 
slat = s['lat']
slon = s['lon']
stime = np_datetime(s['datetime'])
gps = pd.read_csv('2014_04_16_rawgps.csv') # orginal data file
gpslat = gps['LAT']
gpslon = gps['LON']
gpstime = np_datetime(gps['D_DATE'])
lonsize = [np.min(ctdlon), np.max(ctdlon)]
latsize = [np.min(ctdlat), np.max(ctdlat)]


index = []
i = 0
for lat, lon, ctdtm in zip(ctdlat, ctdlon, ctdtime):
    l = dist(lon, lat, gpslon, gpslat)
    p = np.where(l<r)
    maxtime = ctdtm+timedelta(hours=hour)
    mintime = ctdtm-timedelta(hours=hour)
    mx = gpstime[p[0]]<maxtime
    mn = gpstime[p[0]]>mintime
    #print mx,mn
    TF = mx*mn
    if TF.any():
        index.append(i)
    i += 1













