# Author: Pietro Malky
# Purpose: Program for image re-sizing to handle bulk images
# Date: 08/27/2019


import os
import sys

import numpy as np
from PIL import Image


# basic function definitions
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
    for i in range(len(message)):
        bit = message[i]
        imagePixels[i][0][0] = bit
    return imagePixels


def decodingFunction(imagePixels):
    rows = len(imagePixels)

    differences = []
    for i in range(rows):
        current = imagePixels[i][0][0]
        if current > 1:
            break
        differences.append(str(current))

    return ''.join(differences)


def encodeMessage(imagePixels, message):
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
    modded = np.array(Image.open(moddedImgPath))

    differences = decodingFunction(modded)
    hiddenMsg = fromBinary(differences)

    return hiddenMsg


# define input + output paths
inputPath = "flowers.png"
outputPath = "messenger.png"  # save as PNG because JPG uses lossy compression


# define secret message
message = input("Please enter a message to hide: ")

# load file from disk
imagePixels = np.array(Image.open(inputPath))

encodeMessage(imagePixels, message)

with open('secretMsg.txt', 'w') as fout:
    fout.write(decodeMessage(outputPath))
