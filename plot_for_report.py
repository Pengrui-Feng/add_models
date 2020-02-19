#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:24:00 2020
python2
plot special data for reporting
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
start_time = datetime(2018,4,1).strftime('%m-%d-%Y') 
#end_time = datetime(2019,8,14).strftime('%m-%d-%Y')   # create a forder named by 'IOError'


color=['g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate',
'g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate']
shift = 12 # offset of profiles in degC
maxdepth = 200 # maximum depth of profile plot
t_ids=[118940, 118941, 118944, 118947, 118948, 118951, 118943, 118945,118946, 118942, 118952, 118949, 118950, 118953, 118954, #tu_73
       118884, 118894, 118896, 118885, 118887, 118888, 118889, 118890,118886, 118891, 118893, 118892, 118899, 118901, 118903, 118897,118898, 118900, 118902, 118895, 118906, 118905, 118904, 118913, #tu74
       118905, 149443, 149448, 149449, 149445, 149446, 149447, 151557,151558, 151561, 149450, 151559, 151560,  #tu94
       159795, 159796, 159797, 161305, 161444, 161868, 161293, 161302,161441, 161443, 172178, 172180, 172184, 161442, 161445, 172193,172181, 172189, 172177, 172182, 172183, 172185, 172186, 172187,172190, 172192, 172194, 172196, #tu98
       161426, 161427, 161428, 161432, 161433, 161435, 161429, 161436,161437, 161430, 161434, 161439, 161431, 161438, 161440, #tu_99
       161291, 161292, 161296, 172191, 175934, 175935, 161295, 175939,161299, 161303, 161294, 161297, 161298, 161300, 161301, 161304,172179, 172188, 175938, 175932, 175936, 175940] #tu_102

#data = pd.read_csv(path2+db+'withModelsold.csv')
data = pd.read_csv(path2+'tu102withfModels.csv')
data = data.dropna()
#dive = data['dive_num']
data['obs_temp']=data['obs_temp']*1.8+30
data['doppio_temp']=data['doppio_temp']*1.8+30
data['FVCOM_temp']=data['FVCOM_temp']*1.8+30
data['depth']= data['depth']*3.280839895
data['obs_temp'] = data['obs_temp'].astype('str')
data['doppio_temp']= data['doppio_temp'].astype('str')
data['FVCOM_temp']= data['FVCOM_temp'].astype('str')
data['depth']= data['depth'].astype('str')

#data1=data.groupby(['PTT','dive_num','argos_date','lat_argos','lon_argos','gps_date','lat_gps','lon_gps']).agg(lambda x:x.str.cat(sep=','))
data1=data.groupby(['PTT','argos_date'])['depth','obs_temp','doppio_temp','FVCOM_temp'].agg(lambda x:x.str.cat(sep=','))
#data1.to_csv('tu102_adapt.csv')
data1.to_csv('special_combine.csv')
obsData =pd.read_csv('special_combine.csv') #
obsturtle_id=obsData['PTT']
ids=obsturtle_id.unique()#118905 # this is the interest turtle id

Time = pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in obsData['argos_date']))
#indx=np.where((Time>=end_time-timedelta(days=7)) & (Time<end_time))[0]
indx=np.where((Time>=start_time))[0]
time=Time[indx]
time.sort()

Data = obsData.ix[time.index[0:8]]
Data.index=range(8)
obsTime =  pd.Series((datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in Data['argos_date']))
obsTemp = pd.Series(str2ndlist(Data['obs_temp']))
dopTemp = pd.Series(str2ndlist(Data['doppio_temp']))
fvcTemp = pd.Series(str2ndlist(Data['FVCOM_temp']))
obsDepth = pd.Series(str2ndlist(Data['depth']))
obsID = Data['PTT']
obsIDs=obsID.unique()

mintime=obsTime[0].strftime('%m-%d-%Y')
maxtime=obsTime[len(obsTime)-1].strftime('%m-%d-%Y')


year,month,day=[],[],[]
for d in obsTime.index:
    day.append(obsTime[d].day)
    month.append(obsTime[d].month)    
    year.append(obsTime[d].year)
#####  plot all turtles during selected days          
m=int(len(Data)/8)
fig=plt.figure()
for n in range(8):
    ax=fig.add_subplot(2,4,n+1)
    for j in range(n*m,n*m+m):
        for i in range(len(t_ids)):       
            if obsID[j]==t_ids[i]:  # to give the different color line for each turtle
                ax.plot(np.array(obsTemp[j]),obsDepth[j],color=color[i],linewidth=3)#,label='id:'+str(obsID[j]))
                ax.plot(np.array(dopTemp[j]),obsDepth[j],linestyle='--',color=color[i],linewidth=3)
                ax.plot(np.array(fvcTemp[j]),obsDepth[j],linestyle=':',color=color[i],linewidth=3)        
                
                ax.text(obsTemp[j][-1]-6,obsDepth[j][-1]+3,round(obsTemp[j][-1],1),color='r',fontsize=10)                
                ax.text(dopTemp[j][-1]+1,obsDepth[j][-1]+3,round(dopTemp[j][-1],1),color='g',fontsize=10)                              
                
                ax.text(obsTemp[j][0]-8,obsDepth[j][0]-1,round(obsTemp[j][0],1),color='r',fontsize=10)
                ax.text(dopTemp[j][0]-2,obsDepth[j][0]-1,round(dopTemp[j][0],1),color='g',fontsize=10)

    time=obsTime[n].strftime('%m-%d-%Y')           
    ax.set_ylim([maxdepth,-10])
    ax.set_xticks([int(obsTemp[n][-1]-6), int(dopTemp[n][0])+5])
    ax.text(57, 195,'%s'%time,ha='center', va='center',color='black',fontsize=10)
    plt.setp(ax.get_xticklabels() ,visible=False)
    if n!=0 and n!=4:
        plt.setp(ax.get_yticklabels() ,visible=False)
        ax.spines['left'].set_visible(False)
    #ax.axis('off')
    if n !=3 and n != 7 :
        ax.spines['right'].set_visible(False)
#plt.setp(ax2.get_xticklabels() ,visible=False)
middletime=obsTime[m].strftime('%m-%d-%Y')        
#ax.set_title('profiles color-coded-by-turtle during '+mintime+' ~ '+maxtime )#('%s profiles(%s~%s)'% (e,obsTime[0],obsTime[-1]))
#ax.set_title(middletime+' ~ '+maxtime)
fig.text(0.5, 0.05, 'Turtle(red_label) & Model(green_label) Temperature(degF)', ha='center', va='center', fontsize=14)#  0.5 ,0.04 represent the  plotting scale of x_axis and y_axis
fig.text(0.5, 0.95, 'Turtle(solid) & Model(dash) Profile', ha='center', va='center', fontsize=14)
fig.text(0.06, 0.5, 'Depth(Ft)', ha='center', va='center', rotation='vertical',fontsize=14)
plt.subplots_adjust(wspace =0, hspace =0.05)
#plt.savefig(path2+'/model_compare/compare_profile.png',dpi=200)#put the picture to the file"turtle_comparison"
plt.show()

