#!python3

import tkinter as tk
from tkinter import*

win = tk.Tk()
win.geometry("500x400")

import math

trianglepic = PhotoImage(file="triangle.png")
l1 = tk.Label(win, image=trianglepic)

a_e = tk.Entry(win, width=7)
b_e = tk.Entry(win, width=7)
c_e = tk.Entry(win, width=7)
h_e = tk.Entry(win, width=7)

output = StringVar()
instruction = "Please insert the triangle measurements and it will show up here :D"
output.set(instruction)
e1 = tk.Entry(win, textvariable=output, width=len(instruction))

def calculate():
    a = a_e.get()
    b = b_e.get()
    c = c_e.get()
    h = h_e.get()
    if h != "":
        if b != "":
            area = float(b)*float(h)/2
            A = str(area)
            output.set("The area of the triangle is: " + A)
        elif a != "" and c != "":
            b = math.sqrt(float(a)**2-float(h)**2) + math.sqrt(float(c)**2-float(h)**2)
            area = float(b)*float(h)/2
            A = str(area)
            output.set("The area of the triangle is: " + A)
        else:
            output.set("The area cannot be calculated from the information given\nPlease try again")
    else:
        if a != "" and b != "" and c != "":
            s = (float(a)+float(b)+float(c))/2
            area = math.sqrt(s*(s-float(a))*(s-float(b))*(s-float(c)))
            A = str(area)
            output.set("The area of the triangle is: " + A)
        else:
            output.set("The area cannot be calculated from the information given. Please try again")

b1 = tk.Button(win, text="calculate :D", command=calculate)

l1.place(x=0,y=0)
e1.place(x=0,y=300)
b1.place(x=300,y=350)
a_e.place(x=100,y=150)
h_e.place(x=300,y=150)
c_e.place(x=400,y=150)
b_e.place(x=300,y=250)

win.mainloop()