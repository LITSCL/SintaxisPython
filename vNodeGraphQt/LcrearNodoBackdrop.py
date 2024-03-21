from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode, BackdropNode

class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()
        
        puerto_a: object = self.add_input("Entrada", color = (180, 80, 0))
        puerto_b: object = self.add_output("Salida")

#Creando clase nodo backdrop (Hereda de BackdropNode).
class EjemploNodoBackdrop(BackdropNode):
    __identifier__: str = "cl.litscl.ejemplonodobackdrop"
    NODE_NAME: str = "Ejemplo Nodo Backdrop"

    def __init__(self) -> None:
        super(EjemploNodoBackdrop, self).__init__()
        

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    #Registrar el nodo Backdrop.
    controlador.register_node(EjemploNodoBackdrop)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))
    
    #Crear el nodo Backdrop.
    nodo_c: object = controlador.create_node("cl.litscl.ejemplonodobackdrop.EjemploNodoBackdrop", name = "Nodo Backdrop")

    #Configurar el nodo Backdrop.
    nodo_c.set_size(300, 300)
    nodo_c.set_text("Este es el texto del Backdrop.")
    nodo_c.set_color(130, 80, 0)
    
    #Envolver nodos (Opcional).
    nodo_c.wrap_nodes(nodes = [nodo_b, nodo_a])

    nodo_a.set_output(0, nodo_b.input(0))

    app.exec_()
