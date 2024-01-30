"""
Message Box (Alertas):
En Tkinter, messagebox es un módulo que proporciona funciones para mostrar mensajes emergentes y cuadros de diálogo en una interfaz 
gráfica de usuario. 
"""

import pathlib
from tkinter import *
from tkinter.messagebox import * #Importando el módulo.

ruta_absoluta: str = str(pathlib.Path().absolute())

ventana: object = Tk()
ventana.title("Ventana Principal")
ventana.iconbitmap(ruta_absoluta + "/recursos/icono.ico")
ventana.geometry("750x450")
ventana.resizable(1, 1)

#1. Crear los botones que accionan las alertas.
btn_1: object = Button(ventana)
btn_2: object = Button(ventana)
btn_3: object = Button(ventana)
btn_4: object = Button(ventana)

#2. Crear las funciones que renderizan las alertas.
def mostrar_alerta_info() -> None:
    showinfo("Información", "Este es el texto de la alerta Info")
    
def mostrar_alerta_warning() -> None:
    showwarning("Precaución", "Este es el texto de la alerta Warning")
    
def mostrar_alerta_error() -> None:
    showerror("Error", "Este es el texto de la alerta Error")
    
def mostrar_alerta_question() -> None:
    resultado: str = askquestion("Pregunta", "¿Eres Hombre?")
    
    if (resultado == "yes"):
        print("Si")
    else:
        print("No")

#3. Configurar los Buttons.
btn_1.config(
    text = "Alerta Info",
    cursor = "hand2",
    command = mostrar_alerta_info
)

btn_2.config(
    text = "Alerta Warning",
    cursor = "hand2",
    command = mostrar_alerta_warning
)

btn_3.config(
    text = "Alerta Error",
    cursor = "hand2",
    command = mostrar_alerta_error
)

btn_4.config(
    text = "Alerta Question",
    cursor = "hand2",
    command = mostrar_alerta_question
)

#4. Empaquetar los Buttons (Esto permite que se muestren).
btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()

ventana.mainloop()