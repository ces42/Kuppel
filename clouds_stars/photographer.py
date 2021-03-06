#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Name:       photographer
# Purpose:    
# Created:    21.10.16
from clouds_stars.stars import clouded

__author__ = 'Carlos Esparza-Sanchez'
#-------------------------------------------------------------------------------

from stars import *
import picamera
from time import sleep, time
from io import BytesIO
import PIL.Image as im

camera = picamera.PiCamera()

# einstellungen für Photographie mit wenig Licht
camera.framerate = 1/4
camera.shutter_speed = 4000000
camera.exposure_mode = 'off'
camera.iso = 600

T = 1.0 # Zeitintervall, in dem Bilder gemacht werden


while True: #TODO: hier sollten wir vielleicht Uhrzeiten abfragen
    stream = BytesIO() # wir emulieren eine Datei
    t = time()

    camera.capture(stream) # Photo schießen
    image = im.open(stream.getvalue())
    print(clouded(image))

    sleep(T + t - time()) # jeder Durchgang der Schleife soll  T minuten dauern



