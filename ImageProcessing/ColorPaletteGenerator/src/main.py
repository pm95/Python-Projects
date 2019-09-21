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


def distance(p1, p2):
    acc = 0
    for i in range(len(p1)):
        acc += (p1[i]-p2[i])**2
    return math.sqrt(acc)


inPath = "../inputImages/roads.png"
outPath = "../outputImages/palette.png"

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
colorPalette = sorted(colorPalette, key=lambda c: sum(c)/len(c), reverse=True)

newImg = np.array(colorPalette).reshape((len(colorPalette), 1, 4))

newImg = np.tile(newImg, (len(colorPalette), 1))
newImg = Image.fromarray(newImg)
newImg.save(outPath)
