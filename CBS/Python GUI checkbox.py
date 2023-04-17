from tkinter import *

def display():
    if(x.get()==1):
        print("CBS VT OK")
    else:
        print("CBS VT NOK")


window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text="CBS VT",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',11),
                           fg='black')
check_button.pack()




window.mainloop()