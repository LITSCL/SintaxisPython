from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode
from NodeGraphQt.constants import PortTypeEnum

class EjemploNodo(BaseNode):

    __identifier__: str = "cl.litscl.ejemplonodo"

    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        puerto_a: object = self.add_input("Entrada 1")
        puerto_b: object = self.add_input("Entrada 2")
        puerto_c: object = self.add_input("Entrada 3")
        puerto_d: object = self.add_output("Salida 1")
        puerto_e: object = self.add_output("Salida 2")
        puerto_f: object = self.add_output("Salida 3")
        
        #Controlar la compatibilidad de puertos.
        puerto_a.add_accept_port_type( #Indicando que este input solo acepta este output.
            port_name = "Salida 1",
            port_type = PortTypeEnum.OUT.value, #Indicando que el puerto es de salida.
            node_type = "cl.litscl.ejemplonodo.EjemploNodo"
        )

        puerto_c.add_reject_port_type( #Indicando que este input rechaza este output.
            port_name = "Salida 3",
            port_type = PortTypeEnum.OUT.value, #Indicando que el puerto es de salida.
            node_type = "cl.litscl.ejemplonodo.EjemploNodo"
        )


if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    nodo_a.set_output(0, nodo_b.input(0))
    nodo_a.set_output(2, nodo_b.input(1))

    app.exec_()

