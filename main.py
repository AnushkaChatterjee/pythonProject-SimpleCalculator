from tkinter import *
import math
root = Tk()
root.title("Simple Calculator")
root.configure(bg="#ffffff")

e = Entry(root, width=80, background="black", borderwidth=6, bg="#878D91", bd=4, fg="white")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if fmath == "addition":
        e.insert(0, f_num + int(second_number))

    if fmath == "subtraction":
        e.insert(0, f_num - int(second_number))

    if fmath == "multiplication":
        e.insert(0, f_num * int(second_number))

    if fmath == "division":
        e.insert(0, f_num / int(second_number))

def button_sqrt():
    current1 = e.get()
    e.delete(0, END)
    e.insert(0, math.sqrt(int(current1)))

def button_add():
    first_number = e.get()
    global f_num
    global fmath
    fmath = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global fmath
    fmath = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global fmath
    fmath = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global fmath
    fmath = "division"
    f_num = int(first_number)
    e.delete(0, END)

# Define Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1),fg="#ffffff", bg="#000000", font="bold")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), fg="#ffffff", bg="#000000", font="bold")
button_3 = Button(root, text="3", padx=42.5, pady=20, command=lambda: button_click(3), fg="#ffffff", bg="#000000", font="bold")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), fg="#ffffff", bg="#000000", font="bold")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), fg="#ffffff", bg="#000000", font="bold")
button_6 = Button(root, text="6", padx=42.5, pady=20, command=lambda: button_click(6), fg="#ffffff", bg="#000000", font="bold")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), fg="#ffffff", bg="#000000", font="bold")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), fg="#ffffff", bg="#000000", font="bold")
button_9 = Button(root, text="9", padx=42.5, pady=20, command=lambda: button_click(9), fg="#ffffff", bg="#000000", font="bold")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), fg="#ffffff", bg="#000000", font="bold")
button_add = Button(root, text="+", padx=51, pady=20, command=button_add, fg="#ffffff", bg="#000000", font="bold")
button_equal = Button(root, text="=", padx=95, pady=20, command=button_equal, fg="#ffffff", bg="#000000", font="bold")
button_clear = Button(root, text="Clear", padx=93, pady=20, command=button_clear, fg="#ffffff", bg="#000000", font="bold")

button_subtract = Button(root, text="-", padx=48, pady=20, command=button_subtract, fg="#ffffff", bg="#000000", font="bold")
button_multiply = Button(root, text="*", padx=53, pady=20, command=button_multiply, fg="#ffffff", bg="#000000", font="bold")
button_divide = Button(root, text="/", padx=48.5, pady=20, command=button_divide, fg="#ffffff", bg="#000000", font="bold")
button_sqrt= Button(root, text="sqrt", padx=99, pady=20, command=button_sqrt, fg="#ffffff", bg="#000000", font="bold")

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=1, column=3, columnspan=2)
button_add.grid(row=3, column=3)
button_equal.grid(row=4, column=1,columnspan=2)

button_subtract.grid(row=3, column=4)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=2, column=4)
button_sqrt.grid(row=4, column=3, columnspan=2)

root.mainloop()