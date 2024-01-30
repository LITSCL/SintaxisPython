"""
Option Menu (Menú de Opciones):
Este widget proporciona una lista desplegable de opciones predefinidas. Permite a los usuarios seleccionar una 
opción de entre las disponibles.
"""

import pathlib
from tkinter import *

ruta_absoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(ruta_absoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear la variable de englobe de seleccion de opciones.
opcion = StringVar()

#2. Definir la opción seleccionada por defecto (Se entrega el valor de la opción).
opcion.set("Opción 1")

#3. Definir la lista de opciones.
opciones: list = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

#4. Crear el OptionMenu, indicando a que ventana va a pertenercer.
om: object = OptionMenu(ventana, opcion, *opciones)

#5. Definir la función controladora.
def mostrar() -> None:
    print(opcion.get())

btn: object = Button(ventana)

btn.config(
    text = "Mostrar",
    cursor = "hand2",
    command = mostrar
)

#6. Empaquetar el OptionMenu (Esto permite que se muestre).
om.pack()
btn.pack()

ventana.mainloop()