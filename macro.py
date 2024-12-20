from PIL import Image
import keyboard
import Image_gathering as ig
import Image_parser as ip
import time
import Keyboard_Controler_Win as kc
from multiprocessing import Process
import sys
from screeninfo import get_monitors

monitor = get_monitors()[0]
print(str(monitor))
width = monitor.width
height = monitor.height

left = int(width * .3)
right = int(width * .7)
height = int(height * .85)

region = (left,height-1,right-left,1)
bbox = (left,height-1,right,height)

def collectData():
    counter = 0

    while True:
        keyboard.wait("e")
        ip.displayImage(ig.getPillowScreenShots(str(counter)),str(counter))
        
        counter+=1
        print("e")

def testSum(path:str,name:str):
    '''ip.processImage(Image.open(path),name+"_sum")'''
    ip.determinePosition(Image.open(path),name)

def func1():
    for i in range (5):
        testSum(str(i)+"_small.png",str(i))

def gameLoop():
    keyboard.wait("e") 
    print("e")
    currentlyInputting = False
    while True:
        im = ig.getPillowScreenShot()
        result = ip.determinePositionV2(im,"")
        currentlyInputting = result
        if result=="in":
            keyboard.release("space")
            keyboard.send("space")
        elif (result=="left"):
            if (currentlyInputting=="right"):
                time.sleep(0.5)
            keyboard.release("space")
        elif (result=="right"):
            keyboard.press("space")
            #if (not currentlyInputting):
                #kc.inputSpace()
        #else:
            #kc.releaseSpace()
            
if __name__ == "__main__":
    #collectData()
    #ip.displayImage("0.png","0")
    '''gameLoop()'''
    for i in range(5):
        im = Image.open(str(i)+"_full.png")
        im = im.crop(bbox)
        im.save(str(i)+"_small.png")
        im = im.convert("1")
        im.save(str(i)+"bw.png")
        #ip.determineDifference(im,str(i))'''


