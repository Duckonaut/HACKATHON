import webbrowser
import tkinter as tk
import time
import random


def start():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)


def main():
    while random.randint(0, 10) != 1:
        time.sleep(1)

    root = tk.Tk()
    root.title("Uwaga!")
    root.geometry("250x100")
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    root.configure(bg="black")
    lbl = tk.Label(root, text="Masz nową wiadomość!", font=('arial', 15, 'bold'), foreground='red', background='black', width=20)
    lbl.place(x=5, y=10)
    Button1 = tk.Button(root, text="Otwórz", command=start).place(x=100, y=50)
    root.mainloop()


if __name__ == "__main__":
    main()
