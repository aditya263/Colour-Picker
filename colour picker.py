from tkinter import *

from tkinter.colorchooser import *
window =Tk()
window.title("Color Picker")
window.config(background="#000")
window.geometry("323x323")


def choose_color():
    color=askcolor()
    print(color)
    txtfield.insert(0,color)


txtfield=Entry(
    window,
    bd=3,
    width=48,
    font=("sans-serif",10),
)
txtfield.grid(row=0,column=0,)


a=Button(
    text="Select your color",
    font=("Roboto",15),
    bg="#fff",
    command=choose_color,
)
a.place(relx=0.5,rely=0.5,anchor=CENTER)


mainloop()