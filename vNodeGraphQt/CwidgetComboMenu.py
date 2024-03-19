from Qt import QtWidgets
from NodeGraphQt import BaseNode, NodeGraph

#Nodo personalizado.
class EjemploNodo(BaseNode):

    __identifier__: str = "cl.litscl.ejemplonodo"

    NODE_NAME: str = "Ejemplo Nodo"

    #Estructura del nodo.
    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        frutas: list = ["Manzanas", "Platanos", "Peras", "Mangos", "Naranjas"]
        self.add_combo_menu("listado", "Listado", frutas) #Añadiendo el widget ComboMenu con sus respectivos elementos.

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
    combo_menu_widget: object = EjemploNodo.get_widget(nodo_a, name = "listado")

    #Obtener todos los elementos.
    combo_menu_widget.all_items()

    #Agregar un nuevo elemento.
    combo_menu_widget.add_item("Frutillas")

    #Agregar varios elementos.
    combo_menu_widget.add_items(["Cerezas", "Pomelos", "Melones"])

    #Borrar todos los elementos.
    combo_menu_widget.clear()

    app.exec_()