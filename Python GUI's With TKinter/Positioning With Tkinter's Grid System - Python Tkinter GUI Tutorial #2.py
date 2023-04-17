from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="eeeeeeeeeeeeeee")
myLabel3 = Label(root, text="aaaaaaaaaaaaaaaa")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=6, column=6)


root.mainloop()