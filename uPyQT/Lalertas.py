"""
Message Box (Alertas):
En Tkinter, messagebox es un módulo que proporciona funciones para mostrar mensajes emergentes y cuadros de diálogo en una interfaz 
gráfica de usuario. 
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear los botones que accionan las alertas.
btn_1: object = QPushButton("Alerta Info", ventana)
btn_2: object = QPushButton("Alerta Warning", ventana)
btn_3: object = QPushButton("Alerta Error", ventana)
btn_4: object = QPushButton("Alerta Question", ventana)

#2. Crear las funciones que renderizan las alertas.
def mostrar_alerta_info() -> None:
    QMessageBox.information(ventana, "Información", "Este es el texto de la alerta Info")

def mostrar_alerta_warning() -> None:
    QMessageBox.warning(ventana, "Precaución", "Este es el texto de la alerta Warning")

def mostrar_alerta_error() -> None:
    QMessageBox.critical(ventana, "Error", "Este es el texto de la alerta Error")

def mostrar_alerta_question() -> None:
    resultado: object = QMessageBox.question(ventana, "Pregunta", "¿Eres Hombre?")

    if (resultado == QMessageBox.Yes):
        print("Si")
    else:
        print("No")

#3. Configurar los Buttons.
btn_1.setCursor(Qt.PointingHandCursor)
btn_1.setGeometry(50, 50, 150, 30)
btn_1.clicked.connect(mostrar_alerta_info)

btn_2.setCursor(Qt.PointingHandCursor)
btn_2.setGeometry(50, 100, 150, 30)
btn_2.clicked.connect(mostrar_alerta_warning)

btn_3.setCursor(Qt.PointingHandCursor)
btn_3.setGeometry(50, 150, 150, 30)
btn_3.clicked.connect(mostrar_alerta_error)

btn_4.setCursor(Qt.PointingHandCursor)
btn_4.clicked.connect(mostrar_alerta_question)
btn_4.setGeometry(50, 200, 150, 30)

ventana.show()

sys.exit(app.exec_())