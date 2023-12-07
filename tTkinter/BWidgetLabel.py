"""
Label (Etiqueta):
La clase Label se utiliza para mostrar texto o imágenes en una ventana de Tkinter. Se Puede configurar el texto que 
se muestra en la etiqueta y ajustar su estilo, como la fuente, el color, etc.
"""

import pathlib
from tkinter import *

rutaAbsoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(rutaAbsoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear el Label, indicando a que ventana va a pertenercer.
lbl: object = Label(ventana, text = "Hola, soy el texto del Label.")

#2. Configurar el Label.
lbl.config(
    fg = "white", #Color de letra.
    bg = "black", #Color de fondo.
    padx = 20, #Relleno del Widget en eje x.
    pady = 20, #Relleno del Widget en eje y.
    font = ("Arial", 12), #Fuente de la letra y tamaño.
    cursor = "circle" #Indica la forma del cursor cuando se pasa el mouse por encima.
)

#3. Empaquetar el Label (Esto permite que se muestre).
lbl.pack()

ventana.mainloop()