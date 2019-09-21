# Author: Pietro Malky
# Date: 09/20/2019
# Purpose: Extract color pallets from Images

'''
Ideas

Resize Images to w*h = 200*h
Declare Set object to hold colors
Add colors to Set object and save Set to disk
Create Pallette Image from Set object and save to disk
'''

import json
import math
import numpy as np
from PIL import Image
from pprint import pprint


def getClosestFactors(n):
    factors = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            factors.append((i, int(n/i)))

    closestFactors = (99999999, 0)
    for f in factors:
        if abs(f[0] - f[1]) < abs(closestFactors[0] - closestFactors[1]):
            closestFactors = f
    return closestFactors


inPath = "../inputImages/roads.png"
outPath = "../outputImages/palette.png"

# define base width constant for new image
BASE_WIDTH = 200

# open input image
img = Image.open(inPath)

# calculate width percent and new height
widthPercent = BASE_WIDTH/float(img.size[0])
newHeight = int(float(img.size[1]*float(widthPercent)))

# re-size image
img = img.resize((BASE_WIDTH, newHeight), Image.ANTIALIAS)

# declare colors set to hold palette
colorPalette = set()

# turn resized image to numpy array
imgArr = np.array(img)

# traverse img array and add colors to set
for row in imgArr:
    for pixel in row:
        pixel = tuple(pixel)
        colorPalette.add(pixel)


colors = len(colorPalette)
cf = (*getClosestFactors(colors), 4)
colorPalette = list(colorPalette)
colorPalette = sorted(colorPalette, key=lambda c: sum(c[:2])/3, reverse=True)


newImg = np.array(colorPalette).reshape(cf)
newImg = Image.fromarray(newImg)
newImg.save(outPath)
