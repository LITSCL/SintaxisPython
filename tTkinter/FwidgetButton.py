"""
Button (Botón):
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

#1. Crear el Text, indicando a que ventana va a pertenercer.
btn: object = Button(ventana)

#2. Configurar el Button.
btn.config(
    text = "Texto del Botón",
    cursor = "hand2"
)

#3. Empaquetar el Button (Esto permite que se muestre).
btn.pack()

ventana.mainloop()