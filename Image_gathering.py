from PIL import Image
import os
import keyboard
import pyautogui
import pyscreeze
import screeninfo
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


def getScreenShot(name:str,path=""):
    pyautogui.screenshot(imageFilename=path+name+"_full.png")
    pyautogui.screenshot(imageFilename=path+name+"_small.png",region=region)

