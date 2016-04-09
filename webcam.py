#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import cv2
import cv2.cv as cv
import pygame
from datetime import datetime
import time
import os
import sys

outfile = "/home/agrover/Desktop/camera.jpg"
prevent_file = "/home/agrover/cam_ok"
warning_sound = "/home/agrover/git/pysnapper/4321.wav"
scp_path = "ca-server1:public_html"

font = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
font_size = 24

try:
    os.stat(prevent_file)
except OSError:
    sys.exit(-1)

pygame.init()
sound = pygame.mixer.Sound(warning_sound)
sound.set_volume(0.4)
sound.play()
time.sleep(4)

camera = cv.CaptureFromCAM(1)
ipl = cv.QueryFrame(camera)
im = Image.frombytes("RGB", cv.GetSize(ipl), ipl.tostring())

now = datetime.now()
date_str = now.ctime()

draw = ImageDraw.Draw(im)
draw_font = ImageFont.truetype(font, font_size)
draw.text((10,10), date_str, font=draw_font)

im.save(outfile, "JPEG")

# os.system("scp %s %s" % (outfile, scp_path))
