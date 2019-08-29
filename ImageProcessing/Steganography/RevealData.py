# Author: Pietro Malky
# Purpose: Program for image re-sizing to handle bulk images
# Date: 08/27/2019

from Steganographer import decodeMessage

inputPath = "messenger.png"  # save as PNG because JPG uses lossy compression

with open('secretMsg.txt', 'w') as fout:
    fout.write(decodeMessage(inputPath))
