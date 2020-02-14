#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:45:49 2020

@author: pengrui
"""
import numpy as np
import pandas as pd

db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path2='/home/zdong/PENGRUI/'


data = pd.read_csv(path2+db+'withModels.csv')
data = data.dropna()
a = data['depth'].groupby(data['PTT'])
b = data.groupby(['PTT','argos_date'])['depth'].apply(lambda x:x.tolist())
depth = data.groupby(['PTT','argos_date'])['depth']
obs = data.groupby(['PTT','argos_date'])['obs_temp']
dop = data.groupby(['PTT','argos_date'])['doppio_temp']

#std=
#Data['dive_num'] = Data['argos_date'].groupby(Data['PTT']).rank()



stats = pd.DataFrame()
#stats.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False) 
#stats.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')

stats['obs_bot_temp']=pd.Series(obs.min())
stats['obs_suf_temp']=pd.Series(obs.max())
stats['mod_suf_temp']=pd.Series(dop.max())
stats['mod_bot_temp']=pd.Series(dop.min())
stats['obs_mod_diff_mean']=pd.Series(dop.mean()-obs.mean())
#stats['obs_mod_diff_mean']=pd.Series(round(dop.mean()-obs.mean(),3))




stats.to_csv('stats.csv')
stat = pd.read_csv('stats.csv')
stat['dive_num'] = stat['argos_date'].groupby(stat['PTT']).rank()
stat=stat[['PTT','dive_num','argos_date','obs_bot_temp','obs_suf_temp','mod_suf_temp','mod_bot_temp','obs_mod_diff_mean']]
stat.to_csv('stats.csv')

