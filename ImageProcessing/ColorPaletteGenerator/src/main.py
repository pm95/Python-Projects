# Author: Pietro Malky
# Date: 09/20/2019
# Purpose: Extract color pallets from Images

'''
Ideas

Resize input image
Declare Set object to hold colors
Add colors to Set object and save Set to disk
Create Pallette Image from Set object and save to disk
'''

import math
import sys
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


name = sys.argv[1]
inPath = "../inputImages/%s.png" % name
outPath = "../outputImages/%s_palette.png" % name

# define base width constant for new image
NEW_WIDTH = 50

# open input image
img = Image.open(inPath)

# calculate width percent and new height
widthPercent = NEW_WIDTH/float(img.size[0])
# NEW_HEIGHT = int(float(img.size[1]*float(widthPercent)))
NEW_HEIGHT = NEW_WIDTH

# re-size image
img = img.resize((NEW_WIDTH, NEW_HEIGHT), Image.ANTIALIAS)

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
colorPalette = sorted(colorPalette, key=lambda c: c, reverse=True)


# divide color palette list into specified number of segments
segments = 8  # 8 seems to be most reasonable segmentation value
simplePalette = []
for i in range(0, len(colorPalette), int(len(colorPalette)/segments)):
    simplePalette.append(colorPalette[i])

# create new image array and then image from array
newImg = np.array(simplePalette).reshape(len(simplePalette), 1, 4)
newImg = np.tile(newImg, (len(simplePalette), 1))
newImg = Image.fromarray(newImg)
newImg = newImg.resize((500, 500))
newImg.save(outPath)
