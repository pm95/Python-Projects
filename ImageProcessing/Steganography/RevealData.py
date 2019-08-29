# Author: Pietro Malky
# Purpose: Program for image re-sizing to handle bulk images
# Date: 08/27/2019

from Steganographer import decodeMessage

# save as PNG to avoide lossy compression
inputPath = input("Please enter the path for concealer image: ")

with open('secretMsg.txt', 'w') as fout:
    fout.write(decodeMessage(inputPath))
