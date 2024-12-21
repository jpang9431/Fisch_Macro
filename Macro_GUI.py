import tkinter as tk

root = None

def toggleOnTop(button):
    global root
    if root is not None:
        root.attributes('-topmost', not root.attributes('-topmost'))
        button.config(text='On Top: On' if root.attributes('-topmost') else 'On Top: Off')
        root.update()


def createGUI():
    global root
    if root is not None:
        return

    root = tk.Tk()
    root.title("FISCH Macro")
    root.geometry("400x450")

    root.attributes('-topmost', True)
    root.resizable(False, False)

    label = tk.Label(root, text="FISCH Macro")
    label.pack(padx=10, pady=10)

    button1 = tk.Button(root, text='On Top: On', command=lambda: toggleOnTop(button1))
    button1.pack(pady=10)

    panel = tk.Frame(root)

    button2 = tk.Button(panel, text='Start Automation')
    button2.pack(side=tk.LEFT, padx=10)

    button3 = tk.Button(panel, text='Stop Automation')
    button3.pack(side=tk.RIGHT, padx=10)

    root.mainloop()

def onTop(onTop: bool):
    global root
    root.attributes('-topmost', onTop)
    root.update()


if __name__ == "__main__":
    createGUI()