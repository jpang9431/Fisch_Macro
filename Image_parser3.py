from PIL import Image

FISH_BAR = 233
ARROW = 400

def analyseImage(image: Image):
    '''
    Precondition: image has a height of 1
    Postcondition: analyse the image and determine the position of the capture bar, target bar, and directional arrow
    '''
    width, height = image.size

    mode = 0 # 0 for search, 1 for FISH_BAR, 2 for ARROW
    fish = False
    arrow = False

    matrix = [[-1 for i in range(2)] for j in range(3)]
    
    i = 0
    while i < width:
        i+=1
        if(fish and arrow):
            break

        sumation = sum(image.getpixel((i,0)))

        

        #print(mode)

        match mode:
            case 0:
                match sumation:
                    case 233:
                        mode = 1
                        matrix[0][0] = i
                    case 400:
                        mode = 2
                        matrix[1][0] = i
            case 1:
                while(sum(image.getpixel((i+1,0))) == FISH_BAR):
                    i+=1
                matrix[0][1] = i
                fish = True
                mode = 0
            case 2:
                while((sum(image.getpixel((i+1,0)))) == ARROW):
                    i+=1
                matrix[1][1] = i
                arrow = True
                mode = 0
    
    #print("fish: " + str(matrix[0][0]) + " to " + str(matrix[0][1]) + "\narrow: " + str(matrix[1][0]) + " to " + str(matrix[1][1]))

    check = True
    start = matrix[1][1]
    multiplier = matrix[1][1] - matrix[1][0]
    i = 1
    while check:
        i+=1
        location = start + (1 if i%2 else -1) * multiplier * i
        
        if(location >= width or location < 0):
            break

        sumation = sum(image.getpixel((location,0)))
        if(sumation < 140):
            check = False
    
    location = start
    if(i%2):
        location = start - multiplier * 10
    else:
        location = start + multiplier * 10

    print("center of capture bar is approximatly at " + str(location))
    print("fish bar is at " + str(matrix[0][0]) + " to " + str(matrix[0][1]))
    fishCenter = (matrix[0][0] + matrix[0][1]) / 2
    return fishCenter > location
                