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

while True:
    keyboard.wait("e")
    screenshot = pyautogui.screenshot(imageFilename=str(counter)+".png",region=region)
    counter+=1
    print("e")
