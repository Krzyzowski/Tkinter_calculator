from tkinter import *


def doNothing():
    print("ok ok I won't ...")

root = Tk()

root.geometry("400x400")

# ****** Main  Menu *****

menu = Menu(root)
root.config(menu=menu)

dok1Menu = Menu(menu)
menu.add_cascade(label="DOK1", menu=dok1Menu)
dok1Menu.add_command(label="dach całość", command=doNothing)
dok1Menu.add_command(label="Endwal blizej biura", command=doNothing)
dok1Menu.add_separator()
dok1Menu.add_command(label="na wykonczenie", command=doNothing)

wyk1Menu = Menu(menu)
menu.add_cascade(label="Wykonczenie1", menu=wyk1Menu)
wyk1Menu.add_command(label="VT ",command=doNothing)
wyk1Menu.add_command(label="Visual ",command=doNothing)
wyk1Menu.add_separator()
wyk1Menu.add_command(label="Srut", command=doNothing)
wyk1Menu.add_command(label="29/30", command=doNothing)

# *******The Toolbar*****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="dodaj CBS", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="usun CBS", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()