"""
Check Button (Checkbox):
Este widget permite a los usuarios realizar acciones al hacer click en el botón. Se puede asociar una función 
o un comando al botón para que se ejecute cuando el usuario lo presiona.
"""

import pathlib
from tkinter import *

ruta_absoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(ruta_absoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear los Checkbuttons, indicando a que ventana va a pertenercer.
chk_1: object = Checkbutton(ventana)
chk_2: object = Checkbutton(ventana)
chk_3: object = Checkbutton(ventana)

#2. Configurar los Checkbuttons.
chk_1.config(
    text = "Java",
    cursor = "hand2",
    onvalue = 1, #Valor que toma el Widget si está activado.
    offvalue = 0 #Valor que toma el Widget si está desactivado.
)

chk_2.config(
    text = "PHP",
    cursor = "hand2",
    onvalue = 1,
    offvalue = 0
)

chk_3.config(
    text = "C++",
    cursor = "hand2",
    onvalue = 1,
    offvalue = 0,
)

#3. Empaquetar los Checkbuttons (Esto permite que se muestren).
chk_1.pack()
chk_2.pack()
chk_3.pack()

ventana.mainloop()