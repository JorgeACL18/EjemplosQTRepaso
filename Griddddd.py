import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QSizePolicy


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")

        grid = QGridLayout()

        btn1 = QPushButton("Botón 1")
        btn2 = QPushButton("Botón 2")
        btn3 = QPushButton("Botón 3")
        btn3.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        btn4 = QPushButton("Botón 4")
        btn5 = QPushButton("Botón 5")
        btn6 = QPushButton("Botón 6")

        grid.addWidget(btn1,0,0,1,1)
        grid.addWidget(btn2,0,1,1,2)
        grid.addWidget(btn3,1,0,2,1)
        grid.addWidget(btn4,1,1,1,2)
        grid.addWidget(btn5,2,1,1,1)
        grid.addWidget(btn6,2,2,1,1)

        centralWidget = QWidget()
        centralWidget.setLayout(grid)
        self.setCentralWidget(centralWidget)

        self.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    app.exec()