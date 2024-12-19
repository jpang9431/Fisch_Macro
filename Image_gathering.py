from PIL import Image, ImageGrab, ImageShow
import os
import keyboard
import pyautogui
import pyscreeze
import screeninfo
from datetime import datetime
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

counter = 0


'''def getScreenShotSaved(name:str,path=""):
    currentTime = datetime.now()
    pyautogui.screenshot(imageFilename=path+name+"_full.png")
    elapsedTime1 = datetime.now()- currentTime
    currentTime = datetime.now()
    pyautogui.screenshot(imageFilename=path+name+"_small.png",region=region)
    elapsedTime2 = datetime.now() - currentTime
    print("Time to take full screenshot: "+str(elapsedTime1))
    print("Time to take small screenshot: "+str(elapsedTime2))'''

def getPillowScreenShots(name:str,path="")-> Image:
    im1 = ImageGrab.grab()
    im1.save(fp=path+name+"_full.png")
    im2 = im1.crop(bbox)
    im2.save(fp=path+name+"_small.png")
    return im2

def getPillowScreenShot(name:str,path="")-> Image:
    im = ImageGrab.grab(bbox=bbox)
    return im

'''def getScreenShot(name:str,path="") -> Image:
    return pyautogui.screenshot(region=region)'''