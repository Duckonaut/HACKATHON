import tkinter as tk

class Window(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Breathalyser")
        self.window.geometry("300x500")
        self.sex = None
        self.weight = None
        self.create_listbox()
        self.create_boxes()
        self.window.mainloop()

    def create_listbox(self):
        self.sex_title = tk.Text(self.window, bg='white', fg='black', height=1, width=22)
        self.sex_title.place(x=60, y=0)
        self.sex_title.insert(tk.END, "Are you male or female?")
        self.tkvarq = tk.StringVar(self.window)
        self.tkvarq.set("Choose your gender")
        options = ['Male', 'Female']
        self.listbox = tk.OptionMenu(self.window, self.tkvarq, *options, command=self.set_sex)
        self.listbox.config(width=31)
        self.listbox.place(x=5, y=30)

    def set_sex(self, evt):
        self.sex = 0.7 if self.tkvarq.get() == "Male" else 0.6
        
    def create_boxes(self):
        self.create_beers()
        self.create_wines()
        self.create_vodkas()
        self.create_weight()
        self.create_calculate_button()

    def create_beers(self):
        self.b_text = tk.Text(self.window, bg='white', fg='black', height=1, width=12)
        self.b_text.place(x=95, y=70)
        self.b_text.insert(tk.END, "Beers drunk:", "center")
        self.beer = tk.Entry(self.window, width=31)
        self.beer.place(x=20, y=100)

    def create_wines(self):
        self.w_text = tk.Text(self.window, bg='white', fg='black', height=1, width=22)
        self.w_text.place(x=55, y=130)
        self.w_text.insert(tk.END, "Glasses of wine drunk:", "center")
        self.wine = tk.Entry(self.window, width=31)
        self.wine.place(x=20, y=160)

    def create_vodkas(self):
        self.v_text = tk.Text(self.window, bg='white', fg='black', height=1, width=18)
        self.v_text.place(x=70, y=190)
        self.v_text.insert(tk.END, "Vodka shots drunk:", "center")
        self.vodka = tk.Entry(self.window, width=31)
        self.vodka.place(x=20, y=220)

    def create_weight(self):
        self.weight_text = tk.Text(self.window, bg='white', fg='black', height=1, width=18)
        self.weight_text.place(x=70, y=250)
        self.weight_text.insert(tk.END, "Enter your weight:", "center")
        self.weight_entry = tk.Entry(self.window, width=31)
        self.weight_entry.place(x=20, y=280)

    def create_calculate_button(self):
        self.calculate = tk.Button(self.window, text="CALCULATE!", width=10, command=self.get_alcohol)
        self.calculate.place(x=95, y=310)

    def get_alcohol(self):
        self.alcohol_amount = 0
        try:
            self.alcohol_amount = int(self.beer.get()) * 18 + int(self.wine.get()) * 20 + int(self.vodka.get()) * 13
            self.weight = int(self.weight_entry.get())
            if self.sex: 
                self.amount = (str(round(self.alcohol_amount / (self.sex * self.weight), 3)) + "‰")
                self.show_time()
            else: pass
        except(TypeError, ValueError): pass

    def show_time(self):
        self.alcotext = tk.Text(self.window, bg='white', fg='black', height=3, width=31)
        self.alcotext.tag_configure("center", justify='center')
        self.alcotext.insert("1.0", self.amount+'\n'+f'You need to wait {self.get_time()} hours')
        self.alcotext.tag_add("center", "1.0", "end")
        self.alcotext.place(x=20, y=350)
    
    def get_time(self):
        sub = 0.15 if self.sex == 'Male' else 0.1
        hours = 0
        promiles = round(self.alcohol_amount / (self.sex * self.weight), 3)
        while promiles > 0.2:
            hours += 1
            promiles -= sub
        return hours

Window()
