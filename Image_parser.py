from PIL import Image
import os

def displayImage(image: Image):
    im = Image.open(image)
    print(im.size())
    width, height = im.size()

    for i in range(width):
        for j in range(height):
            print(im.getpixel((i,j)))

    
    
