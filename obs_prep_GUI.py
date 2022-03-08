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


# Functions
def clear():
    e.delete(0,END)

def set_longitude():
    longitude=e.get() 
    with open('data123.txt','a') as f:
        f.write(longitude)
        f.write('\n')

def set_latitude():
    latitude=e.get() 
    with open('data123.txt','a') as f:
        f.write(latitude)
        f.write('\n')
        
def set_elevation():
    elevation=e.get()
    with open('data123.txt','a') as f:
        f.write(elevation)
        f.write('\n')
        


root = Tk()
root.configure(background="grey")
root.geometry("600x500")
time_now=Time.now()
download_IERS_A()

with open('data123.txt','a') as f:
    f.write(str(time_now)+'\n')


# Buttons, Fonts
Font_tuple = ("Comic Sans MS", 15, "bold")


e = Entry(root,background="grey",fg="white",font=Font_tuple,width=40)
clear_button = Button(root, text="Clear",command=clear)
set_longitude= Button(root, text="Set Longitude",command=set_longitude)
set_latitude= Button(root, text="Set Latitude",command=set_latitude)
set_elevation= Button(root,text="Set Elevation",command=set_elevation)


# Element coordinates
e.place(x=25, y=10)
clear_button.place(x=25, y=75)
set_longitude.place(x=70,y=75)
set_latitude.place(x=160,y=75)
set_elevation.place(x=240,y=75)

root.mainloop()
