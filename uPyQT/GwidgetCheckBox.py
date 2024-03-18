"""
Check Box (Checkbox):
Este widget permite a los usuarios realizar acciones al hacer click en el botón. Se puede asociar una función 
o un comando al botón para que se ejecute cuando el usuario lo presiona.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear los CheckBox, indicando a que ventana va a pertenercer.
chk_1: object = QCheckBox(ventana)
chk_2: object = QCheckBox(ventana)
chk_3: object = QCheckBox(ventana)

#2. Configurar los CheckBoxs.
chk_1.setText("Java")
chk_1.setCursor(Qt.PointingHandCursor)
chk_1.setChecked(False)
chk_1.setGeometry(50, 50, 100, 30)

chk_2.setText("PHP")
chk_2.setCursor(Qt.PointingHandCursor)
chk_2.setChecked(False)
chk_2.setGeometry(50, 70, 100, 30)

chk_3.setText("C++")
chk_3.setCursor(Qt.PointingHandCursor)
chk_3.setChecked(False)
chk_3.setGeometry(50, 90, 100, 30)

#3. Mostrar los CheckBoxs.
chk_1.setVisible(True)
chk_2.setVisible(True)
chk_3.setVisible(True)

ventana.show()

sys.exit(app.exec_())