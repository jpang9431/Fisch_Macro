from pynput.keyboard import Key, Controller
keyboard = Controller()

def inputSpace():
    keyboard.press(Key.space)

def releaseSpace():
    keyboard.release(Key.space)