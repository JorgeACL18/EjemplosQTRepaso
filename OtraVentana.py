import sys

from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QGroupBox, QListWidget


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXCELeINFO - Hojas")
        self.setFixedSize(500,300)

        self.grid = QGridLayout()
        self.vBox = QVBoxLayout()
        self.hBox = QHBoxLayout()

        self.vis = QLabel("Hojas Visibles")
        self.ocu = QLabel("Hojas Ocultas")
        self.mos = QPushButton("<< Mostrar")
        self.inv = QPushButton("Ocultar >>")
        self.grid.addWidget(self.vis,0,0)
        self.grid.addWidget(self.ocu,0,2)
        self.grid.addLayout(self.vBox,1,1)
        self.vBox.addWidget(self.mos)
        self.vBox.addWidget(self.inv)
        self.inv.clicked.connect(self.ocultarHoja)
        self.mos.clicked.connect(self.mostrarHoja)

        self.listVis = QListWidget()
        self.listOcu = QListWidget()
        self.listVis.addItems(["Hoja 1", "Hoja 2", "Hoja 3"])
        self.listOcu.addItems(["Hoja 4", "Hoja 5", "Hoja 6"])
        self.grid.addWidget(self.listVis, 1,0,1,1)
        self.grid.addWidget(self.listOcu,1,2,1,1)

        self.grid.addLayout(self.hBox, 2,2)
        self.cerrar = QPushButton("Cerrar")
        self.hBox.addWidget(self.cerrar)
        self.cerrar.clicked.connect(self.close)

        self.container = QWidget()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)
        self.setVisible(True)

    def ocultarHoja(self):
        item = self.listVis.currentItem()

        if item:
            fila = self.listVis.row(item)
            item_extraido = self.listVis.takeItem(fila)
            self.listOcu.addItem(item_extraido)

    def mostrarHoja(self):
        item = self.listOcu.currentItem()

        if item:
            fila = self.listOcu.row(item)
            item_extraido = self.listOcu.takeItem(fila)
            self.listVis.addItem(item_extraido)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    app.exec()