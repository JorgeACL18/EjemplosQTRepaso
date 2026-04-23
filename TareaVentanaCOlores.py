import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout


class Colores(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colores")
        self.setGeometry(300, 300, 300, 300)

        self.vCaja1 = QVBoxLayout()
        self.vCaja2 = QVBoxLayout()
        self.vCaja3 = QVBoxLayout()
        self.hPrincipal = QHBoxLayout()

        # ------- Rojo -------
        self.cRojo = QColor(255,0,0)
        self.rojo = QWidget()

        self.rojo.setAutoFillBackground(True)
        self.paletaR = self.rojo.palette()
        self.paletaR.setColor(QPalette.ColorRole.Window, self.cRojo)
        self.rojo.setPalette(self.paletaR)

        self.vCaja1.addWidget(self.rojo)
        # ------- Rojo -------

        # ------- Amarillo -------
        self.cYell = QColor(255,255,0)
        self.yell = QWidget()

        self.yell.setAutoFillBackground(True)
        self.paletaY = self.yell.palette()
        self.paletaY.setColor(QPalette.ColorRole.Window, self.cYell)
        self.yell.setPalette(self.paletaY)

        self.vCaja1.addWidget(self.yell)
        # ------- Amarillo -------

        # ------- Morado -------
        self.cMor = QColor(131,12,123)
        self.mor = QWidget()

        self.mor.setAutoFillBackground(True)
        self.paletaMor = self.mor.palette()
        self.paletaMor.setColor(QPalette.ColorRole.Window, self.cMor)
        self.mor.setPalette(self.paletaMor)

        self.vCaja1.addWidget(self.mor)
        # ------- Morado -------

        # ******* SEGUNDA COLUMNA *******
        # ------- Verde -------
        self.cVer = QColor(0,127,0)
        self.ver = QWidget()

        self.ver.setAutoFillBackground(True)
        self.paletaVer = self.ver.palette()
        self.paletaVer.setColor(QPalette.ColorRole.Window, self.cVer)
        self.ver.setPalette(self.paletaVer)

        self.vCaja2.addWidget(self.ver)
        # ------- Verde -------

        # ******* TERCERA COLUMNA *******
        # ------- Rojo -------
        self.cRojo2 = QColor(255,0,0)
        self.rojo2 = QWidget()

        self.rojo2.setAutoFillBackground(True)
        self.paletaR2 = self.rojo2.palette()
        self.paletaR2.setColor(QPalette.ColorRole.Window, self.cRojo2)
        self.rojo2.setPalette(self.paletaR2)

        self.vCaja3.addWidget(self.rojo2)
        # ------- Rojo -------

        # ------- Morado -------
        self.cMor2 = QColor(131,12,123)
        self.mor2 = QWidget()

        self.mor2.setAutoFillBackground(True)
        self.paletaMor2 = self.mor2.palette()
        self.paletaMor2.setColor(QPalette.ColorRole.Window, self.cMor2)
        self.mor2.setPalette(self.paletaMor2)

        self.vCaja3.addWidget(self.mor2)
        # ------- Morado -------

        self.hPrincipal.addLayout(self.vCaja1)
        self.hPrincipal.addLayout(self.vCaja2)
        self.hPrincipal.addLayout(self.vCaja3)
        self.container = QWidget()
        self.container.setLayout(self.hPrincipal)
        self.setCentralWidget(self.container)
        self.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Colores()
    app.exec()