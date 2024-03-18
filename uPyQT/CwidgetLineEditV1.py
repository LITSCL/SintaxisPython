"""
Line Edit (Entrada de texto):
Las entradas de texto permiten al usuario ingresar datos de texto, como nombres, contraseñas o números. Puedes 
recuperar el texto ingresado por el usuario para su procesamiento.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear el LineEdit.
le: object = QLineEdit(ventana)

#2. Configurar el LineEdit.

le.setStyleSheet("color: black; background-color: green; font: 12pt Arial;") #Estilos CSS del LineEdit.
le.move(10, 10) #Especificar el margen de la izquierda y superior del LineEdit.
le.resize(300, 30) #Indicando las dimensiones del LineEdit.
le.setCursor(Qt.PointingHandCursor) #Indica la forma del cursor cuando se pasa el mouse por encima.

#3. Mostrar el LineEdit.
le.setVisible(True)

ventana.show()

sys.exit(app.exec_())