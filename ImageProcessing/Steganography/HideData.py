# Author: Pietro Malky
# Purpose: Program for image re-sizing to handle bulk images
# Date: 08/27/2019

from Steganographer import encodeMessage, loadImageToArray

# Run main script logic here:
# define input + output paths
inputPath = "flowers.png"
outputPath = "messenger.png"  # save as PNG because JPG uses lossy compression

# define secret message
message = input("Please enter a message to hide: ")

# load file from disk
imagePixels = loadImageToArray(inputPath)
encodeMessage(imagePixels, message, outputPath)
