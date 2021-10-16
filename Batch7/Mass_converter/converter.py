import tkinter as tk

class Window(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mass converter")
        self.window.geometry("300x400")
        self.units_names = ['mg', 'g', 'kg', 't', 'lb', 'oz']
        self.unit1 = None
        self.unit2 = None
        self.amount = None
        self.units_values = {       # how much kg is in every unit
            "mg": 0.000001,
            "g": 0.001,
            "kg": 1,
            "t": 1000,
            "lb": 0.43559,
            "oz": 0.02835
        }
        self.create_title()
        self.create_listboxes()
        self.create_entry_widget()
        self.create_convert_button()
        self.window.mainloop()

    def create_title(self):
        self.title = tk.Text(self.window, bg='white', fg='black', height=1, width=16)
        self.title.place(x=85, y=3)
        self.title.insert(tk.END, "Select two units", "center")

    def create_listboxes(self):
        self.tkvarq1 = tk.StringVar(self.window)
        self.tkvarq2 = tk.StringVar(self.window)
        self.tkvarq1.set("Convert from")
        self.tkvarq2.set("Convert to")
        self.listbox1 = tk.OptionMenu(self.window, self.tkvarq1, *self.units_names, command=self.set_unit1)
        self.listbox2 = tk.OptionMenu(self.window, self.tkvarq2, *self.units_names, command=self.set_unit2)
        self.listbox1.config(width=13)
        self.listbox2.config(width=13)
        self.listbox1.place(x=0, y=50)
        self.listbox2.place(x=150, y=50)

    def set_unit1(self, evt):
        self.unit1 = self.units_values[self.tkvarq1.get()]

    def set_unit2(self, evt):
        self.unit2 = self.units_values[self.tkvarq2.get()]

    def create_entry_widget(self):
        self.entry = tk.Entry(self.window, width=31)
        self.entry.place(x=20, y=110)

    def create_convert_button(self):
        self.convert = tk.Button(self.window, text="CONVEEERT!", width=10, command=self.calculate)
        self.convert.place(x=95, y=150)

    def calculate(self):
        try:
            self.amount = float(self.entry.get())
        except(ValueError):
            self.amount = 1
        try:
            self.converted = self.amount * self.unit1 / self.unit2
            self.create_result()
        except(TypeError):
            pass

    def create_result(self):
        self.result = tk.Text(self.window, bg='white', fg='black', height=1, width=31)
        self.result.place(x=20, y=200)
        self.result.insert(tk.END, str(round(self.converted, 9)) + " " + self.tkvarq2.get(), "center")

Window()
