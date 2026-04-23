import sys

from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QGroupBox, QListWidget


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXCELeINFO - Hojas")

        self.grid = QGridLayout()
        self.vis = QLabel("Hojas Visibles")
        self.ocu = QLabel("Hojas Ocultas")
        self.mos = QPushButton("<< Mostrar")
        self.inv = QPushButton("Ocultar >>")
        self.grid.addWidget(self.vis,0,0,1,1)
        self.grid.addWidget(self.ocu,0,2,1,1)
        self.grid.addWidget(self.mos,1,1,1,1)
        self.grid.addWidget(self.inv,2,1,1,1)

        self.listVis = QListWidget()
        self.listOcu = QListWidget()
        self.listVis.addItems(["Hoja 1", "Hoja 2", "Hoja 3"])
        self.listOcu.addItems(["Hoja 4", "Hoja 5", "Hoja 6"])
        self.grid.addWidget(self.listVis, 1,0,1,1)
        self.grid.addWidget(self.listOcu,1,2,1,1)

        self.container = QWidget()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)
        self.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    app.exec()