import keyboard
import pyautogui
import pyscreeze

counter = 0
while True:
    keyboard.wait("e")
    screenshot = pyautogui.screenshot(str(counter)+".png")
    counter+=1
    print("e")
