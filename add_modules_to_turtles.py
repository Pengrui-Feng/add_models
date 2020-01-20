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
#path1='/home/zdong/PENGRUI/merge_split/'
path1=''

#obsData = pd.read_csv('data_for_Doppio.csv')#Mingchao
obsData = pd.read_csv(path1+db+'_merge_split.csv')#Pengrui

obsData['argos_date'] = pd.to_datetime(obsData['argos_date'])
date = obsData['argos_date']
lat = obsData['lat_gps']
lon = obsData['lon_gps']
lat1 = obsData['lat_argos']
lon1 = obsData['lon_argos']
depth = obsData['depth']
temp = obsData['temp']
'''
#obsData['datet'] = pd.to_datetime(obsData['datet'])
date = obsData['datet']
lat = obsData['lat']
lon = obsData['lon']
depth = obsData['depth']
temp = obsData['mean_temp']

'''
doppio_temp = []
FVCOM_temp = []
gomofs_temp = []

for i in tqdm(range(19)):
#for i in tqdm(range(len(obsData))):
    if pd.isnull(lat[i]) or pd.isnull(lon[i]):
        lat[i],lon[i]=lat1[i],lon1[i]
    d_temp=dm.get_doppio(lat[i],lon[i],depth=depth[i],time=str(date[i]))
    #b=gm.get_gomofs(date[i],lat[i],lon[i],fortype='temperature')
    #c=fm.get_FVCOM_temp(lat[i],lon[i],date[i],depth='bottom',mindistance=2,fortype='temperature')
    print (d_temp)
    #print (b)
    #print (c)
    doppio_temp.append(d_temp)
    #FVCOM_temp.append(b)
    #gomofs_temp.append(c)

c = pd.DataFrame()
c['date']=pd.Series(date)
c['lat']=pd.Series(lat)
c['lon']=pd.Series(lon)
c['depth']=pd.Series(depth)
c['doppio_temp']=pd.DataFrame(doppio_temp)
#c['FVCOM_temp']=pd.DataFrame(FVCOM_temp)
#c['gomofs_temp']=pd.DataFrame(gomofs_temp)
c['obs_temp']=pd.Series(temp)

#c.to_csv(db+'withModules.csv')

