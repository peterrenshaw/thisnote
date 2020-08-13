#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#    ________ __________  _  ______  __________
#   /_  __/ // /  _/ __/ / |/ / __ \/_  __/ __/
#    / / / _  // /_\ \  /    / /_/ / / / / _/  
#   /_/ /_//_/___/___/ /_/|_/\____/ /_/ /___/  
#


#
# name: report.py
# date: 2020JUL04
# prog: pr
# desc: A simple pihole hack to display
#       to show number of ADVERTS blocked
#       and how many as % today.
# sorc: Inspired and totally ripped off the 
#       fantastic inky-hole 
#       <https://github.com.cnpmjs.org/neauoire/inky-hole>
#


import os
import json
from urllib.request import urlopen


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from font_fredoka_one import FredokaOne


from inky import InkyPHAT


from tools import dt_get_now
from tools import dt_get_hour
from tools import dt_get_watch
from tools import dt_get_month_day


#
# Setup  globals
#

DEBUG = False
COLOR = "red"
URL = "http://127.0.0.1/admin/api.php"
PATH = os.path.join(os.path.dirname(__file__), "img")
NOW = dt_get_now()
FN_NEEK = "logoneek.png"

get_dt = dt_get_month_day(NOW)
DT = "{}".format(get_dt).upper()
ID = InkyPHAT(COLOR)


def debug(s, is_debug=DEBUG):
    """show the debug message if is_debug T"""
    if s: 
        if is_debug: print("> ".format(s))
        else: pass
    else:
        pass

def main():
    """main entry point"""

    # determine watch
    hour = dt_get_hour(NOW)
    wn =dt_get_watch(hour)
    
    # generate image to get
    fn = "{}-{}".format(wn, FN_NEEK)

    #load current image for this watch
    img = Image.open(os.path.join(PATH, fn))
    draw = ImageDraw.Draw(img)


    try:
        debug("url <{}>".format(URL))
        data  = urlopen(URL).read()
        js = json.loads(data)
   
        debug("data [{}]".format(data))
        debug("json <{}>".format(js))

        ads = js['ads_blocked_today']
        rat = js['ads_percentage_today']

        debug("ads ({})".format(ads))
        debug("rat ({})".format(rat))
    except Error:
        print("Error: ♬ This note, this note is for you ♬ ...Trouble fetching <{}>".format(u))
        sys.exit(0)


    ID.set_border(ID.WHITE)


    # Load the FredokaOne font
    font = ImageFont.truetype(FredokaOne, 22)

    debug("ads ({})".format(ads))
    ratio = round(rat, 1)
    debug("rat ({})".format(ratio))

    draw.text((20,10), DT, ID.RED, font)
    draw.text((20,35), str(ads), ID.BLACK, font)
    draw.text((20,60), "{}".format(ratio) + "%", ID.BLACK, font)

    ID.set_image(img)
    ID.show()


if __name__ == "__main__":
    main()


# eof
