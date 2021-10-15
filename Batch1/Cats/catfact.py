import json
import requests
import json
import tkinter as tk
import random

CATFACT_URL = 'https://catfact.ninja/fact'

def main():
    response = requests.get(CATFACT_URL)
    fact = json.loads(response.text)['fact']

    app = tk.Tk()
    app.geometry("400x200")
    app.wm_title("Cat Fact nr. " + str(random.randint(1, 1000)))


    label = tk.Label(text=fact, width=400, height=100, wraplength=400, font=("Arial", 16))
    label['bg'] = '#FFB6C1'   
    label.pack()

    app.mainloop()


if __name__ == '__main__':
    main()