#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:45:49 2020
comparing observed temperature with model temp of doppio and fvcom, calculate std

@author: pengrui
"""
import numpy as np
import pandas as pd

db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path2='/home/zdong/PENGRUI/'


data = pd.read_csv(path2+'special_data.csv')
data = data.dropna()

depth = data.groupby(['PTT','gps_date'])['depth'].apply(lambda x:x.tolist())

obs = data.groupby(['PTT','gps_date'])['obs_temp'].apply(lambda x:x.tolist())
dop = data.groupby(['PTT','gps_date'])['doppio_temp'].apply(lambda x:x.tolist())
fvc = data.groupby(['PTT','gps_date'])['FVCOM_temp'].apply(lambda x:x.tolist())
#std=
obs_suf=[]
obs_btm=[]
dop_suf=[]
dop_btm=[]
fvc_suf=[]
fvc_btm=[]
o_d_std=[]
o_f_std=[]
for i in range(len(obs)):
    obs_suf.append(round(obs[i][0],1))
    obs_btm.append(round(obs[i][-1],1))
    dop_suf.append(round(dop[i][0],1))
    dop_btm.append(round(dop[i][-1],1))
    fvc_suf.append(round(fvc[i][0],1))
    fvc_btm.append(round(fvc[i][-1],1))
    
    o_d_std.append(round(np.std(obs[i]+dop[i]),1))
    o_f_std.append(round(np.std(obs[i]+fvc[i]),1))
#convert format from list to series
#obs_suf=pd.Series(obs_suf)    
    
    
    


stats = pd.DataFrame()
stats['PTT']=pd.Series(depth)
stats['PTT']=pd.Series(depth)
stats.to_csv('stats.csv')
stat = pd.read_csv('stats.csv')
stat['dive_num'] = stat['gps_date'].groupby(stat['PTT']).rank()
stat['obs_suf']=pd.Series(obs_suf)
stat['dop_suf']=pd.Series(dop_suf)
stat['fvc_suf']=pd.Series(fvc_suf)
stat['obs_btm']=pd.Series(obs_btm)
stat['dop_btm']=pd.Series(dop_btm)
stat['fvc_btm']=pd.Series(fvc_btm)
stat['obs_dop_std']=pd.Series(o_d_std)
stat['obs_fvc_std']=pd.Series(o_f_std)
stat=stat[['PTT','dive_num','gps_date','obs_suf','dop_suf','fvc_suf','obs_btm','dop_btm','fvc_btm','obs_dop_std','obs_fvc_std']]

stat.to_csv('stats.csv')

