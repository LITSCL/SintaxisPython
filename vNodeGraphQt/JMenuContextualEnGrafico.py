from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode

class EjemploNodo(BaseNode):

    __identifier__: str = "cl.litscl.ejemplonodo"

    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        self.add_input("Entrada", color = (180, 80, 0))
        self.add_output("Salida")

def menu_funcion_1() -> None:
    print("Funcion 1")

def menu_funcion_2() -> None:
    print("Funcion 2")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    #Habilitando el menú contextual para el gráfico.
    menu_contextual_grafico: object = controlador.get_context_menu("graph")

    #Añadiendo los seleccionables con sus respectivas funciones.
    menu_contextual_grafico.add_command("Test 1", func = menu_funcion_1)
    menu_contextual_grafico.add_command("Test 2", func = menu_funcion_2)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    nodo_a.set_output(0, nodo_b.input(0))

    app.exec_()