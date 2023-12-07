import pathlib
from tkinter import *

rutaAbsoluta: str = str(pathlib.Path().absolute())

#Crear la ventana raíz.
ventana: object = Tk()

#Asignar el titulo de la ventana.
ventana.title("Ventana Principal")

#Asignar el icono a la ventana.
ventana.iconbitmap(rutaAbsoluta + "/recursos/icono.ico")

#Dimensionar la ventana raíz.
ventana.geometry("750x450")

#Bloquear el redimensionamiento de la ventana.
ventana.resizable(0, 0)

#Mostrar la ventana raíz hasta que se cierre.
ventana.mainloop()