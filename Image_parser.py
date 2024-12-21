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

def simpleSum(image: Image, name:str):
    width, height = image.size
    with open(name+".csv","w") as file:
        text = ""
        for i in range(width):
            for j in range(height):
                text+=str(sum(image.getpixel((i,j))))+","
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
        #print(name+"|"+str(counter))
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
        sumation = sum(image.getpixel((i,0)))
        flattenedColor = flattenPixelColor(sumation)

        if(flattenedColor == elevation):
            # same elevation
            continue

        
        #print("matrix: " + str(matrix))

        #print("elevation is " + str(elevation) + " and flattened color is " + str(flattenedColor) + " at pixel " + str(i))
        
        if(flattenedColor > elevation):
            startElevation(matrix, elevation, flattenedColor, sumation, i)

        if((flattenedColor > elevation) or i == 0):
            # dont end if going to an higher elevation
            elevation = flattenedColor
            continue

        if(elevation != 0):
            # old elevation not the background (also check if it is the first pixel)
            endElevation(matrix, elevation, flattenedColor, sumation, i)

        elevation = flattenedColor

    # below is analasys
    
    for i in range(3):
        for j in range(2):
            if(matrix[i][j] == -1):
                # location not set
                print("Location for elevation " + str(i+1) + " has not been defined, i="+str(i)+", j="+str(j))
    
    print("Data:\nCapture Bar: " + str(matrix[1-1][0]) + " to " + str(matrix[1-1][1]) + "\nDirectional Arrow: " + str(matrix[2-1][0]) + " to " + str(matrix[2-1][1]) + "\nTarget Bar: " + str(matrix[3-1][0]) + " to " + str(matrix[3-1][1]))
    print("Directional arrow reletive to capture bar is: ", end="")

    captureBarStart = matrix[0][0]
    captureBarEnd = matrix[0][1]
    directionalArrowStart = matrix[1][0]
    directionalArrowEnd = matrix[1][1]
    targetBarStart = matrix[2][0]
    targetBarEnd = matrix[2][1]
    directionalArrowCenter = (directionalArrowEnd + directionalArrowStart) / 2
    percent = ((directionalArrowCenter)-captureBarStart) / (captureBarEnd - captureBarStart)

    print(str(percent * 100) + "%")
    if(percent > 0.5):
        print("Capture bar is movng right")
    else:
        print("Capture bar is moving left")

    captureBarCenter = (captureBarEnd + captureBarStart) / 2
    targetBarCenter = (targetBarEnd + targetBarStart) / 2

    if(targetBarCenter > captureBarCenter):
        print("Target bar is to the right of the capture bar -> Press space")
    else:
        print("Target bar is to the left of the capture bar -> Do nothing")

            


                    
def warnBehavior():
    raise ValueError

def startElevation(matrix: list, elevation: int, flattenedColor: int, sumation: int, i: int):
    '''
    Precondition: 
    Postcondition: 
    '''

    if(matrix[flattenedColor-1][0] == -1):
        #location not set yet
        #print("set start location for elevation " + str(flattenedColor) + " at " + str(i))
        matrix[flattenedColor-1][0] = i
    else:
        # location already set
        warningLocationAlreadySet(0, elevation, flattenedColor, i, sumation, matrix[flattenedColor-1][0])
        warnBehavior()

def endElevation(matrix: list, elevation: int, flattenedColor: int, sumation: int, i: int):
    '''
    Precondition: 
    Postcondition: 
    '''

    if(matrix[elevation-1][1] == -1):
        #location not set yet
        #print("set end location for elevation " + str(elevation) + " at " + str(i))
        matrix[elevation-1][1] = i
    else:
        # location already set
        #print("original location was " + str(matrix[elevation-1][1]))
        warningLocationAlreadySet(1, elevation, flattenedColor, i, sumation, matrix[flattenedColor-1][1])
        warnBehavior()

def warningInvalidElevationChange(fromElevation, toElevation, pixelNum: int, rgbSumation: int):
    print("The elevation change from " + str(fromElevation) + " to " + str(toElevation) + " is invalid (pixel location: " + str(pixelNum) + ", sumation of: " + str(rgbSumation) + ")")

def warningLocationAlreadySet(location: int, fromElevation, toElevation, pixelNum: int, rgbSumation: int, originalLocation: int):
    print("The ", end="")
    
    if(location == 1):
        print("end location for elevation " + str(fromElevation), end="")
    else:
        print("start location for elevation " + str(toElevation), end ="")

    print(" has already been defined at " + str(originalLocation) + "\nOccured at pixel #" + str(pixelNum) + " with a sum of "+ str(rgbSumation) + " and a classification of ", end = "")

    if(location == 1):
        print(str(toElevation))
    else:
        print(str(fromElevation))



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
    elif ((sumation > 140 and sumation < 180) or (sumation > 233)):
        return 1

def edgeDetection(image:int, name: str) -> bool:
    width, height = image.size
    prev = 0
    left = -1
    lastFishingBar = 0
    #Fish bar is at the 0 index and the fishing bar is at the 1 index
    bars = [[],[]]
    for i in range(width):
        sumOfValues = sum(image.getpixel((i,0)))
        if (sumOfValues<100):
            sumOfValues=0
        if (not prev==233 and sumOfValues==233):
            bars[0].append(i)
        elif(prev==233 and not sumOfValues==233):
            bars[0].append(i)
        if (prev==0 and not sumOfValues==0):
            left = i
        elif (not prev==0 and sumOfValues==0 and i-left>lastFishingBar):
            lastFishingBar = i-left
            bars[1] = [left,i]
        prev = sumOfValues
    if (not prev==0 and width-left>lastFishingBar):
            lastFishingBar = i-left
            bars[1] = [left,i]
    #print(name+"|"+str(bars))
    return bars

def determineWhatToDo(bar):
    fish = getCenterOfBar(bar[0])
    fishingBar = getCenterOfBar(bar[1])
    if (fishingBar<fish):
        return True
    else:
        return False    

def getCenterOfBar(bar):
    return (bar[0]+bar[1])/2