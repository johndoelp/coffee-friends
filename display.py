#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import Pimoroni Inky wHAT Large e-Ink Display (Red/Black/White)
#https://shop.pimoroni.com/products/inky-what?variant=13590497624147
from inky.auto import auto
inky_display = auto()

#import Pillow (https://pypi.org/project/Pillow/) to resize/edit/etc image file if needed
from PIL import Image, ImageFont, ImageDraw

#determine which wHAT is in use & set border color
inky_display = auto(ask_user=True, verbose=True)
inky_display.set_border(inky_display.WHITE)

#determine px Height & Width of wHAT
w = inky_display.width
h = inky_display.height

#import date & sleep for stand-in refresh rate
import datetime
import time

date = datetime.today()

print("one")

#count up from 0 -> 5
pausecount = 0
while pausecount < 5:
    print(pausecount)
    pausecount += 1
    time.sleep(1)

print(date)