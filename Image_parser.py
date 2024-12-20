from PIL import Image
import os

lastAction = ""

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
        
#0 is the black bar color, 1 is any other color, if this prints out 2 then the fish line is within the fishing bar, otherwise if it is 4 then the fish line is not within the fishing bar
def processImage(image: Image, name:str) -> None:
    width, height = image.size
    with open(name+".csv","w") as file:
        text = ""
        prev = 0
        counter = 0
        for i in range(width):
            sumOfValues = sum(image.getpixel((i,0)))
            if (sumOfValues<100):
                
                text+=str(sumOfValues)
            else:
                text+=str(sumOfValues)
            if (prev!=sumOfValues):
                counter+=1
                prev = sumOfValues
            text+="\n" 
        if (prev==1):
            counter+=1
        print(name+"|"+str(counter))
        file.write(text)

#Determines where the fishing bar is realively to the fish bar, returns true if need to click/hold down mouse, returns false if need to do nothing (aka no click and lift down click mouse)
def determinePosition(image: Image, name:str) -> bool:
    width, height = image.size
    bars = []
    prev = 0
    left = -1
    for i in range(width):
        sumOfValues = sum(image.getpixel((i,0)))
        if (sumOfValues<100):
            sumOfValues=0
        else:
            sumOfValues=1
        if (sumOfValues!=prev):
            prev = sumOfValues
            if (left==-1):
                left = i
            else:
                bars.append(i-left)
                left = -1
    if (prev==1):
        bars.append(width-left-1)
    global lastAction
    if (len(bars)==1):
        #print(name+"|inside")
        if (lastAction=="right"):
            return True
        else:
            return False
    elif(bars[0]<bars[1]):
        #print(name+"|left")
        lastAction = "left"
        return False
    elif(bars[0]>bars[1]):
        #print(name+"|right")
        lastAction = "right"
        return True

# Returns if the current image is a valid image or not 
def validImage(image: Image) -> bool:
    try:
        determinePosition(image,"")
    except:
        return False
    return True

def determineDifference(image: Image, name: str) ->bool:
    width, height = image.size
    prev = sum(image.getpixel((0,0)))
    index=[]
    with open(name+".csv","w") as file:
        text = ""
        for i in range(1,width,1):
            #print(i)
            sumOfValues = sum(image.getpixel((i,0)))
            diff = abs(sumOfValues-prev)
            if (diff>40):
                text+=str(diff)+"\n"
                index.append(i)
            else:
                text+=str(0)+"\n"
            prev = sumOfValues
        #print(text)
        print(name+"|"+str(index))
        file.write(text)
        file.close()

def analyseImage(image: Image):
    '''
    Precondition: image has a height of 1
    Postcondition: analyse the image and determine the position of the capture bar, target bar, and directional arrow
    '''
    width, height = image.size

    # prev = -1 #previous pixel sum
    elevation = 0 #the elevation of the "bump" (the ammount of the sum of the rgb values)
    # elevatin is 0 for background, 1 for capture bar, 2 for directional arrow, 3 for target bar

    matrix = [[-1 for i in range(2)] for j in range(3)]
    
    # captureBarStart = matrix[1-1][0]
    # captureBarEnd = matrix[1-1][1]

    # directionalArrowStart = matrix[2-1][0]
    # directionalArrowEnd = matrix[2-1][0]

    # targetBarStart = matrix[3-1][0]
    # targetBarEnd = matrix[3-1][1]

    for i in range(width):
        sumation = sum(image.getpixel(i,0))
        flattenedColor = flattenPixelColor(sumation)

        if(flattenedColor == elevation):
            # same elevation
            continue
        
        # elevation CHANGED
        match flattenedColor:
            case 0:
                # Set endpoint if not set already

                #TODO setup system to "end" and "start" areas, preferabally functions

                if(matrix[elevation-1][1] != -1):
                    # check if end area already set
                    warningLocationAlreadySet(1, elevation, flattenedColor, i, sumation, matrix[elevation-1][1])
                    warnBehavior()
                
                # set endpoint
                matrix[elevation-1][1] = i
            
            case 1:
                # change to catch bar

                if(matrix[elevation-1][0] != -1):
                    # check if starting point already set
                    warningLocationAlreadySet(1, elevation, flattenedColor, i, sumation, matrix[elevation-1][1])

            


                    
def warnBehavior():
    raise ValueError

def warningInvalidElevationChange(fromElevation, toElevation, pixelNum: int, rgbSumation: int):
    print("The elevation change from " + fromElevation + " to " + toElevation + " is invalid (pixel location: " + pixelNum + ", sumation of: " + rgbSumation + ")")

def warningLocationAlreadySet(location: int, fromElevation, toElevation, pixelNum: int, rgbSumation: int, originalLocation: int):
    print("The ", end="")
    
    if(location == 0):
        print("end ", end="")
    else:
        print("start ", end ="")

    print("location for elevation " + str(fromElevation) + " has already been defined at " + str(originalLocation) + "\nOccured at pixel #"+pixelNum+"with a sum of "+ rgbSumation + " and a classification of " + toElevation)



def flattenPixelColor(sumation: int) -> int:
    '''
    Precondition: 
    Postcondition: 
    '''
    
    if (sumation == 233):
        # target block color
        return 3
    elif (sumation == 400):
        # arrow color
        return 2
    elif (sumation < 100):
        return 0
    else:
        return 1
