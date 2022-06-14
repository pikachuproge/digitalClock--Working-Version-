from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)
 

clock = Label(master, font=("Calibri",90),bg="black",fg="white")
clock.pack()

get_time()

master.mainloop()

# To change the font to a font supported by windows, change the font=("Calibri",90) to font=("YOUR FONT NAME HERE",90)
