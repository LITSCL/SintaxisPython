import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#Instanciar la aplicación Qt.
app: object = QApplication(sys.argv)

#Crear la ventana principal.
ventana: object = QMainWindow()

#Asignar el titulo de la ventana.
ventana.setWindowTitle("Ventana Principal")

#Dimensionar la ventana principal.
ventana.setGeometry(100, 100, 750, 450)

#Bloquear el redimensionamiento de la ventana.
ventana.setFixedSize(ventana.size())

#Mostrar la ventana principal.s
ventana.show()

#Iniciar el bucle de eventos (Mantiene en ejecución la aplicación Qt)
sys.exit(app.exec_())