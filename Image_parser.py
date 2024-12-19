from PIL import Image
import os

def displayImage(image: Image, name=str):
    im = Image.open(image)
    width, height = im.size
    with open(name+".csv","w") as file:
        test = ""
        for i in range(height):
            for j in range(width):
                test+=str(im.getpixel((j,i)))+","
            test = test[:-1]
            test+="\n"
        file.write(test)

    
    
