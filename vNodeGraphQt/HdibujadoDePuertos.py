from Qt import QtWidgets, QtGui, QtCore
from NodeGraphQt import NodeGraph, BaseNode

class EjemploNodo(BaseNode):
    __identifier__: str = "cl.litscl.ejemplonodo"
    NODE_NAME: str = "Ejemplo Nodo"

    def __init__(self) -> None:
        super(EjemploNodo, self).__init__()

        puerto_a: object = self.add_input("Entrada", color = (180, 80, 0), painter_func = self.dibujar_puerto_triangular) #El parámetro "painter_func", recibe la función pintora.
        puerto_b: object = self.add_output("Salida")

    #Metodos de dibujado de puertos.
    def dibujar_puerto_cuadrado(self, painter: object, rect: object, info: dict) -> None:
        painter.save()

        #1. Definir variables de visualización del puerto.
        color: object = None
        color_borde: object = None

        #2. Establecer visualización en base a eventos del puerto.
        if (info["hovered"]): #Visualización cuando el mouse hace hover en el puerto.
            color = QtGui.QColor(14, 45, 59)
            color_borde = QtGui.QColor(136, 255, 35, 255)
        elif (info["connected"]): #Visualización cuando el puerto está conectado.
            color = QtGui.QColor(195, 60, 60)
            color_borde = QtGui.QColor(200, 130, 70)
        else: #Visualización por defecto del puerto.
            color = QtGui.QColor(*info["color"])
            color_borde = QtGui.QColor(*info["border_color"])

        #3. Configurar el pincel.
        pen: object = QtGui.QPen(color_borde, 1.8)
        pen.setJoinStyle(QtCore.Qt.MiterJoin)

        #4. Configurar el pintor y dibujar el puerto.
        painter.setPen(pen)
        painter.setBrush(color)
        painter.drawRect(rect)

        painter.restore()

    def dibujar_puerto_triangular(self, painter: object, rect: object, info: dict) -> None:
        painter.save()

        #1. Crear el triangulo.
        dimensiones: int = int(rect.height() / 2)
        triangulo: object = QtGui.QPolygonF()
        triangulo.append(QtCore.QPointF(-dimensiones, dimensiones))
        triangulo.append(QtCore.QPointF(0.0, -dimensiones))
        triangulo.append(QtCore.QPointF(dimensiones, dimensiones))

        #2. Ubicar el triangulo en la posicion adecuada.
        transformacion: object = QtGui.QTransform()
        transformacion.translate(rect.center().x(), rect.center().y())
        polygon: object = transformacion.map(triangulo)

        #3. Definir variables de visualización del puerto.
        color: object = None
        color_borde: object = None

        #4. Establecer visualización en base a eventos del puerto.
        if (info["hovered"]): #Visualización cuando el mouse hace hover en el puerto.
            color = QtGui.QColor(14, 45, 59)
            color_borde = QtGui.QColor(136, 255, 35, 255)
        elif (info["connected"]): #Visualización cuando el puerto está conectado.
            color = QtGui.QColor(195, 60, 60)
            color_borde = QtGui.QColor(200, 130, 70)
        else: #Visualización por defecto del puerto.
            color = QtGui.QColor(*info["color"])
            color_borde = QtGui.QColor(*info["border_color"])

        #5. Configurar el pincel.
        pen: object = QtGui.QPen(color_borde, 1.8)
        pen.setJoinStyle(QtCore.Qt.MiterJoin)

        #6. Configurar el pintor y dibujar el puerto.
        painter.setPen(pen)
        painter.setBrush(color)
        painter.drawPolygon(polygon)

        painter.restore()

if (__name__ == "__main__"):
    app: object = QtWidgets.QApplication([])

    controlador: object = NodeGraph()

    controlador.register_node(EjemploNodo)

    ventana: object = controlador.widget
    ventana.show()

    nodo_a: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo A")
    nodo_b: object = controlador.create_node("cl.litscl.ejemplonodo.EjemploNodo", name = "Nodo B", pos = (300, 50))

    nodo_a.set_output(0, nodo_b.input(0))  

    app.exec_()
