"""
Menu (Menú de Navegación):
El widget Menu en Tkinter es una interfaz gráfica que permite la creación de barras de menú desplegables. Estas barras 
de menú contienen opciones y comandos que los usuarios pueden seleccionar para realizar acciones específicas en la aplicación.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear el la barra de menu y asociarlo con la ventana principal.
mnu: object = ventana.menuBar()

#2. Crear un menu desplegable (Opcional).
seleccionar_desplegable: object = QMenu("Seleccionar", ventana)

#3. Añadir los elementos al menu desplegable (Opcional).
seleccionar_desplegable.addAction("Selección 1")
seleccionar_desplegable.addSeparator()
seleccionar_desplegable.addAction("Selección 2")
seleccionar_desplegable.addSeparator()
seleccionar_desplegable.addAction("Selección 3")
seleccionar_desplegable.addSeparator()
seleccionar_desplegable.addAction("Selección 4")

#4. Añadir los elementos a la barra de menu.
mnu.addMenu("Archivo")
mnu.addMenu("Editar")
mnu.addMenu("Depurar")
mnu.addMenu(seleccionar_desplegable)
mnu.addAction("Salir", ventana.close)

ventana.show()

sys.exit(app.exec_())