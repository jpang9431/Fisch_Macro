import keyboard
import Image_gathering as ig
import Image_parser as ip


def collectData():
    counter = 0

    while True:
        keyboard.wait("e")
        ip.displayImage(ig.getPillowScreenShots(str(counter)),str(counter))
        
        counter+=1
        print("e")

if __name__ == "__main__":
    collectData()
    '''ip.displayImage("0.png","0")'''