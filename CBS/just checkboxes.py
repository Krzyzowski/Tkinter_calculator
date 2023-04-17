from tkinter import *

root = Tk()

users = ['VT', 'Visual', 'Geometry']

variables = []

for x in range(len(users)):
    var_ejecutar = f"global {users[x]}_double_var"
    exec(var_ejecutar)

    var_ejecutar = f"{users[x]}_double_var=DoubleVar()"
    exec(var_ejecutar)

    variables.append(f"{users[x]}_double_var")

    var_ejecutar = f"""l = Checkbutton(root, text=\"{str(users[x][0])}\", 
        variable={users[x]}_double_var,onvalue = 1,offvalue = 0)"""
    exec(var_ejecutar)

    var_ejecutar = "l.pack(anchor = 'w')"
    exec(var_ejecutar)


def get_val():
    for i in variables:
        var_ejecutar = f"print({i}.get())"

        exec(var_ejecutar)


btn = Button(root, text="ACTUALIZAR", state=NORMAL, command=get_val, bg="#C2CDD1")  # crear boton
btn.pack(anchor='w')

root.mainloop()