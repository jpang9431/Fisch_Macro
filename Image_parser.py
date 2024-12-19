from PIL import Image
import os

def displayImage(image: Image, name=str):
    width, height = image.size
    with open(name+".csv","w") as file:
        test = ""
        for i in range(width):
            for j in range(height):
                test+=str(image.getpixel((i,j)))+","
            test = test[:-1]
            test+="\n" 
        file.write(test)

    
    
