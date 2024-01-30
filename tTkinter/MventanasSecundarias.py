import pathlib
from tkinter import *

#Definir el Frame hijo.
class SecundarioFrame:
    ruta_absoluta: str = str(pathlib.Path().absolute())
    ventana_padre: object = None
    
    #1. Constructor del Secundario Frame.
    def __init__(self, ventana_padre: object) -> None:
        #1.1 Obtener el frame padre.
        self.ventana_padre = ventana_padre
        
        #1.2 Modificar los parámetros del frame.
        self.top = Toplevel(ventana_padre)
        self.top.title("Ventana Secundaria")
        self.top.iconbitmap(self.ruta_absoluta + "/recursos/icono.ico")
        self.top.geometry("550x350")
        self.top.resizable(1, 1)

        #1.3 Añadir los widgets al frame.
        Label(self.top, text = "Contenido del JInternalFrame").pack(padx = 20, pady = 20)
        Button(self.top, text = "Cerrar", command = self.cerrar).pack(pady = 10)

        #1.4. Definir la ubicación del frame respecto a su padre.
        largo_padre: int = self.ventana_padre.winfo_width()
        ancho_padre: int = self.ventana_padre.winfo_height()
        largo_propio: int = self.top.winfo_reqwidth()
        ancho_propio: int = self.top.winfo_reqheight()

        x: int = (largo_padre - largo_propio) // 2 #Calculando las coordenadas para el frame secundario.
        y: int = (ancho_padre - ancho_propio) // 2
        self.top.geometry(f"+{x}+{y}") #Estableciendo la posición del frame secundario.
        
    #2. Métodos del frame (Se asocian a los widgets).
    def cerrar(self) -> None:
        self.top.destroy()

#Definir el Frame padre.
class MainFrame:
    ruta_absoluta: str = str(pathlib.Path().absolute())
    ventana_principal: object = None
    
    #1. Constructor del Main Frame.
    def __init__(self, ventana_principal: object) -> None:
        #1.1 Obtener el frame principal.
        self.ventana_principal = ventana_principal
        
        #1.2 Modificar los parámetros del frame.
        self.ventana_principal.title("Ventana Principal")
        self.ventana_principal.iconbitmap(self.ruta_absoluta + "/recursos/icono.ico")
        self.ventana_principal.geometry("750x450")
        self.ventana_principal.resizable(1, 1)

        #1.3 Añadir los widgets al frame.
        Button(ventana_principal, text = "Mostrar Ventana Secundaria", command = self.mostrar_secundario_frame).pack(pady = 20)
    
    #2. Método de muetreo del frame principal.
    def mostrar(self) -> None:
        self.ventana_principal.mainloop()
        
    #3. Métodos del frame (Se asocian a los widgets).
    def mostrar_secundario_frame(self) -> None:
        secundario_frame: SecundarioFrame = SecundarioFrame(self.ventana_principal) #Creando la instancia de SecundarioFrame.

main_frame: MainFrame = MainFrame(Tk())
main_frame.mostrar()