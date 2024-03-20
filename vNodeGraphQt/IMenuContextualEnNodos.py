from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode

class EjemploNodo(BaseNode):

    __identifier__: str = "cl.litscl.ejemplonodo"

    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        puerto_a: object = self.add_input("Entrada", color = (180, 80, 0))
        puerto_b: object = self.add_output("Salida")

    #Funciones de menú contextual.
    def menu_funcion_1(self, nodo: object) -> None:
        print(f"Funcion 1: {nodo.name()}")

    def menu_funcion_2(self, nodo: object) -> None:
        print(f"Funcion 2: {nodo.name()}")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    #Habilitando el menú contextual para los nodos.
    menu_contextual_nodos: object = controlador.get_context_menu("nodes")

    #Añadiendo los seleccionables con sus respectivas funciones.
    menu_contextual_nodos.add_command("Test 1", func = EjemploNodo.menu_funcion_1, node_type = "cl.litscl.ejemplonodo.EjemploNodo", node_class = EjemploNodo)
    menu_contextual_nodos.add_command("Test 2", func = EjemploNodo.menu_funcion_2, node_type = "cl.litscl.ejemplonodo.EjemploNodo", node_class = EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    nodo_a.set_output(0, nodo_b.input(0))

    app.exec_()

