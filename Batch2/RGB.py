import PIL.ImageGrab
from pynput.mouse import Listener
import tkinter as tk


windowActive = False
keepRunning = True

def rgbToHex(rgb):
    return f'#{rgb[0]:0>2X}{rgb[1]:0>2X}{rgb[2]:0>2X}'

def on_click(x, y, button, pressed):
    global windowActive
    global keepRunning
    global listener

    if pressed and not windowActive:
        rgb = PIL.ImageGrab.grab().load()[x, y]

        windowActive = True
        listener.stop()

        app = tk.Tk()
        app.geometry(f'400x120+{x}+{y}')
        app.wm_title('Color Picker')
        app.command = lambda: exit(None)

        colorValues = f'RGB: {rgb}'
        label = label = tk.Label(text=colorValues, width=400, height=200, wraplength=400, font=("Arial", 16), fg=rgbToHex((255 - rgb[0], 255 - rgb[1], 255 - rgb[2])))
        label['bg'] = rgbToHex(rgb)
        label.pack()

        app.mainloop()

listener = None

def main():
    global listener

    with Listener(on_click=on_click) as l:
        listener = l
        listener.join()

if __name__ == "__main__":
    main()
