import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Repaso QT')

        self.cajaV = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.cajaV)

        self.lblSaludo = QLabel("oña")
        self.cajaV.addWidget(self.lblSaludo)

        self.txtNombre = QLineEdit()
        self.txtNombre.setPlaceholderText("Nombre")
        self.cajaV.addWidget(self.txtNombre)

        self.btnSaludar = QPushButton("Saludo")
        self.cajaV.addWidget(self.btnSaludar)
        self.btnSaludar.clicked.connect(self.btn_saludar)

        self.setCentralWidget(self.container)


        self.setVisible(True)

    def btn_saludar(self):
        nombre = self.txtNombre.text()
        if nombre != "":
            self.lblSaludo.setText("Borra cuenta " + nombre)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()