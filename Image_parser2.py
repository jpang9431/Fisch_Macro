from PIL import Image

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
    else:
        return 0
