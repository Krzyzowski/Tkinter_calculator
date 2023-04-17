from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Wpisz swoje imię:")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()



myButton = Button(root, text="Click Me!", padx=10, pady=10, command=myClick, width=60, bg="yellow")
myButton.pack()


root.mainloop()