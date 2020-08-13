#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~


#    ________ __________  _  ______  __________
#   /_  __/ // /  _/ __/ / |/ / __ \/_  __/ __/
#    / / / _  // /_\ \  /    / /_/ / / / / _/  
#   /_/ /_//_/___/___/ /_/|_/\____/ /_/ /___/  
#


import time
import datetime
from time import strftime


H = "%H"
HHMM = "%H%M"
MMMDD = "%b%d"


# ---- datetime start -----
def dt_get_now():
    """determine the current LOCALTIME"""
    now = datetime.datetime.now()
    return now

def dt_get_hour(now, hour=H):
    """determine hour in strformat, return as integer"""
    h = now.strftime(H)
    return int(h)

def dt_get_hour_minute(now, hm=HHMM):
    """determine the time with supplied strf format"""
    hourminute = "{}".format(now.strftime(hm))
    return hourminute 

def dt_get_month_day(now, md=MMMDD):
    """determine the Month and day with supplied strf format"""
    monthday = "{}".format(now.strftime(md).upper())
    return monthday
# ---- datetime end -----


#
# dt_get_watch: logic for determining quarter watch. 
#               pass in a 24 H time, cast to integer 
#               returns the watch number from 1 to 4.
#
#    input : hh as 24 hour number, cast as integer
#    output: 1, 2, 3, 4 integer depending on hours  
#          
#    Watch  i24   24 Hour
#    1       0    0000 - 0600   
#    2       6    0600 - 1200
#    3      12    1200 - 2100
#    4      21    2100 - 0000
#
def dt_get_watch(hh):
    """determine the WATCH number from hours in current 24 hour format"""
    if hh >= 0 and hh <= 6:
        # between zero hour and 0600
        return 1
    elif hh > 6 and hh <= 12:
        # between 0600 and 1200
        return 2
    elif hh > 12 and hh <= 21:
        # between 1200 and 2100
        return 3
    else:
        # after 2100, before zero hour
        return 4

def dsp_output(n):
    """display simple output for testing"""
    print("{}/{}".format(dt_get_month_day(n), dt_get_hour_minute(n)))

def dsp_current(n):
    """display simple current hour, watch for testing"""
    hour = dt_get_hour(n)
    print("n is {}".format(n))
    print("hour is {}".format(hour))

    watch = dt_get_watch(hour)
    print("The current watch is {}".format(watch))


if __name__ == "__main__":
    pass


# eof
