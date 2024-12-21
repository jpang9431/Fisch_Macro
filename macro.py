from PIL import Image
import keyboard
import Image_gathering as ig
import Image_parser3 as ip3
import Image_parser as ip
import time
import Keyboard_Controler_Win as kc
from multiprocessing import Process
import sys

def collectData():
    counter = 5

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
        if ip.determinePosition(im, ""):
            keyboard.send("space")
            #if (not currentlyInputting):
                #kc.inputSpace()
        #else:
            #kc.releaseSpace()

def timeTest():
    JScore = 0
    BScore = 0
    for i in range(8):
        
        name = str(i)+"_small.png"
        image = Image.open(name)

        print("Image " + name)
        
        current = time.time()
        ip3.analyseImage(image)
        bTime = time.time()-current
        current = time.time()
        ip.edgeDetection(image, name)
        jTime = time.time()-current

        print("BTime: "+str(bTime))
        print("JTime: "+str(jTime))
        if bTime > jTime:
            JScore+=1
        else:
            BScore+=1
    print("JScore: "+str(JScore))
    print("BScore: "+str(BScore))
    if(JScore > BScore):
        print("Jason wins")
    else:
        print("Bida wins")
            
if __name__ == "__main__":
    '''for i in range(8):
        print(str(ip.getCenterOfBar(ip.edgeDetection(Image.open(str(i)+"_small.png"),str(i))[1])))'''
    #collectData()
    #ip.displayImage("0.png","0")
    #gameLoop()
    
    '''for i in range(7):
        ip.processImage(Image.open(str(i)+"_small.png"),str(i)+"_sum")'''
    
    timeTest()



        