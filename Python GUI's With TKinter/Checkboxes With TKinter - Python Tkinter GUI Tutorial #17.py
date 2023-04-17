from tkinter import *

root = Tk()
root.title('Krzyzu')

root.geometry("200x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Kliknij", variable=var, onvalue="VT ok", offvalue="VT nok")
c.deselect()
c.pack()



myButton = Button(root, text="Show Selection", command=show).pack()



root.mainloop()
