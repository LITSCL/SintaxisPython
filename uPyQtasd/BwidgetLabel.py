"""
Label (Etiqueta):
La clase Label se utiliza para mostrar texto o imágenes en una ventana de Qt. Se Puede configurar el texto que 
se muestra en la etiqueta y ajustar su estilo, como la fuente, el color, etc.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

app: object = QApplication(sys.argv)

ventana: object = QMainWindow()
ventana.setWindowTitle("Ventana Principal")
ventana.setGeometry(100, 100, 750, 450)

#1. Crear el Label.
lbl: object = QLabel(ventana)

#2. Configurar el Label.
lbl.setText("Hola, soy el texto del Label.")
lbl.setStyleSheet("color: white; background-color: black;") #Estilos CSS del Label.
lbl.setFixedSize(200, 100) #Establecer un tamaño fijo para el Label.
lbl.setAlignment(Qt.AlignCenter) #Alinear el texto al centro del Label.
lbl.setCursor(Qt.PointingHandCursor) #Indica la forma del cursor cuando se pasa el mouse por encima.

#3. Mostrar el Label.
lbl.setVisible(True)

ventana.show()

sys.exit(app.exec_())