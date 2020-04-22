#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:15:07 2020
input merge csv files(spliting depth),get models temps
@author: pengrui
"""
from tqdm import tqdm
import netCDF4
import numpy as np
import pandas as pd
import zlconversions as zl
from get_doppio_model import *
from get_fvcom_model import *
from get_espresso_model import *
from datetime import datetime 

db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/content/drive/My Drive/PENGRUI/merge_split/'

Data = pd.read_csv(path1+db+'_merge_split.csv')
date = pd.to_datetime(Data['gps_date'])
lat = Data['lat_gps']
lon = Data['lon_gps']
depth = Data['depth']
date1 = pd.to_datetime(Data['argos_date'])
lat1=Data['lat_argos']
lon1=Data['lon_argos']
#temp = Data['temp']

doppio_temp = []
FVCOM_temp = []
espresso_temp = []

#for i in tqdm(range(27,29)):
for i in tqdm(range(len(Data))):
    if pd.isnull(lat[i]) or pd.isnull(lon[i]):
        date[i],lat[i],lon[i]=date1[i],lat1[i],lon1[i]
    d_temp=get_doppio(lat[i],lon[i],depth=depth[i],time=str(date[i]))
    f_temp=get_FVCOM_temp(lat[i],lon[i],dtime=str(date[i]),depth=depth[i])
    e_temp=get_espresso_temp(str(date[i]),lat[i],lon[i],depth[i])
    #print (depth[i],d_temp)
    #print (depth[i],f_temp)
    doppio_temp.append(d_temp)
    FVCOM_temp.append(f_temp)
    espresso_temp.append(e_temp)
Data['doppio_temp']=pd.DataFrame(doppio_temp)
Data['FVCOM_temp']=pd.DataFrame(FVCOM_temp)
Data['espresso_temp']=pd.DataFrame(espresso_temp)
Data.rename(index=str, columns={"temp": "obs_temp"},inplace=True)
Data=Data[['PTT','dive_num','argos_date','lat_argos','lon_argos','gps_date','lat_gps','lon_gps','depth','obs_temp','FVCOM_temp','doppio_temp','espresso_temp']]
Data['depth']= Data['depth'].astype('str')
Data['obs_temp']= Data['obs_temp'].astype('str')
Data['FVCOM_temp']= Data['FVCOM_temp'].astype('str')
Data['doppio_temp']= Data['doppio_temp'].astype('str')
Data['espresso_temp']= Data['espresso_temp'].astype('str')
Data= Data.groupby(['PTT','dive_num','argos_date','lat_argos','lon_argos','gps_date','lat_gps','lon_gps'])['depth','obs_temp','FVCOM_temp','doppio_temp','espresso_temp'].agg(lambda x:x.str.cat(sep=','))
Data.to_csv('/content/drive/My Drive/'+db+'wModels.csv')
