from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode
from NodeGraphQt.constants import LayoutDirectionEnum

class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        puerto_a: object = self.add_input("Entrada", color = (180, 80, 0))
        puerto_b: object = self.add_output("Salida")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    grafico: object = NodeGraph()

    grafico.register_node(EjemploNodo)

    #Cambiar la dirección del layout.
    grafico.set_layout_direction(LayoutDirectionEnum.HORIZONTAL.value) #Asignar dirección del Layout de izquierda a derecha.
    grafico.set_layout_direction(LayoutDirectionEnum.VERTICAL.value) #Asignar dirección del layout de arriba hacia abajo.

    ventana: object = grafico.widget
    ventana.show()

    nodo_a: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 150))

    nodo_a.set_output(0, nodo_b.input(0))

    app.exec_()

