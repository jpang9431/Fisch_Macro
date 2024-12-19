from PIL import Image
import os

def displayImage(image: Image, name:str):
    width, height = image.size
    with open(name+".csv","w") as file:
        text = ""
        for i in range(width):
            for j in range(height):
                text+=str(image.getpixel((i,j)))+","
            text = text[:-1]
            text+="\n" 
        file.write(text)
        
def processImage(image: Image, name:str):
    width, height = image.size
    with open(name+".csv","w") as file:
        text = ""
        prev = 0
        counter = 0
        for i in range(width):
            sumOfValues = sum(image.getpixel((i,0)))
            if (sumOfValues<100):
                sumOfValues=0
                text+="0"
            else:
                sumOfValues=1
                text+="1"
            if (prev!=sumOfValues):
                counter+=1
                prev = sumOfValues
            text+="\n" 
        if (prev==1):
            counter+=1
        print(name+"|"+str(counter))
        file.write(text)

    
    
