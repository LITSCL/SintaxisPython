"""
Menu (Menú de Navegación):
El widget Menu en Tkinter es una interfaz gráfica que permite la creación de barras de menú desplegables. Estas barras 
de menú contienen opciones y comandos que los usuarios pueden seleccionar para realizar acciones específicas en la aplicación.
"""

import pathlib
from tkinter import *

ruta_absoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(ruta_absoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear el Menu, indicando a que ventana va a pertenercer.
mnu: object = Menu(ventana)

#2. Añadir el menu a la ventana.
ventana.config(
    menu = mnu
)

#3. Crear un menu desplegable (Opcional).
seleccionar_desplegable: object = Menu(mnu)

#4. Congigurar el menu desplegable (Opcional).
seleccionar_desplegable.config(
    tearoff = 0 #Elimina la línea inicial.
)

#5. Añadir los elementos al menu desplegable (Opcional).
seleccionar_desplegable.add_command(label = "Selección 1")
seleccionar_desplegable.add_separator()
seleccionar_desplegable.add_command(label = "Selección 2")
seleccionar_desplegable.add_separator()
seleccionar_desplegable.add_command(label = "Selección 3")
seleccionar_desplegable.add_separator()
seleccionar_desplegable.add_command(label = "Selección 4")

#6. Añadir los elementos al menu.
mnu.add_command(label = "Archivo")
mnu.add_command(label = "Editar")
mnu.add_command(label = "Depurar")
mnu.add_cascade(label = "Seleccionar", menu = seleccionar_desplegable)
mnu.add_command(label = "Salir", command = ventana.quit) #Se debe entregar la función sin ejecutarla, por eso no se añaden parentesis.

ventana.mainloop()