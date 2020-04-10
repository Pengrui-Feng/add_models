import netCDF4
import numpy as np
from datetime import datetime
from get_espresso_model import*
#get the same temp no matter what the depth
#the data duration offunction 'get_espresso_temp1' from 2009-10-12 to 2017-1-1
#the data duration offunction 'get_espresso_temp' from 2009-10-12 to 2013-5-18
time= datetime(2012,3,5)
lat,lon= 39 , -70
depth = 20


temp = get_espresso_temp(time,lat,lon,depth)
print(temp)

