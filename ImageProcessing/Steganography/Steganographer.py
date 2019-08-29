# Author: Pietro Malky
# Purpose: Program for image re-sizing to handle bulk images
# Date: 08/27/2019


import os
import sys
import math

import numpy as np
from PIL import Image


# basic function definitions
def loadImageToArray(path):
    return np.array(Image.open(path))


def toBinary(message):
    result = []
    for char in message:
        char = ord(char)
        char = bin(char)[2:]
        char = "00000000"[len(char):] + char
        result.append(char)
    result = ''.join(result)
    return result


def fromBinary(binMsg):
    result = []
    for i in range(0, len(binMsg), 8):
        char = binMsg[i:i + 8]
        char = int(char, 2)
        char = chr(char)
        result.append(char)
    return ''.join(result)


def encodingFunction(imagePixels, message):
    rows = len(imagePixels)
    cols = len(imagePixels[0])
    for i in range(len(message)):
        r = math.floor(i/cols)
        c = i % cols

        imagePixels[r][c][0] = int(
            bin(
                imagePixels[r][c][0]
            )[2:-1] + message[i], 2)

        imagePixels[r][c][3] = 254

    return imagePixels


def decodingFunction(imagePixels):
    rows = len(imagePixels)
    cols = len(imagePixels[0])

    differences = []
    for i in range(rows):
        for j in range(cols):
            if imagePixels[i][j][3] != 254:
                break
            current = bin(imagePixels[i][j][0])[-1:]
            differences.append(str(current))

    return ''.join(differences)


def encodeMessage(imagePixels, message, outputPath):
    message = toBinary(message)
    imagePixels = encodingFunction(imagePixels, message)

    print("saving image...")

    try:
        Image.fromarray(imagePixels).save(outputPath)
        print("image saved with secret message...")
    except:
        print("could not save image to disk please try again")
        return False

    return True


def decodeMessage(moddedImgPath):
    print("beginning message decoding step...")
    modded = loadImageToArray(moddedImgPath)

    differences = decodingFunction(modded)
    hiddenMsg = fromBinary(differences)

    print("finished message decoding step...")

    return hiddenMsg
