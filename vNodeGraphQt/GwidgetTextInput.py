from Qt import QtWidgets
from NodeGraphQt import BaseNode, NodeGraph

#Nodo personalizado.
class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    #Estructura del nodo.
    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        self.add_text_input("nombre", label = "Nombre", text = "Daniel", placeholder_text = "Ingrese su nombre...")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    #Instanciar nodos.
    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = [300, 100])

    #Obtener el widget de un nodo especifico.
    text_input_widget: object = EjemploNodo.get_widget(nodo_a, name = "nombre")

    #Obtener valor ingresado.
    text_input_widget.get_value()

    #Modificar valor ingresado.
    text_input_widget.set_value("Esteban")

    app.exec_()