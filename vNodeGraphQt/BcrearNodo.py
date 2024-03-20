from Qt import QtWidgets
from NodeGraphQt import BaseNode, NodeGraph

#Nodo personalizado.
class EjemploNodo(BaseNode):

    __identifier__: str = "cl.litscl.ejemplonodo"

    NODE_NAME: str = "Ejemplo Nodo"

    #Estructura del nodo.
    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()
        puerto_a: object = self.add_input("Entrada 1")
        puerto_b: object = self.add_input("Entrada 2")
        puerto_c: object = self.add_output("Salida 1")
        puerto_d: object = self.add_output("Salida 2")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    #Instanciar nodos (Opcional).
    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = [300, 100])

    app.exec_()