from tkinter import *


def doNothing():
    print("ok ok I won't ...")

root = Tk()

root.geometry("400x400")

# ****** Main  Menu *****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="DOK1", menu=subMenu)
subMenu.add_command(label="dach całość", command=doNothing)
subMenu.add_command(label="Endwal blizej biura", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="na wykonczenie", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Wykonczenie1", menu=editMenu)
editMenu.add_command(label="VT ",command=doNothing)
editMenu.add_command(label="Visual ",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Srut", command=doNothing)
editMenu.add_command(label="29/30", command=doNothing)

# *******The Toolbar*****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="dodaj CBS", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="usun CBS", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()