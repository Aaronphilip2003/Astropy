from time import time, time_ns
import numpy as np
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
import pytz
from astroplan import Observer, FixedTarget
from astropy.utils.iers import conf
conf.auto_max_age = None
from astroplan import download_IERS_A
from astropy.coordinates import get_sun, get_moon, get_body
from astroplan import moon_illumination
from tkinter import *
import numpy as np
from astropy.time import Time   

data=[]

lines = []
with open('data123.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    data.append(line)
    
print(data)

# t = Time(data[0], format='iso', scale='utc') isot is another date format

# longitude=data[1]
# latitude=data[2]
# elevation=int(data[3]) * u.m

# print(elevation)

# # location=EarthLocation(longitude,latitude,elevation)
# # ioMIT=Observer(location=location,timezone='Asia/Kolkata',
# #                name='MIT-Telescope',description="GSO-Newtonian Telescope MIT World Peace University")
# # print(location)
