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

##### SET basic parameters
db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/home/zdong/PENGRUI/merge/'
path2='/home/zdong/PENGRUI/'
start_time = datetime(2018,8,1).strftime('%m-%d-%Y') 
end_time = datetime(2018,10,29).strftime('%m-%d-%Y')   # create a forder named by 'IOError'

#
data = pd.read_csv(path2+db+'withModels.csv')
turtle_id=data['PTT']
dive = data['dive_num']
Temp = data['obs_temp']
Depth = data['depth']



fig=plt.figure()

for i in range(0,12):
    temp=[]
    depth=[]
    for j in range(15):
        if dive[j+1]==dive[j]:
            temp.append(Temp[i+j])        
            depth.append(Depth[i+j])
    
    plt.plot(temp+shift*i,depth,color=color[c],linewidth=1)
    #plt.plot(temp,depth)
plt.show()
'''        
    e=obsIDs[i]
    indx=[]  
    for i in Data.index:
        if obsID[i]==e:   
            indx.append(i)
    Data_e = Data.ix[indx]  
    Data_e.index= range(len(indx))             
    Time_e= pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in Data_e['argos_date']))
    Temp_e = pd.Series(str2ndlist(Data_e['temp']))
    Depth_e = pd.Series(str2ndlist(Data_e['depth']))
    
    fig=plt.figure()
    ax1=fig.add_subplot(1,1,1)
    l=len(Data_e)/40.0
    for j in Data_e.index:
        
        for c in range(len(t_ids)):
            if e==t_ids[c]:
               ax1.plot(np.array(Temp_e[j])+shift*j,Depth_e[j],color=color[c],linewidth=1)
        if Depth_e[j][-1]<maxdepth:
            ax1.text(Temp_e[j][-1]+shift*j-l,Depth_e[j][-1]+2,round(Temp_e[j][-1],1),color='r',fontsize=6)
        else:
            ax1.text(Temp_e[j][-1]+shift*j-l,maxdepth,round(Temp_e[j][-1],1),color='r',fontsize=6)
        if j%2==0:
            ax1.text(Temp_e[j][0]+shift*j-l,Depth_e[j][0],round(Temp_e[j][0],1),color='k',fontsize=5)
        else:
            ax1.text(Temp_e[j][0]+shift*j-l,Depth_e[j][0]-1,round(Temp_e[j][0],1),color='k',fontsize=5)
    ax1.set_ylim([maxdepth,-1])
        #plt.setp(ax1.get_xticklabels() ,visible=False)
    ax1.set_xticks([int(Temp_e[0][-1]), int(Temp_e[0][-1])+shift])
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
    plt.savefig(path2+'per_turtle_period/%s~%s/%s_%s~%s.png'% (mintime,maxtime,e,mintime,maxtime),dpi=200)#put the picture to the file "each_profiles"
    plt.show()
'''