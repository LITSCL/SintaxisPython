from Qt import QtWidgets
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

    grafico: object = NodeGraph()

    grafico.register_node(EjemploNodo)

    ventana: object = grafico.widget
    ventana.show()

    nodo_a: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    #Obtener puerto.
    puerto_d: object = nodo_a.get_output(2)

    #Obtener el nombre del puerto.
    nombre_puerto: str = puerto_d.name()
    print(f"Nombre del puerto: {nombre_puerto}")

    #Hacer visible o invisible un puerto.
    puerto_d.set_visible(True)

    #Obtener si el puerto es visible o no actualmente.
    visibilidad_puerto: bool = puerto_d.visible()
    print(f"Puerto visible: {visibilidad_puerto}")

    #Bloquear el puerto (No se pueden sacar tuberías de allí).
    puerto_d.set_locked(False)

    #Obtener si el puerto esta bloqueado o no actualmente.
    bloqueo_puerto: bool = puerto_d.locked()
    print(f"Puerto bloqueado: {bloqueo_puerto}")

    #Conectar un puerto a otro.
    nodo_a.set_output(2, nodo_b.input(0))

    #Obtener los puertos ajenos conectados a este.
    puertos_conectados: list = puerto_d.connected_ports()
    print(puertos_conectados)

    #Desconectar un puerto especifico que está conectado a este.
    puerto_d.disconnect_from(puerto_d.connected_ports()[0])

    #Desconectar todos los puertos ajenos conectados a este.
    puerto_d.clear_connections()

    #Cambiar el color interno del puerto.
    puerto_d.color = (3, 252, 57)
    
    #Cambiar el color del borde del puerto.
    puerto_d.border_color = (252, 3, 40)

    app.exec_()
