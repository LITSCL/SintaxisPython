from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode

#Definir los estilos de la aplicación Qt.
estilos: str = """
    QWidget {
        background-color: #353535;
        color: white;
    }
    
    QPushButton {
        background-color: #454545;
        color: white;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 6px;
    }

    QPushButton:hover {
        background-color: #555;
    }

    QPushButton:pressed {
        background-color: #333;
    }
"""
#Crear la clase nodo (Hereda de BaseNode).
class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        puerto_a: object = self.add_input("Entrada", color = (180, 80, 0))
        puerto_b: object = self.add_output("Salida")

if (__name__ == "__main__"):
    #Instanciar la aplicación Qt.
    app: object = QtWidgets.QApplication([])

    #Aplicar la hoja de estilos.
    app.setStyleSheet(estilos)

    #Crear el grafico de nodos de la aplicación.
    grafico: object = NodeGraph()

    #Registrar las clases que permiten instanciar nodos.
    grafico.register_node(EjemploNodo)

    #Crear la ventana principal.
    ventana: object = QtWidgets.QWidget()
    layout_principal: object = QtWidgets.QGridLayout()

    #Agregar la ventana principal al layout.
    ventana.setLayout(layout_principal)

    #Crear el panel lateral.
    panel_lateral: object = QtWidgets.QWidget()
    layout_lateral: object = QtWidgets.QVBoxLayout()

    #Agregar el panel lateral al layout.
    panel_lateral.setLayout(layout_lateral)
    layout_principal.addWidget(panel_lateral, 0, 0)

    #Añadir los botones al panel lateral.
    for i in range(5):
        btn: object = QtWidgets.QPushButton(f"Botón {i + 1}")
        layout_lateral.addWidget(btn)

    #Añadir el grafico de nodos al panel principal.
    layout_principal.addWidget(grafico.widget, 0, 1)

    #Instanciar nodos (Opcional).
    nodo_a: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = grafico.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    #Conectar los nodos (Opcional).
    nodo_a.set_output(0, nodo_b.input(0))

    #Mostrar la ventana principal.
    ventana.show()

    #Iniciar el bucle de eventos (Mantiene en ejecución la aplicación Qt).
    app.exec_()