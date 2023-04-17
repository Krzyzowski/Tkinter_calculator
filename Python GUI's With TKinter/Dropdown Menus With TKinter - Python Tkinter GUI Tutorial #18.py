from tkinter import *

root = Tk()
root.geometry("250x250")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Pokaż kotku", command=show).pack()




root.mainloop()