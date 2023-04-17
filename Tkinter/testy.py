from tkinter import *


def doNothing():
    print("OK OK I won't....")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="DOK1", menu=subMenu)
subMenu.add_command(label="dach calosc", command=doNothing)
subMenu.add_command(label="zelazka", command=doNothing)
subMenu.add_command(label="caly CBS OK")

editMenu = Menu(menu)
menu.add_cascade(label="DOK2", menu=editMenu)
editMenu.add_command(label="dach calosc", command=doNothing)
editMenu.add_command(label="zelazka", command=doNothing)
editMenu.add_command(label="caly CBS OK", command=doNothing)

jedenMenu = Menu(menu)
menu.add_cascade(label="wykonczenie_1", menu=editMenu)
jedenMenu.add_command(label="VT", command=doNothing)
jedenMenu.add_command(label="manual", command=doNothing)
jedenMenu.add_command(label="Visual", command=doNothing)

dwaMenu = Menu(menu)
menu.add_cascade(label="wykonczenie_2", menu=editMenu)
dwaMenu.add_command(label="VT", command=doNothing)
dwaMenu.add_command(label="manual", command=doNothing)
dwaMenu.add_command(label="Visual", command=doNothing)

root.mainloop()