"""
Radio Button (Botones de opción):
Este widget permite a los usuarios seleccionar una opción de un conjunto predefinido. A diferencia del widget Button, 
los RadioButtons se utilizan en grupos, y solo se puede seleccionar una opción dentro de ese grupo a la vez.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Valor por defecto para el primer radio button.
opcion: int = 1

#2. Crear los Radiobuttons, indicando a que ventana va a pertenercer.
rb_1: object = QRadioButton(ventana)
rb_2: object = QRadioButton(ventana)

#3. Definir la función controladora.
def mostrar(valor) -> None:
    global opcion
    if (valor != -1):
        opcion = valor
        print(opcion)

#4. Configurar los Radiobuttons.
rb_1.setText("Hombre")
rb_1.setCursor(Qt.PointingHandCursor)
rb_1.setGeometry(50, 50, 100, 30)
rb_1.toggled.connect(lambda valor: mostrar(1 if valor else -1)) #Indicando que cuando se le da click, el valor es 1.

rb_2.setCursor(Qt.PointingHandCursor)
rb_2.setText("Hombre")
rb_2.setGeometry(50, 100, 100, 30)
rb_2.toggled.connect(lambda valor: mostrar(2 if valor else -1)) #Indicando que cuando se le da click, el valor es 2.

#5. Establecer RadioButton seleccionado por defecto.
rb_1.setChecked(True)

#6. Mostrar los RadioButtons.
rb_1.setVisible(True)
rb_2.setVisible(True)

ventana.show()

sys.exit(app.exec_())