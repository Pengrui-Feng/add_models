#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:15:07 2020

@author: pengrui
"""
from tqdm import tqdm
import netCDF4
import numpy as np
import pandas as pd
import zlconversions as zl
import doppio_model as dm
#import FVCOM_modules as fm
#import gomofs_modules as gm

db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/home/zdong/PENGRUI/merge_split/'

Data = pd.read_csv(path1+db+'_merge_split.csv')
Data['argos_date'] = pd.to_datetime(Data['argos_date'])
date = Data['argos_date']
lat = Data['lat_gps']
lon = Data['lon_gps']
lat1 = Data['lat_argos']
lon1 = Data['lon_argos']
depth = Data['depth']
temp = Data['temp']

doppio_temp = []
FVCOM_temp = []
gomofs_temp = []

for i in tqdm(range(len(Data))):
    if pd.isnull(lat[i]) or pd.isnull(lon[i]):
        lat[i],lon[i]=lat1[i],lon1[i]
    d_temp=dm.get_doppio(lat[i],lon[i],depth=depth[i],time=str(date[i]))
    #b=gm.get_gomofs(date[i],lat[i],lon[i],fortype='temperature')
    #c=fm.get_FVCOM_temp(lat[i],lon[i],date[i],depth='bottom',mindistance=2,fortype='temperature')
    #print (d_temp)
    #print (b)
    #print (c)
    doppio_temp.append(round(d_temp,3))
    #FVCOM_temp.append(b)
    #gomofs_temp.append(c)
    #print(doppio_temp)
  

Data['doppio_temp']=pd.DataFrame(doppio_temp)
#c['FVCOM_temp']=pd.DataFrame(FVCOM_temp)
#c['gomofs_temp']=pd.DataFrame(gomofs_temp)
Data.rename(index=str, columns={"temp": "obs_temp"},inplace=True)
Data=Data[['dive_num','PTT','argos_date','lat_argos','lon_argos','gps_date','lat_gps','lon_gps','depth','obs_temp','doppio_temp']]
Data.to_csv(db+'withModels.csv')
