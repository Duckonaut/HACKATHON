import PIL.ImageGrab
from pynput.mouse import Listener
import tkinter as tk


#wszechobecne okienko podążające za kursorem zainicjowane globalnie


def on_click(x, y, button, pressed):
    if pressed:
        rgb = PIL.ImageGrab.grab().load()[x, y]
        #zmien kolor okienka i napisz na nim jego kolor w rgb
        print(rgb)


def main():
    with Listener(on_click=on_click) as listener:
        listener.join()

    while True:
        pass


if __name__ == "__main__":
    main()
