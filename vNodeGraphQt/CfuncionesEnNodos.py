from Qt import QtWidgets, QtGui
from NodeGraphQt import NodeGraph, BaseNode
from NodeGraphQt.constants import PipeLayoutEnum

class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        puerto_a: object = self.add_input("Entrada", color = (180, 80, 0))
        puerto_b: object = self.add_output("Salida 1")
        puerto_c: object = self.add_output("Salida 2")
        puerto_d: object = self.add_output("Salida 3")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    #Cambiar color del nodo.
    nodo_a.set_color(153, 51, 102)

    #Cambiar nombre del nodo.
    nodo_a.set_name("Nombre Cambiado")

    #Obtener el color del nodo.
    color_nodo: tuple = nodo_a.color()
    print(f"Color del nodo: {color_nodo}")

    #Deshabilitar un nodo.
    nodo_a.set_disabled(True)
    
    #Obtener si el nodo está deshabilitado o no.
    nodo_deshabilitado: bool = nodo_a.disabled()
    print(f"Nodo deshabilitado: {nodo_deshabilitado}")

    #Seleccionar un nodo (Por defecto siembre viene seleccionado el último nodo agregado en el gráfico).
    nodo_b.set_selected(False)

    #Obtener si un nodo está seleccionado.
    nodo_seleccionado: bool = nodo_b.selected()
    print(f"Nodo seleccionado: {nodo_seleccionado}")

    #Cambiar la posición del nodo (Ambos ejes).
    nodo_b.set_pos(600, 300)

    #Cambiar la posición del nodo (Eje X).
    nodo_b.set_y_pos(600)

    #Cambiar la posición del nodo (Eje Y).
    nodo_b.set_x_pos(600)

    #Obtener la posición del nodo.
    posicion_nodo: list = nodo_b.pos()
    print(posicion_nodo)

    #Cambiar la dirección del layout del nodo.
    nodo_b.set_layout_direction(1) #Orientaciones (HORIZONTAL = 0 | Vertical = 1).

    #Obtener la dirección del layout del nodo.
    direccion_layout_nodo: int = nodo_b.layout_direction()
    print(f"Direccion del layout del nodo: {direccion_layout_nodo}")

    app.exec_()
