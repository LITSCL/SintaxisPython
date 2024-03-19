from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode


#Creando clase nodo (Hereda de BaseNode).
class EjemploNodo(BaseNode):

    #Identificador único de la clase.
    __identifier__: str = "cl.litscl.ejemplonodo"

    #Nombre por defecto al instanciar el nodo.
    NODE_NAME: str = "Ejemplo Nodo"

    #Constructor del nodo (Indicando sus parametros por defecto al instanciarse en pantalla).
    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        #Creando un puerto de entrada (Input).
        self.add_input("Entrada", color = (180, 80, 0))

        #Creando un puerto de salida (Output).
        self.add_output("Salida")

if (__name__ == "__main__"):
    #Instanciar la aplicación Qt.
    app: object = QtWidgets.QApplication([])

    #Crear el controlador de nodos de la aplicación.
    controlador: object = NodeGraph()

    #Registrar las clases que permiten instanciar nodos.
    controlador.register_node(EjemploNodo)

    #Crear y mostrar la ventana principal.
    ventana: object = controlador.widget
    ventana.show()

    #Instanciar nodos (Opcional).
    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    #Conectar los nodos (Opcional).
    nodo_a.set_output(0, nodo_b.input(0)) #La salida del A se conecta a la entrada del B.

    #Iniciar el bucle de eventos (Mantiene en ejecución la aplicación Qt).
    app.exec_()
