#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:24:00 2020
python2
@author: pengrui
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from turtleModule import str2ndlist
##### SET basic parameters
db= 'tu102' #tu73,tu74,tu94,tu98,tu99,tu102
path1='/home/zdong/PENGRUI/merge_nosplit/'
path2='/home/zdong/PENGRUI/'
start_time = datetime(2019,7,10).strftime('%m-%d-%Y') 
end_time = datetime(2019,7,20).strftime('%m-%d-%Y')   # create a forder named by 'IOError'


color=['g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate']
shift = 4 # offset of profiles in degC
maxdepth = 60 # maximum depth of profile plot
t_ids=[118940, 118941, 118944, 118947, 118948, 118951, 118943, 118945,118946, 118942, 118952, 118949, 118950, 118953, 118954, #tu_73
       118884, 118894, 118896, 118885, 118887, 118888, 118889, 118890,118886, 118891, 118893, 118892, 118899, 118901, 118903, 118897,118898, 118900, 118902, 118895, 118906, 118905, 118904, 118913, #tu74
       118905, 149443, 149448, 149449, 149445, 149446, 149447, 151557,151558, 151561, 149450, 151559, 151560,  #tu94
       159795, 159796, 159797, 161305, 161444, 161868, 161293, 161302,161441, 161443, 172178, 172180, 172184, 161442, 161445, 172193,172181, 172189, 172177, 172182, 172183, 172185, 172186, 172187,172190, 172192, 172194, 172196, #tu98
       161426, 161427, 161428, 161432, 161433, 161435, 161429, 161436,161437, 161430, 161434, 161439, 161431, 161438, 161440, #tu_99
       161291, 161292, 161296, 172191, 175934, 175935, 161295, 175939,161299, 161303, 161294, 161297, 161298, 161300, 161301, 161304,172179, 172188, 175938, 175932, 175936, 175940] #tu_102

obsData =pd.read_csv('tu102_adapt.csv') #
obsturtle_id=obsData['PTT']
ids=obsturtle_id.unique()#118905 # this is the interest turtle id

Time = pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in obsData['argos_date']))
#indx=np.where((Time>=end_time-timedelta(days=7)) & (Time<end_time))[0]
indx=np.where((Time>=start_time) & (Time<=end_time))[0]
time=Time[indx]
time.sort()

Data = obsData.ix[time.index]
Data.index=range(len(indx))
obsTime =  pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in Data['argos_date']))
obsTemp = pd.Series(str2ndlist(Data['obs_temp']))
dopTemp = pd.Series(str2ndlist(Data['doppio_temp']))
obsDepth = pd.Series(str2ndlist(Data['depth']))
obsID = Data['PTT']
obsIDs=obsID.unique()

mintime=obsTime[0].strftime('%m-%d-%Y')
maxtime=obsTime[len(obsTime)-1].strftime('%m-%d-%Y')


month,day=[],[]
for d in obsTime.index:
    day.append(obsTime[d].day)
    month.append(obsTime[d].month)    

#####  plot all turtles during selected days          
m=int(len(Data)/2)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
for j in range(0,m):
    for i in range(len(t_ids)):       
        if obsID[j]==t_ids[i]:  # to give the different color line for each turtle
            ax1.plot(np.array(obsTemp[j])+shift*j,obsDepth[j],color=color[i],linewidth=1)#,label='id:'+str(obsID[j]))
            ax1.plot(np.array(dopTemp[j])+shift*j,obsDepth[j],linestyle='--',color=color[i],linewidth=1)
            '''
            if obsDepth[j][-1]<maxdepth:
                ax1.text(obsTemp[j][-1]+shift*j-1,obsDepth[j][-1]+1,round(obsTemp[j][-1],1),color='r',fontsize=5)
                #ax1.text(dopTemp[j][-1]+shift*j-1,obsDepth[j][-1]+1,str(month[j])+'/'+str(day[j]),color='g',fontsize=5)
            else:
                ax1.text(obsTemp[j][-1]+shift*j-1,maxdepth,str(month[j])+'/'+str(day[j]),color=color[i],fontsize=5)
            if j%2==0:
                ax1.text(obsTemp[j][0]+shift*j-1,obsDepth[j][0],round(obsTemp[j][0],1),color='r',fontsize=5)
                #ax1.text(obsTemp[j][0]+shift*j-1,obsDepth[j][0],round(obsTemp[j][0],1),color='g',fontsize=5)
            else:
                ax1.text(obsTemp[j][0]+shift*j-1,obsDepth[j][0]-1,round(obsTemp[j][0],1),color='r',fontsize=5)
                #ax1.text(obsTemp[j][0]+shift*j-1,dopDepth[j][0]-1,round(obsTemp[j][0],1),color='g',fontsize=5)
            '''
ax1.set_ylim([maxdepth,-1])
ax1.set_xticks([int(obsTemp[0][-1]), int(obsTemp[0][-1])+shift])
            #plt.setp(ax1.get_xticklabels() ,visible=False)
