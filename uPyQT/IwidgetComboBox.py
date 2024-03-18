"""
Combo Box (Menú de Opciones):
Este widget proporciona una lista desplegable de opciones predefinidas. Permite a los usuarios seleccionar una 
opción de entre las disponibles.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Definir la opción seleccionada por defecto (Se entrega el valor de la opción).
opcion: str = "Opción 1"

#2. Definir la lista de opciones.
opciones: list = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

#3. Definir la función controladora.
def mostrar() -> None:
    opcion = cb.currentText()
    print(opcion)

#4. Crear el ComboBox y añadir las opciones.
cb: object = QComboBox(ventana)
cb.addItems(opciones) #Agregando los items seleccionables.
cb.setCurrentText(opcion) #Definiendo el valor por defecto.
cb.setGeometry(50, 50, 100, 30)

btn: object = QPushButton(ventana)
btn.setText("Mostrar")
btn.setCursor(Qt.PointingHandCursor)
btn.setGeometry(50, 100, 100, 30)
btn.clicked.connect(mostrar)

#5. Mostrar los los widgets.
cb.setVisible(True)
btn.setVisible(True)

ventana.show()

sys.exit(app.exec_())