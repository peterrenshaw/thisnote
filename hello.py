#!/usr/bin/env python3

from inky import InkyPHAT


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from font_fredoka_one import FredokaOne

print("setup")
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

print("PIL draw")
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
print("PIL font")
font = ImageFont.truetype(FredokaOne, 22)

print("create message")
message = "Hello World!"
w,h = font.getsize(message)
x = (inky_display.WIDTH / 2)  - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

print("draw message")
draw.text((x, y), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()
print("done")


