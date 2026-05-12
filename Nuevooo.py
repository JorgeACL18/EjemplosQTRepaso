import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QComboBox, QTableView, QCheckBox


# --- MODELO ---
class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    def rowCount(self, index):
        return len(self.tabla)

    def columnCount(self, index):
        return len(self.tabla[0])

    def data(self, index, role):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return self.tabla[index.row()][index.column()]


# --- VISTA Y LÓGICA ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios - Repaso")
        self.setMinimumSize(434, 434)

        # Datos iniciales
        self.datos = [['Ana', '1234R', 'Femenino', 'True'],
                      ['Pedro', '5678P', 'Masculino', 'False'],
                      ['Luis', '91011L', 'Masculino', 'False']]

        self.fila_apuntada = None

        # Componentes
        self.grid = QGridLayout()
        self.nomEnt = QLineEdit()
        self.dniEnt = QLineEdit()
        self.generoEnt = QComboBox()
        self.generoEnt.addItems(['Indefinido', 'Masculino', 'Femenino', 'Otro'])
        self.fallecidoEnt = QCheckBox()

        # Botones
        self.bot1 = QPushButton("Añadir")
        self.bot2 = QPushButton("Modificar")
        self.bot3 = QPushButton("Aceptar")
        self.bot4 = QPushButton("Cancelar")

        # Layout
        self.grid.addWidget(QLabel("Nombre:"), 0, 0)
        self.grid.addWidget(self.nomEnt, 0, 1)
        self.grid.addWidget(QLabel("DNI:"), 0, 2)
        self.grid.addWidget(self.dniEnt, 0, 3)
        self.grid.addWidget(QLabel("Género:"), 1, 0)
        self.grid.addWidget(self.generoEnt, 1, 1)
        self.grid.addWidget(QLabel("Fallecido:"), 1, 2)
        self.grid.addWidget(self.fallecidoEnt, 1, 3)

        hBox = QHBoxLayout()
        hBox.addWidget(self.bot1)
        hBox.addWidget(self.bot2)
        hBox.addWidget(self.bot3)
        hBox.addWidget(self.bot4)

        self.tView = QTableView()
        self.modelo = ModeloTabla(self.datos)
        self.tView.setModel(self.modelo)

        vBox = QVBoxLayout()
        vBox.addLayout(self.grid)
        vBox.addLayout(hBox)
        vBox.addWidget(self.tView)

        container = QWidget()
        container.setLayout(vBox)
        self.setCentralWidget(container)

        # --- CONEXIONES IMPORTANTES ---
        # Detectar cuando escriben para habilitar/deshabilitar "Añadir"
        self.nomEnt.textChanged.connect(self.comprobar_campos)  #
        self.dniEnt.textChanged.connect(self.comprobar_campos)  #

        self.bot1.clicked.connect(self.add_data)
        self.bot2.clicked.connect(self.start_edit)
        self.bot3.clicked.connect(self.save_edit)
        self.bot4.clicked.connect(self.cancel_action)
        self.tView.clicked.connect(self.on_table_click)

        # Estado inicial
        self.edit_mode(False)
        self.bot1.setEnabled(False)  # Empieza apagado hasta que escribas
        self.bot2.setEnabled(False)

    def comprobar_campos(self):
        """Habilita Añadir solo si hay texto y NO estamos editando"""
        nombre_ok = len(self.nomEnt.text().strip()) > 0
        dni_ok = len(self.dniEnt.text().strip()) > 0

        # Si NO estamos en modo edición (botón Aceptar apagado), controlamos Añadir
        if not self.bot3.isEnabled():
            self.bot1.setEnabled(nombre_ok and dni_ok)

    def edit_mode(self, active):
        self.bot3.setEnabled(active)  # Aceptar
        self.bot4.setEnabled(active)  # Cancelar
        self.bot1.setEnabled(not active if not active else False)
        # Si activamos edición, Modificar se apaga. Si desactivamos, depende de si hay algo tocado.
        self.bot2.setEnabled(False if active else self.fila_apuntada is not None)

    def clean_fields(self):
        self.nomEnt.clear()
        self.dniEnt.clear()
        self.generoEnt.setCurrentIndex(0)
        self.fallecidoEnt.setChecked(False)
        self.bot1.setEnabled(False)  # Al limpiar, se vuelve a apagar

    def on_table_click(self, index):
        self.fila_apuntada = index.row()
        if not self.bot3.isEnabled():  # Solo habilitar Modificar si no estamos ya editando
            self.bot2.setEnabled(True)

    def add_data(self):
        self.datos.append([
            self.nomEnt.text(), self.dniEnt.text(),
            self.generoEnt.currentText(), str(self.fallecidoEnt.isChecked())
        ])
        self.modelo.layoutChanged.emit()
        self.clean_fields()

    def start_edit(self):
        if self.fila_apuntada is not None:
            f = self.datos[self.fila_apuntada]
            self.nomEnt.setText(f[0])
            self.dniEnt.setText(f[1])
            self.generoEnt.setCurrentIndex(self.generoEnt.findText(f[2]))
            self.fallecidoEnt.setChecked(f[3] == "True")
            self.edit_mode(True)

    def save_edit(self):
        self.datos[self.fila_apuntada] = [
            self.nomEnt.text(), self.dniEnt.text(),
            self.generoEnt.currentText(), str(self.fallecidoEnt.isChecked())
        ]
        self.modelo.layoutChanged.emit()
        self.clean_fields()
        self.edit_mode(False)
        self.fila_apuntada = None

    def cancel_action(self):
        self.clean_fields()
        self.edit_mode(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())