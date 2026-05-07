import sys

from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QGroupBox, QListWidget, QTabWidget, QCheckBox, QRadioButton, QSlider, QTextEdit, \
    QComboBox, QTableWidget, QTableView


# Aquí creas tu "molde" para los datos, igual que en Java usas interfaces o clases abstractas.
class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__() # Inicializamos la clase padre para que no se rompa nada.
        self.tabla = tabla # Guardamos la lista de listas que contiene los datos.

    def rowCount(self, index):
        return len(self.tabla) # Le dice a la tabla cuántas filas debe dibujar.

    def columnCount(self, index):
        return len(self.tabla[0]) # Le dice cuántas columnas tiene cada fila.

    def data(self, index, role):
        # Esta función es la que llena las celdas. Se llama cada vez que la tabla necesita mostrar algo.
        if index.isValid(): # Verificamos que el índice no sea una vaina loca.
            if role == Qt.ItemDataRole.DisplayRole: # Solo nos interesa el rol de "mostrar texto".
                dataGrid = self.tabla[index.row()][index.column()] # Sacamos el dato de nuestra lista.
                return dataGrid # ¡Toma tu dato y muéstralo!


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo")
        self.setMinimumSize(434, 434)

        self.datos = [['Nombre', 'Dni', 'Género', 'Fallecido'],
                      ['Ana', '1234R', 'Femenino', 'True'],
                      ['Pedro', '5678P', 'Masculino', 'False'],
                      ['Luis', '91011L', 'Masculino', 'False']]

        self.grid = QGridLayout()
        self.vBox = QVBoxLayout()
        self.hBox = QHBoxLayout()

        self.grid.addLayout(self.vBox,3,0,-1,-1)

        self.nombre = QLabel("Nombre")
        self.dni = QLabel("DNI")
        self.genero = QLabel("Género")
        self.fallecido = QLabel("Fallecido")

        self.nomEnt = QLineEdit()
        self.dniEnt = QLineEdit()
        self.generoEnt = QComboBox()
        self.woke = ['Indefinido','Masculino', 'Femenino', 'Otro']
        self.generoEnt.addItems(self.woke)
        self.fallecidoEnt = QCheckBox()

        self.grid.addWidget(self.nombre,0,0)
        self.grid.addWidget(self.nomEnt,0,1)

        self.grid.addWidget(self.dni,0,2)
        self.grid.addWidget(self.dniEnt,0,3)

        self.grid.addWidget(self.genero,1,0)
        self.grid.addWidget(self.generoEnt,1,1)

        self.grid.addWidget(self.fallecido,1,2)
        self.grid.addWidget(self.fallecidoEnt,1,3)

        self.grid.addLayout(self.hBox,2,0,1,-1)
        self.bot1 = QPushButton("Añadir")
        self.bot2 = QPushButton("Modificar")
        self.bot3 = QPushButton("Aceptar")
        self.bot4 = QPushButton("Cancelar")
        self.hBox.addWidget(self.bot1)
        self.hBox.addWidget(self.bot2)
        self.hBox.addWidget(self.bot3)
        self.hBox.addWidget(self.bot4)


        self.tView = QTableView() #Mi error de antes estaba aquí ya que puse QTableWidget() en vez de QTableView()
        modelo = ModeloTabla(self.datos)
        self.tView.setModel(modelo)
        self.vBox.addWidget(self.tView)

        self.container = QWidget()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)
        self.show()

    def editAct(self, activo):
        self.bot3.setEnabled(activo)
        self.bot4.setEnabled(activo)

        self.bot1.setEnabled(not activo)
        self.bot2.setEnabled(not activo)

    def addData(self):
        nombre = self.nomEnt.text()
        dni = self.dniEnt.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()