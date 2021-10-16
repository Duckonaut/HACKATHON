import time
import tkinter as tk
import winsound

stopper_running = 0
mode = 0
sh, sm, ss = 0, 0, 0
ah, am, asec = 0, 0, 0

def timeConvert(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    valueD = (((value/365)/24)/60)
    Days = int(valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)

    return f"{Days:0>2} : {Hours:0>2} : {Minutes:0>2} : {Seconds:0>2}"


def start():
    global stopper_running
    stopper_running = True


def stop():
    global stopper_running
    stopper_running = False


def reset(root, lbl):
    global ss, sh, sm
    ss = sh = sm = 0
    lbl = tk.Label(root, text=f"{sh:0>2} : {sm:0>2} : {ss:0>2}", font=('arial', 30, 'bold'), foreground='red', background='black', width=10)
    lbl.place(x=50, y=25)


def changeMode():
    global mode
    if mode == 0:
        mode = 1
    else:
        mode = 0


def stoperCount(root, lbl):
    global stopper_running, ss, sm, sh, ah, am, asec
    if (stopper_running):
        ss += 1
        if (ss == 60):
            ss = 0
            sm += 1
        if (sm == 60):
            sm = 0
            sh += 1
        if (sh, sm, ss) == (ah, am, asec):
            ah = am = asec = 0
            stopper_running = False
            lbl = tk.Label(root, text="ALARM!", font=('arial', 30, 'bold'), foreground='red', background='black', width=10)
            lbl.place(x=50, y=25)
            winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
        else:
            lbl = tk.Label(root, text=f"{sh:0>2} : {sm:0>2} : {ss:0>2}", font=('arial', 30, 'bold'), foreground='red', background='black', width=10)
            lbl.place(x=50, y=25)
    root.after(1000, lambda: stoperCount(root, lbl))


def setTime(text, root, datelbl):
    global ah, am, asec
    mytext = text.get()
    result = checkText(mytext)
    if (result[0]):
        ah, am, asec = result[1]
        datelbl = tk.Label(root, text=f"{ah:0>2} : {am:0>2} : {asec:0>2}", font=('arial', 15, 'bold'), foreground='green', background='black', width=10)
        datelbl.place(x=110, y=0)


def checkText(text):
    try:
        variables = text.split(':')
        if (len(variables) != 3):
            raise Exception
        for i in range(0, 3):
            variables[i] = int(variables[i])
        if (variables[0] > 59 or variables[0] < 0):
            raise Exception
        if (variables[1] > 59 or variables[1] < 0):
            raise Exception
        if (variables[2] > 23 or variables[2] < 0):
            raise Exception
        return (True, variables)
    except Exception:
        return (False, [])


def main():
    root = tk.Tk()
    root.title("Sssstoper")
    root.geometry("300x160")
    root.resizable(False, False)
    root.configure(bg="black")
    textInTextBox = tk.StringVar()

    lbl = tk.Label(root, text=f"{sh:0>2} : {sm:0>2} : {ss:0>2}", font=('arial', 30, 'bold'), foreground='red', background='black', width=10)
    lbl.place(x=50, y=25)
    datelbl = tk.Label(root, text="", font=('arial', 15, 'bold'), foreground='red', background='black', width=10)

    Button1 = tk.Button(root, text="Start", command=start).place(x=15, y=50)
    Button2 = tk.Button(root, text="Stop", command=stop).place(x=15, y=80)
    Button3 = tk.Button(root, text="Reset", command=lambda: reset(root, lbl)).place(x=15, y=110)
    insertDate = tk.Entry(root, bd=5, textvariable=textInTextBox).place(x=100, y=75)
    Button5 = tk.Button(root, text="Ustaw Alarm", command=lambda: setTime(textInTextBox, root, datelbl)).place(x=125, y=110)
    format = tk.Label(root, text=f"( hh:mm:ss )", font=('arial', 10, 'bold'), foreground='red', background='black', width=10)
    format.place(x=210, y=110)

    root.after(1000, lambda: stoperCount(root, lbl))
    root.mainloop()



if __name__ == "__main__":
    main()