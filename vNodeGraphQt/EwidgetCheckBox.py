from Qt import QtWidgets
from NodeGraphQt import BaseNode, NodeGraph

#Nodo personalizado.
class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    #Estructura del nodo.
    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        self.add_checkbox("hombre", label = "Hombre", state = True)

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    grafico: object = NodeGraph()

    grafico.register_node(EjemploNodo)

    ventana: object = grafico.widget
    ventana.show()

    #Instanciar nodos.
    nodo_a: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = [300, 100])

    #Obtener el widget de un nodo especifico.
    check_box_widget: object = EjemploNodo.get_widget(nodo_a, name = "hombre")

    #Obtener valor seleccionado (True | False).
    check_box_widget.get_value()

    #Modificar valor seleccionado.
    check_box_widget.set_value(False)

    app.exec_()