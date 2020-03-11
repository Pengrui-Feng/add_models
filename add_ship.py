# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:26:31 2020

@author: pengrui
"""

import pandas as pd
import numpy as np
import math
from datetime import datetime,timedelta
import zlconversions as zl
import matplotlib.pyplot as plt
from turtleModule import draw_basemap
#from tqdm import tqdm
r = 3   # the boat position that has gps position within (r) kilometers 
h = 3   # the ctd time that has gps time within (h) hours

def numSplit(num):

    hour=int(math.floor(num))
    minn = round((num-hour),2)
    mins= int(minn*60)
    time = '{0}:{1}:00'.format(str(hour).zfill(2),str(mins).zfill(2))
    return time

def nearlonlat(lon,lat,lonp,latp): # needed for the next function get_FVCOM_bottom_temp
    """
    i=nearlonlat(lon,lat,lonp,latp) change
    find the closest node in the array (lon,lat) to a point (lonp,latp)
    input:
        lon,lat - np.arrays of the grid nodes, spherical coordinates, degrees
        lonp,latp - point on a sphere
        output:
            i - index of the closest node
            For coordinates on a plane use function nearxy           
            Vitalii Sheremet, FATE Project  
    """
    cp=np.cos(latp*np.pi/180.)
    # approximation for small distance
    dx=(lon-lonp)*cp
    dy=lat-latp
    dist2=dx*dx+dy*dy
    i=np.argmin(dist2)
    return i

#ship1 = pd.read_csv('nefsc_hydro_for_erddap.csv') #4710692 rows
'''
###filter the data
ship= pd.read_csv('nefsc_hydro_for_erddap.csv',skiprows= 4370000)#,nrows=200,usecols=[0,2,3,4,5,6,7,8],header=None)
ship.to_csv('ship_data.csv')

ship= pd.read_csv('ship_data.csv',usecols=[2,3,4,5,6,7,8,9],header=None)

ship.columns=['vessel_num','dive_num','date','time','lat','lon','depth','temp']

for i in range(len(ship)):
    ship['time'][i] = numSplit(ship['time'][i])

ship['datetime']=pd.to_datetime(ship['date']+' '+ship['time'])
ship['lon']=-ship['lon']
ship=ship[['vessel_num','dive_num','datetime','lat','lon','depth','temp']]

#ship.to_csv('ship_data.csv')
'''

###observe the positon of ship
lonsize = [-77.8, -63.8]#tu99
latsize = [32.8, 46.8]#tu199
obsdata = pd.read_csv('ship_data.csv')
lon=obsdata['lon']
lat=obsdata['lat']
fig =plt.figure()
ax = fig.add_subplot(111)
for i in range(10000,len(obsdata),100):
    plt.scatter(lon[i],lat[i],s=15,linewidths=None)
draw_basemap(fig, ax, lonsize, latsize, interval_lon=2, interval_lat=2) 

plt.show()


'''
s = pd.read_csv('ship_data.csv') 
s['depth']=s['depth'].astype('str')
s['temp']=s['temp'].astype('str')
t = pd.read_csv('tu102_merge_nosplit.csv') # orginal data file
tlat = t['lat_gps']
tlon = t['lon_gps']
ttime = t['gps_date']
data1=s.groupby(['vessel_num','datetime','lat','lon'])['depth','temp'].agg(lambda x:x.str.cat(sep=','))
data1.to_csv('ship_data2.csv')

s = pd.read_csv('ship_data2.csv')
slat = s['lat']
slon = s['lon']
stime = s['datetime']

index = []
'''

'''
for lat, lon, stm in zip(slat, slon, stime):
    l = zl.dist(slon, slat, tlon, tlat)
    p = np.where(l<r)
    maxtime = stm+timedelta(hours=h)
    mintime = stm-timedelta(hours=h)
    mx = ttime[p[0]]<maxtime
    mn = ttime[p[0]]>mintime
    #print mx,mn
    TF = mx*mn
    if TF.any():
        index.append(i)
    i += 1



for i in range(100):
    
    #l = zl.dist(slon[i], slat[i], tlon[j], tlat[j])
    #p = np.where(l<10)[0]
    #time= 
    inode = nearlonlat(slon[i],slat[i],tlon,tlat)
    index.append(inode)
'''        
'''   
r1,r2 = 0,3                # the obs position that has shipboard position within (r) kilometers might be considered as good data.
day = 3                # the obs time that has shipboard time within (3 days) days might be considered as good data.
s = pd.read_csv('ship_data2.csv')
s_id = s['vessel_num']
slat = s['lat']
slon = s['lon']
stime = pd.Series(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in s['datetime'])
sdepth = s['depth']
stemp= s['temp']

t = pd.read_csv('tu102_merge_td_gps.csv') # orginal data file
t_id= t['PTT']
tlat = t['lat_argos']
tlon = t['lon_argos']
ttime = pd.Series(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in t['argos_date'])
tdepth = t['depth']
ttemp= t['temp']
index = []     #index of turtle
indx=[]      #index of shipboard 

for i in tqdm(range(len(s))):
    for j in range(len(t)):
        l = zl.dist(slat[i],slon[i],tlat[j],tlon[j])
        if l<r2 and l>=r1:
            #print l        #distance
            maxtime = ttime[i]+timedelta(days=day)
            mintime = ttime[i]-timedelta(days=day)
            mx = stime[j]<maxtime
            mn = stime[j]>mintime
            TF = mx*mn  
            if TF==1:      #time
                index.append(i)     #turtle index
                indx.append(j)      #ship index

INDX=pd.Series(indx).unique() 
data=pd.DataFrame(range(len(indx)))
s_id,t_id,s_time,t_time,s_lat,s_lon,t_lat,t_lon=[],[],[],[],[],[],[],[]
s_depth,s_temp,t_depth,t_temp=[],[],[],[]
for i in INDX:
    for j in range(len(indx)):
        if indx[j]==i:
            s=indx[j]
            t=index[j]
            s_id.append(s_id[s])
            s_time.append(s['datetime'][s])
            s_lat.append(slat[s])
            s_lon.append(slon[s])
            s_depth.append(sdepth[s])
            s_temp.append(stemp[s])
            t_id.append(t_id[t])
            t_time.append(t['argos_date'][t])
            t_lat.append(tlat[t])
            t_lon.append(tlon[t])
            t_depth.append(tdepth[t])
            t_temp.append(ttemp[t])

data['ship_id']=pd.Series(s_id)
data['ship_time']=pd.Series(s_time)
data['ship_lat']=pd.Series(s_lat)
data['ship_lon']=pd.Series(s_lon)
data['ship_depth']=pd.Series(s_depth)
data['ship_temp']=pd.Series(s_temp)
data['turtle_id']=pd.Series(t_id)
data['turtle_time']=pd.Series(t_time)
data['turtle_lat']=pd.Series(t_lat)
data['turtle_lon']=pd.Series(t_lon)
data['turtle_depth']=pd.Series(t_depth)
data['turtle_temp']=pd.Series(t_temp)

data.to_csv('matched_turtleVSship.csv')       
        
'''
