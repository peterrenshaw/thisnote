#!/usr/bin/env python3

import os
import json
from urllib.request import urlopen

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from font_fredoka_one import FredokaOne

from inky import InkyPHAT


COLOR = "red"
#URL = "http://pi.hole/admin/api.php"
URL = "http://127.0.0.1/admin/api.php"
PATH = os.path.dirname(__file__)
ID = InkyPHAT(COLOR)
MASK = (ID.WHITE,ID.BLACK,ID.RED)


#load image
img = Image.open(os.path.join(PATH, "logo.png"))
draw = ImageDraw.Draw(img)


try:
    print("url <{}>".format(URL))
    data  = urlopen(URL).read()
    js = json.loads(data)
   
    print("data [{}]".format(data))
    print("json <{}>", js)

    ads = js['ads_blocked_today']
    rat = js['ads_percentage_today']

    print("ads ({})".format(ads))
    print("rat ({})".format(rat))
except Error:
   # queries = '?'
    ads = '?'
    rat = '?'
    print("Error: trouble  fetching <{}>".format(u))
    sys.exit(0)


ID.set_border(ID.WHITE)


# Load the FredokaOne font
font = ImageFont.truetype(FredokaOne, 22)

print("ads ({})".format(ads))
ratio = round(rat, 2)
print("rat ({})".format(ratio))

draw.text((20,20), str(ads), ID.BLACK, font)
draw.text((20,50), "{}".format(ratio) + "%", ID.BLACK, font)

ID.set_image(img)
ID.show()



