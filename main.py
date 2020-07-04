#!/usr/bin/env python3


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
from time import gmtime, strftime


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from font_fredoka_one import FredokaOne


from inky import InkyPHAT


DEBUG = False
get_dt = strftime("%b%d", gmtime())
DT = "{}".format(get_dt).upper()
COLOR = "red"
URL = "http://127.0.0.1/admin/api.php"
PATH = os.path.dirname(__file__)
ID = InkyPHAT(COLOR)
MASK = (ID.WHITE,ID.BLACK,ID.RED)


def debug(s, is_debug=DEBUG):
    """show the debug message if is_debug T"""
    if s: 
        if is_debug: print("> ".format(s))
        else: pass
    else:
        pass


#load image
img = Image.open(os.path.join(PATH, "logo.png"))
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
    print("Error: trouble  fetching <{}>".format(u))
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


# eof
