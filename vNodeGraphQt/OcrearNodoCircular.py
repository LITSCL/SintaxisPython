from Qt import QtWidgets
from NodeGraphQt import BaseNodeCircle, NodeGraph

#Nodo personalizado.
class EjemploNodoCircle(BaseNodeCircle):
    __identifier__: str = "cl.litscl.ejemplonodocircle"
    NODE_NAME: str = "Ejemplo Nodo"

    #Estructura del nodo.
    def __init__(self) -> None:
        super(EjemploNodoCircle, self).__init__()
        
        puerto_a: object = self.add_input("Entrada 1")
        puerto_b: object = self.add_input("Entrada 2")
        puerto_c: object = self.add_output("Salida 1")
        puerto_d: object = self.add_output("Salida 2")

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    grafico: object = NodeGraph()

    grafico.register_node(EjemploNodoCircle)

    ventana: object = grafico.widget
    ventana.show()

    #Instanciar nodos (Opcional).
    nodo_a: object = grafico.create_node("cl.litscl.ejemplonodocircle.EjemploNodoCircle", name = "Nodo A")
    nodo_b: object = grafico.create_node("cl.litscl.ejemplonodocircle.EjemploNodoCircle", name = "Nodo B", pos = [300, 100])

    app.exec_()