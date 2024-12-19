import keyboard
import Image_gathering as ig
import Image_parser as ip

counter = 0

while True:
    keyboard.wait("e")
    ig.getScreenShot(str(counter))
    counter+=1
    print("e")