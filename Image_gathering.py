from PIL import Image
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

counter = 0


def getScreenShotSaved(name:str,path=""):
    currentTime = datetime.now()
    pyautogui.screenshot(imageFilename=path+name+"_full.png")
    elapsedTime1 = datetime.now()- currentTime
    currentTime = datetime.now()
    pyautogui.screenshot(imageFilename=path+name+"_small.png",region=region)
    elapsedTime2 = datetime.now() - currentTime
    print("Time to take full screenshot: "+str(elapsedTime1))
    print("Time to take small screenshot: "+str(elapsedTime2))

def getScreenShot(name:str,path="") -> Image:
    return pyautogui.screenshot(region=region)