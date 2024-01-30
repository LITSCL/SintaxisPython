"""
Entry (Entrada de texto):
Las entradas de texto permiten al usuario ingresar datos de texto, como nombres, contraseñas o números. Puedes 
recuperar el texto ingresado por el usuario para su procesamiento.
"""

import pathlib
from tkinter import *

ruta_absoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(ruta_absoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear el Entry, indicando a que ventana va a pertenercer.
etr: object = Entry(ventana) 

#2. Configurar el Entry.
etr.config(
    show = "*", #El argumento "show", permite ocultar los caracteres ingresados.
    fg = "black", #Color de letra.
    bg = "green", #Color de fondo.
    font = ("Arial", 12), #Fuente de la letra y tamaño.
    cursor = "circle" #Indica la forma del cursor cuando se pasa el mouse por encima.
)

#3. Empaquetar el Entry (Esto permite que se muestre).
etr.pack()

ventana.mainloop()