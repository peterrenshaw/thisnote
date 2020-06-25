#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DEBUG = True


import os
import json
import urllib.request


from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw


#
# display: show debug messages
#
def display(msg, is_debug=DEBUG):
    """debug message shows if is_debug is True"""
    is_debug: print(">>> {}".format(msg))

display("starting")

# set current directory
display("set current directory")
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# load graphics
display("load graphics")
img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)


# get api data
display("get api data")
try:
    f = urllib.request.urlopen("http://192.168.0.39/admin/api.php")
    json_string = f.read()
    parsed_json = json.loads(json_string)
    adsblocked = parsed_json["ads_percentage_today"]
    ratioblocked = parsed_json["ads_percentage_today"]
    f.close()
    display("api data ok")
except:
    queries = '?'
    adsblocked = '?'
    ratioblocked = 0
    ratio = '?'
    display("api data fail")

#
# inkyPHAT setup
#
display("inkyPHAT setup")

font = ImageFont.truetype(os.path.join("ttf", "BebasNeue-Regular.ttf"), 32)
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)


# 
# inkyPHAT draw
#
display("inkyPHAT draw")
draw.text((20, 20), str(adsblocked), inky_display.BLACK, font)
draw.text((20, 50), str("%.1f" % round(ratioblocked, 2) + "%", inky_display.BLACK, font))

display("inkyPHAT display")
ink_display.set_image(img)
inky_display.show()


# eof