ax2=fig.add_subplot(2,1,2)
for k in range(m,len(Data)):    
    for i in range(len(t_ids)):       
        if obsID[k]==t_ids[i]:  # to give the different color line for each turtle
            ax2.plot(np.array(obsTemp[k])+shift*(k-m),obsDepth[k],color=color[i],linewidth=1)#,label='id:'+str(obsID[j])
            ax2.plot(np.array(dopTemp[k])+shift*(k-m),obsDepth[k],linestyle='--',color=color[i],linewidth=1)
            '''
            if obsDepth[k][-1]<maxdepth:
                ax2.text(obsTemp[k][-1]+shift*(k-m)-1,obsDepth[k][-1]+1,round(obsTemp[k][-1],1),color='r',fontsize=7)
                #ax2.text(dopTemp[k][-1]+shift*(k-m)-1,obsDepth[k][-1]+1,str(month[k])+'/'+str(day[k]),color=color[i],fontsize=7)
            else:
                ax2.text(obsTemp[k][-1]+shift*(k-m)-1,maxdepth,str(month[k])+'/'+str(day[k]),color='r',fontsize=5)
            if k%2==0:
                ax2.text(obsTemp[k][0]+shift*(k-m)-1,obsDepth[k][0],round(obsTemp[k][0],1),color='r',fontsize=5)
                #ax2.text(dopTemp[k][0]+shift*(k-m)-1,obsDepth[k][0],round(obsTemp[k][0],1),color=color[i],fontsize=5)
            else:
                ax2.text(obsTemp[k][0]+shift*(k-m)-1,obsDepth[k][0]-1,round(obsTemp[k][0],1),color='r',fontsize=5)
                #ax2.text(dopTemp[k][0]+shift*(k-m)-1,obsDepth[k][0]-1,round(obsTemp[k][0],1),color=color[i],fontsize=5)
            '''
ax2.set_ylim([maxdepth,-1])
ax2.set_xticks([int(obsTemp[m][-1]), int(obsTemp[m][-1])+shift])
#plt.setp(ax2.get_xticklabels() ,visible=False)
middletime=obsTime[m].strftime('%m-%d-%Y')        
ax1.set_title('profiles color-coded-by-turtle during '+mintime+' ~ '+middletime )#('%s profiles(%s~%s)'% (e,obsTime[0],obsTime[-1]))
ax2.set_title(middletime+' ~ '+maxtime)
fig.text(0.5, 0.04, 'Temperature by time '+str(shift)+' C degree offset', ha='center', va='center', fontsize=14)#  0.5 ,0.04 represent the  plotting scale of x_axis and y_axis
fig.text(0.06, 0.5, 'Depth(m)', ha='center', va='center', rotation='vertical',fontsize=14)

#plt.savefig(path2+'/model_compare/compare_%s~%s.png'%(mintime,maxtime),dpi=200)#put the picture to the file"turtle_comparison"
plt.show()

##### plot profile of each turtle
for i in range(len(obsIDs)):
    e=obsIDs[i]
    indx=[]  
    for i in Data.index:
        if obsID[i]==e:   
            indx.append(i)
    Data_e = Data.ix[indx]  
    Data_e.index= range(len(indx))             
    Time_e= pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in Data_e['argos_date']))
    Temp_obs = pd.Series(str2ndlist(Data_e['obs_temp']))
    Temp_dop = pd.Series(str2ndlist(Data_e['doppio_temp']))
    Depth_e = pd.Series(str2ndlist(Data_e['depth']))
    
    fig=plt.figure()
    ax1=fig.add_subplot(1,1,1)
    l=len(Data_e)/40.0
    for j in Data_e.index:
        for c in range(len(t_ids)):
            if e==t_ids[c]:
               ax1.plot(np.array(Temp_obs[j])+shift*j,Depth_e[j],color='blue',linewidth=1)
               ax1.plot(np.array(Temp_dop[j])+shift*j,Depth_e[j],color='orangered',linewidth=1)
        if Depth_e[j][-1]<maxdepth:
            ax1.text(Temp_obs[j][-1]+shift*j-l,Depth_e[j][-1]+2,round(Temp_obs[j][-1],1),color='r',fontsize=6)
        else:
            ax1.text(Temp_obs[j][-1]+shift*j-l,maxdepth,round(Temp_obs[j][-1],1),color='r',fontsize=6)
        if j%2==0:
            ax1.text(Temp_obs[j][0]+shift*j-l,Depth_e[j][0],round(Temp_obs[j][0],1),color='k',fontsize=5)
        else:
            ax1.text(Temp_obs[j][0]+shift*j-l,Depth_e[j][0]-1,round(Temp_obs[j][0],1),color='k',fontsize=5)
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
    #plt.savefig(path2+'per_turtle_period/%s~%s/%s_%s~%s.png'% (mintime,maxtime,e,mintime,maxtime),dpi=200)#put the picture to the file "each_profiles"
    plt.show()
