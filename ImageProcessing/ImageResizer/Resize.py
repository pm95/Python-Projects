# Author: Pietro Malky
# Purpose: Program for image re-sizing to handle bulk images
# Date: 08/27/2019


import os
from PIL import Image


class ImageResizer:
    def __init__(self, newWidth):
        self.newWidth = int(newWidth)
        self.images = {
            "originals": [],
            "resized": []
        }

    def getOriginals(self, exclude=[".DS_Store"]):
        self.images["originals"] = [path for path in os.listdir(
            "./originals") if path not in exclude]

    def getResized(self, exclude=[".DS_Store"]):
        self.images["resized"] = [path for path in os.listdir(
            "./resized") if path not in exclude]

    def setResized(self, value):
        self.images["resized"].append(value)

    def resizeImages(self):
        foundImages = False

        for image in self.images["originals"]:
            if image not in self.images["resized"]:
                originalPath = "./originals/%s" % image
                resizedPath = "./resized/%s" % image

                img = Image.open(originalPath)

                widthRatio = self.newWidth / img.size[0]
                newHeight = int(img.size[1] * widthRatio)

                img = img.resize((self.newWidth, newHeight), Image.ANTIALIAS)
                img.save(resizedPath)

                self.images["resized"].append(image)

                print("\t%s resized successfully" % image)

                foundImages = True

        if not foundImages:
            print("no images found to re-size")

    def scanAndResize(self):
        self.getOriginals()
        self.getResized()
        self.resizeImages()


newWidth = input("Enter a new width for the images: ")
resizer = ImageResizer(newWidth)
resizer.scanAndResize()
