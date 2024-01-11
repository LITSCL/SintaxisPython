"""
Radio Button (Botones de opción):
Este widget permite a los usuarios seleccionar una opción de un conjunto predefinido. A diferencia del widget Button, 
los RadioButtons se utilizan en grupos, y solo se puede seleccionar una opción dentro de ese grupo a la vez.
"""

import pathlib
from tkinter import *

rutaAbsoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(rutaAbsoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear la variable de englobe de Radiobuttons.
opcion = IntVar()

#2. Definir el Radio Button seleccionado por defecto (Se entrega el valor del Radiobutton).
opcion.set(1)

#3. Crear los Radiobuttons, indicando a que ventana va a pertenercer.
rb_1: object = Radiobutton(ventana)
rb_2: object = Radiobutton(ventana)

#4. Definir la función controladora.
def mostrar():
    print(opcion.get())

#5. Configurar los Radiobuttons.
rb_1.config(
    text = "Hombre",
    cursor = "hand2",
    variable = opcion,
    value = 1,
    command = mostrar
)

rb_2.config(
    text = "Mujer",
    cursor = "hand2",
    variable = opcion,
    value = 2,
    command = mostrar
)

#6. Empaquetar los Radiobuttons (Esto permite que se muestre).
rb_1.pack()
rb_2.pack()

ventana.mainloop()