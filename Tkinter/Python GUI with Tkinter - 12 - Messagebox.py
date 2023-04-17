from tkinter import *

import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkey can...')

answer = tkinter.messagebox.askquestion('Question 1', 'Do You like silly faces?')

if answer == 'yes':
    print(' 8==D~`')

root.mainloop()