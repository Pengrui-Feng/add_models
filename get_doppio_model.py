#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 8 12:15:07 2020
testing the "get_doppio" function
found another one called get_doppio_test.py which has different method not using "fitting"
@author: pengrui
"""

from datetime import timedelta,datetime
from dateutil import parser
import pandas as pd
import pytz
import glob
import numpy as np
import netCDF4
#import zlconversions as zl # Lei Zhao's module

def get_doppio_url(date):
    url='http://tds.marine.rutgers.edu/thredds/dodsC/roms/doppio/2017_da/his/runs/History_RUN_2018-11-12T00:00:00Z'
    return url.replace('2018-11-12',date)

#get_doppio no fitting
def get_doppio(lat,lon,time,depth):
    """
    notice:
        the format of time is like "%Y-%m-%d %H:%M:%S"
        the default depth is under the bottom depth
    the module only output the temperature of point location
    """
    time=dt.strptime(time,'%Y-%m-%d %H:%M:%S') # transform time format
    if (time -datetime(2017,11,1,0,0,0)).total_seconds()<0:
        #print('the date can\'t be earlier than 2017-11-1')
        return np.nan
    
    url_time=time.strftime('%Y-%m-%d')#
    url=get_doppio_url(url_time)
    nc=netCDF4.Dataset(url).variables
    #first find the index of the grid 
    lons=nc['lon_rho'][:]
    lats=nc['lat_rho'][:]
    temp=nc['temp']
    #second find the index of time
    doppio_time=nc['time']
    itime = netCDF4.date2index(time,doppio_time,select='nearest')# where startime in datetime
    # figure out layer from depth
    
    min_distance=zl.dist(lat1=lat,lon1=lon,lat2=lats[0][0],lon2=lons[0][0])   
    index_1,index_2=0,0
    for i in range(len(lons)):
        for j in range(len(lons[i])):
            if min_distance>zl.dist(lat1=lat,lon1=lon,lat2=lats[i][j],lon2=lons[i][j]):
                min_distance=zl.dist(lat1=lat,lon1=lon,lat2=lats[i][j],lon2=lons[i][j])
                index_1=i
                index_2=j
    
    doppio_depth=nc['h'][index_1][index_2]
    
    if depth > doppio_depth:# case of bottom
            S_coordinate=1
    else:
        S_coordinate=float(depth)/float(doppio_depth)
    if 0<=S_coordinate<1:
        doppio_temp=temp[itime,39-int(S_coordinate/0.025),index_1,index_2]# because there are 0.025 between each later
    elif S_coordinate==1:
        doppio_temp=temp[itime][0][index_1][index_2]
    else:
        doppio_temp=temp[itime][0][index_1][index_2]
    return doppio_temp

'''
#HARDCODES ##########
lat,lon=41.9294739,-70.26013184
time='2018-08-15 10:04:57'
depth=35#'bottom'
# main
model_temp=get_doppio(lat,lon,time,depth=depth)
print (depth,model_temp)
'''
