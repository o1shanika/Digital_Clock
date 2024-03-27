from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("_Digital Clock_")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('calibri', 60, 'bold'), background='#AF7AC5', foreground='black')
label.pack(anchor='center')
time()

mainloop()



