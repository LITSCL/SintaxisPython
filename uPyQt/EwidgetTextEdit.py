"""
Text Edit (Entrada de texto):
Las entradas de texto permiten al usuario ingresar datos de texto, como nombres, contraseñas o números. Puedes 
recuperar el texto ingresado por el usuario para su procesamiento.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear el TextEdit.
txt: object = QTextEdit(ventana)

#2. Configurar el TextEdit.
txt.setGeometry(50, 50, 300, 200) #Indica las dimensiones del TextEdit.
txt.setStyleSheet("color: black; background-color: green; padding: 20px; font: 12pt Arial;") #Estilos CSS del LineEdit.
txt.setCursor(Qt.PointingHandCursor) #Indica la forma del cursor cuando se pasa el mouse por encima.

#3. Mostrar el TextEdit.
txt.setVisible(True)

ventana.show()

sys.exit(app.exec_())