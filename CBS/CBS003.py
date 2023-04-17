from tkinter import *


def doNothing():
    print("ok ok I won't ...")

root = Tk()

root.geometry("250x250")

# ****** Main  Menu *****

menu = Menu(root)
root.config(menu=menu)

assDock1Menu = Menu(menu)
menu.add_cascade(label="assembly DOCK1", menu=assDock1Menu)
assDock1Menu.add_command(label="Roof all", command=doNothing)
assDock1Menu.add_command(label="Endwal 1", command=doNothing)
assDock1Menu.add_separator()
assDock1Menu.add_command(label="to finisching ->", command=doNothing)

finisching1Menu = Menu(menu)
menu.add_cascade(label="finisching1", menu=finisching1Menu)
finisching1Menu.add_command(label="VT ",command=doNothing)
finisching1Menu.add_command(label="Visual ",command=doNothing)
finisching1Menu.add_separator()
finisching1Menu.add_command(label="-> shoot blasting", command=doNothing)
finisching1Menu.add_command(label="-> 29/30", command=doNothing)

# *******The Toolbar*****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="add CBS", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="remove CBS", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()