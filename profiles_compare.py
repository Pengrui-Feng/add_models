#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:24:57 2020

@author: zdong
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from turtleModule import str2ndlist
##### SET basic parameters
db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/home/zdong/PENGRUI/merge/'
path2='/home/zdong/PENGRUI/'
start_time = datetime(2018,8,1).strftime('%m-%d-%Y') 
end_time = datetime(2018,10,29).strftime('%m-%d-%Y')   # create a forder named by 'IOError'
shift = 4
maxdepth = 60

'''
#data = pd.read_csv(path2+db+'withModels.csv')
data = pd.read_csv(path2+'s.csv')
dive = data['dive_num']
data['obs_temp'] = data['obs_temp'].astype('str')
data['doppio_temp']= data['doppio_temp'].astype('str')
data['depth']= data['depth'].astype('str')
#data1=data.groupby(['PTT','dive_num','argos_date','lat_argos','lon_argos','gps_date','lat_gps','lon_gps']).agg(lambda x:x.str.cat(sep=','))
data1=data.groupby(['PTT','argos_date'])['depth','obs_temp','doppio_temp'].agg(lambda x:x.str.cat(sep=','))
data1.to_csv('tu102_adapt1.csv')
'''
data2=pd.read_csv('tu102_adapt.csv')
t_id=data2['PTT'].unique()
Otemp = data2['obs_temp']
Dtemp = data2['doppio_temp']
obsTime = pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in data2['argos_date']))


for i in range(len(t_id)):       
    e=t_id[i]
    indx=[]  
    for i in data2.index:
        if data2['PTT'][i]==e:   
            indx.append(i)
    Data_e = data2.loc[indx]  
    Data_e.index= range(len(indx))             
    Time_e= pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in Data_e['argos_date']))
    Otemp = pd.Series(str2ndlist(Data_e['obs_temp']))
    Dtemp = pd.Series(str2ndlist(Data_e['doppio_temp']))
    Depth_e = pd.Series(str2ndlist(Data_e['depth']))
    
    fig=plt.figure()
    ax1=fig.add_subplot(1,1,1)
    l=len(Data_e)/40.0
    for j in Data_e.index:
        for c in range(len(t_id)):
            if e==t_id[c]:
                ax1.plot(np.array(Otemp[j])+shift*j,Depth_e[j],color='r',linewidth=1)
                ax1.plot(np.array(Dtemp[j])+shift*j,Depth_e[j],color='g',linewidth=1)

        if Depth_e[j][-1]<maxdepth:
            ax1.text(Otemp[j][-1]+shift*j-l,Depth_e[j][-1]+2,round(Otemp[j][-1],1),color='r',fontsize=6)
        else:
            ax1.text(Otemp[j][-1]+shift*j-l,maxdepth,round(Otemp[j][-1],1),color='r',fontsize=6)
       
        if j%2==0:
            ax1.text(Otemp[j][0]+shift*j-l,Depth_e[j][0],round(Otemp[j][0],1),color='k',fontsize=5)
        else:
            ax1.text(Otemp[j][0]+shift*j-l,Depth_e[j][0]-1,round(Otemp[j][0],1),color='k',fontsize=5)
    ax1.set_ylim([maxdepth,-1])
        #plt.setp(ax1.get_xticklabels() ,visible=False)
    ax1.set_xticks([int(Otemp[0][-1]), int(Otemp[0][-1])+shift])
        #ax1.set_xticklabels(['a', 'b', 'c'])
    mintime_e=Time_e[0].strftime('%m-%d-%Y')
    maxtime_e=Time_e[len(Time_e)-1].strftime('%m-%d-%Y')
    if len(Data_e)==1:
        fig.text(0.5, 0.04, 'Temperature '+'C degree', ha='center', va='center', fontsize=14)
    else:
        fig.text(0.5, 0.04, 'Temperature_each profile offset by '+str(shift)+' C degree', ha='center', va='center', fontsize=14)#  0.5 ,0.04 represent the  plotting scale of x_axis and y_axis
    
    if mintime_e==maxtime_e:
        ax1.set_title(str(e) +'_profiles '+mintime_e+' ')    
    else:
        ax1.set_title(str(e) +'_profiles '+mintime_e+'~'+maxtime_e+' ')#('%s profiles(%s~%s)'% (e,obsTime[0],obsTime[-1]))
    fig.text(0.06, 0.5, 'Depth(m)', ha='center', va='center', rotation='vertical',fontsize=14)
    #plt.legend(loc='lower right')
    plt.savefig(path2+'/model_compare/%s_%s~%s.png'% (e,mintime_e,maxtime_e),dpi=200)#put the picture to the file "each_profiles"
    plt.show()
