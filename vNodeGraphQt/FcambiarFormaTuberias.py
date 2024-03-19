from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode
from NodeGraphQt.constants import PipeLayoutEnum

class EjemploNodo(BaseNode):

    __identifier__: str = "cl.litscl.ejemplonodo"

    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        self.add_input("Entrada", color = (180, 80, 0))
        self.add_output("Salida")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    #Cambiar la forma en la que se organizan las tuberías.
    controlador.set_pipe_style(PipeLayoutEnum.ANGLE.value) #Organización en ángulos de 90°.
    controlador.set_pipe_style(PipeLayoutEnum.STRAIGHT.value) #Organización en líneas rectas.

    controlador.register_node(EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    nodo_a.set_output(0, nodo_b.input(0))

    app.exec_()

