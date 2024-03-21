"""
Button (Botón):
Este widget permite a los usuarios realizar acciones al hacer click en el botón. Se puede asociar una función 
o un comando al botón para que se ejecute cuando el usuario lo presiona.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear el Button.
btn: object = QPushButton(ventana)

#2. Configurar el Button.
btn.setText("Texto del Botón")
btn.setCursor(Qt.PointingHandCursor)

#3. Mostrar el Button.
btn.setVisible(True)

ventana.show()

sys.exit(app.exec_())