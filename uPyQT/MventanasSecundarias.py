import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDialog

#Definir el Frame hijo.
class SecundarioFrame(QDialog):

    #1. Constructor del Secundario Frame.
    def __init__(self, ventana_padre: object) -> None:
        super().__init__(ventana_padre)

        #2 Modificar los parámetros del frame.
        self.setWindowTitle("Ventana Secundaria")
        self.setGeometry(100, 100, 550, 350)

        #3. Crear el layout.
        layout: object = QVBoxLayout(self)

        #4. Crear y configurar los widgets que van dentro del layout.
        lbl: object = QLabel("Contenido del JInternalFrame")
        btn: object = QPushButton("Cerrar")
        btn.clicked.connect(self.cerrar)

        #5. Agregar los widgets al layout.
        layout.addWidget(lbl, alignment = Qt.AlignCenter)
        layout.addWidget(btn, alignment = Qt.AlignCenter)

        #6. Ajustar la posición del frame dentro de su padre.
        self.move(ventana_padre.geometry().center() - self.rect().center())

    #7. Métodos del frame (Se asocian a los widgets).
    def cerrar(self) -> None:
        self.close()

#Definir el Frame padre.
class MainFrame:

    #1. Constructor del Main Frame.
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        #2 Modificar los parámetros del frame.
        self.ventana_principal: object = QMainWindow()
        self.ventana_principal.setWindowTitle("Ventana Principal")
        self.ventana_principal.setGeometry(100, 100, 750, 450)

        #3. Creando el contenedor de widgets principal y asignandolo al frame.
        central_widget: object = QWidget()
        self.ventana_principal.setCentralWidget(central_widget)

        #4. Crear el layout.
        layout: object = QVBoxLayout(central_widget)

        #5. Crear y configurar los widgets que van dentro del layout.
        btn: object = QPushButton("Mostrar Ventana Secundaria")
        btn.clicked.connect(self.mostrar_secundario_frame)

        #6. Agregar los widgets al layout.
        layout.addWidget(btn, alignment = Qt.AlignCenter)

    #7. Método de muetreo del frame principal.
    def mostrar(self) -> None:
        self.ventana_principal.show()
        sys.exit(self.app.exec_())

    #8. Métodos del frame (Se asocian a los widgets).
    def mostrar_secundario_frame(self) -> None:
        secundario_frame: SecundarioFrame = SecundarioFrame(self.ventana_principal) #Creando la instancia de SecundarioFrame.
        secundario_frame.exec_() #Ejecutando el frame secundario.

main_frame: MainFrame = MainFrame()
main_frame.mostrar()