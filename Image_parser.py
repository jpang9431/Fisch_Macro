from PIL import Image
import os

def displayImage(image: Image, name=str):
    im = Image.open(image)
    print(im.size())
    width, height = im.size()
    with open(name+".csv") as file:
        test = ""
        for i in range(width):
            for j in range(height):
                test+=im.getpixel((i,j))+","
            test+="\n"
        file.write(test)

    
    
