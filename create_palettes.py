import numpy as np
import palettable
import matplotlib
from PIL import Image, ImageOps, ImageChops, ImageStat, ImageDraw
import os
from math import floor
import json
import requests
from collections import Counter
import pickle

import lzma

def get_instagram_url(fn):
    j = json.loads(lzma.open(fn.replace(".jpg",".json.xz")).read().decode("utf-8")).get('node', {})
    return f"https://instagram.com/p/{j.get('shortcode')}/"

def mic_url(url):
    sections = url.split("_")
    uid = sections[2]
    return f"https://moviesincolor.com/post/{uid}"

def iframely_url(url):
    sections = url.split("_")
    uid = sections[2]
    return f"https://iframely.com/api/try?url=https://moviesincolor.com/post/{uid}"

def make_filename(filename):
    keepcharacters = ('(',')','_')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()

def show_key_colors(colorList):
    '''
    Make a long rectangle, composed of the colors
    detailed in colorList, a list of (R, G, B) tuples
    '''
    n = len(colorList)
    if n > 0:
      im = Image.new('RGB', (50*n, 50))
      draw = ImageDraw.Draw(im)

      for idx, color in enumerate(colorList):
          color = tuple([int(x) for x in color])
          print(color)
          draw.rectangle([(50*idx, 0), (50*(idx+1), 50*(idx+1))],
                        fill=tuple(color))
    else:
        im = Image.new('RGB', (1,1))

    return im

# MoviesInColor.com images to palettes 
def get_palette(img):
    upper = []
    lower = []
    if img.size == (1280, 772):
        upper_y = 608
        lower_y = 720
        x = 54
    else:
        upper_y = 414
        lower_y = 488
        x = 36
    for i in range(1,24):
        upper_pixel = img.getpixel((i*x, upper_y))
        upper.append(upper_pixel)
        lower_pixel = img.getpixel((i*x, lower_y))
        lower.append(lower_pixel)
        
    return (upper[0:6], upper[8:14], upper[16:22], lower[1:22])

def get_palette_cp(img):
    try:
        upper = []
        offset = 0
        ncolors = 10
        #lower = []
        w, h = img.size
        y = h - 120
        if h < 900:
            x = 100
        elif h < 1000:
            offset = 0
            x = 115
            ncolors = 9
        else:
            offset = -50
            x = 120
            ncolors = 9

        for i in range(1,ncolors+1):
            pixel = img.getpixel((offset+i*x, y))
            upper.append(pixel)
            #lower_pixel = img.getpixel((i*x, lower_y))
            #lower.append(lower_pixel)
    except:
        print(f"Problem with {img}")
        
    return upper

# filmandcolor
def get_palette_fc(img):
    try:
        upper = []
        offset = 0
        ncolors = 13
        #lower = []
        w, h = img.size
        y = 800
        x = 77
        offset = -35

        for i in range(1,ncolors+1):
            pixel = img.getpixel((offset+i*x, y))
            upper.append(pixel)
            #lower_pixel = img.getpixel((i*x, lower_y))
            #lower.append(lower_pixel)
    except:
        print(f"Problem with {img}")
        
    return upper

# palettemaniac
def get_palette_pm(img):
    try:
        upper = []
        offset = 0
        ncolors = 10
        #lower = []
        w, h = img.size
        y = 660
        x = 108
        if w < 1000:
            x = 96
        offset = -50

        for i in range(1,ncolors+1):
            pixel = img.getpixel((offset+i*x, y))
            upper.append(pixel)
            #lower_pixel = img.getpixel((i*x, lower_y))
            #lower.append(lower_pixel)
    except:
        print(f"Problem with {img}")
        
    return upper