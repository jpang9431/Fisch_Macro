from PIL import Image
import keyboard
import Image_gathering as ig
import Image_parser as ip
import time
import Keyboard_Controler_Win as kc


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
    while True:
        im = ig.getPillowScreenShot()
        if(not ip.validImage(im)):
            time.sleep(0.02)
            continue

        if ip.determinePosition(im, ""):
            kc.inputSpace()
        else:
            kc.releaseSpace()

if __name__ == "__main__":
    #collectData()
    #ip.displayImage("0.png","0")
    gameLoop()