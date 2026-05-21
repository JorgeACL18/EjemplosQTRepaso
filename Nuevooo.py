import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QComboBox, QTableView, QCheckBox
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter, A4
from reportlab.rl_settings import showBoundary


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

    def data(self, index, role):
        if not index.isValid():
            return None

        fila = index.row()
        col = index.column()
        valor = self.tabla[fila][col]

        # 1. El texto que se verá (incluido el de la columna 3)
        if role == Qt.ItemDataRole.DisplayRole:
            return valor

        # 2. La imagen que se añade como "decoración"
        if role == Qt.ItemDataRole.DecorationRole:
            if col == 3 and fila >= 1:
                # Si el valor es "True", ponemos el tic; si no, la equis
                return QIcon("tic.png") if valor == "True" else QIcon("equis.png")

# --- VISTA Y LÓGICA ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios - Repaso")
        self.setMinimumSize(434, 434)

        # Datos iniciales
        self.datos = [['Nombre', 'DNI', 'Genero', 'Fallecido'],
                    ['Ana', '1234R', 'Femenino', 'True'],
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
        self.bot5 = QPushButton("Guardar PDF")

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
        hBox.addWidget(self.bot5)

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
        self.bot5.clicked.connect(self.pdf)
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

        self.dniEnt.setEnabled(not active)

    def clean_fields(self):
        self.nomEnt.clear()
        self.dniEnt.clear()
        self.generoEnt.setCurrentIndex(0)
        self.fallecidoEnt.setChecked(False)
        self.bot1.setEnabled(False)
        self.dniEnt.setEnabled(True)# Al limpiar, se vuelve a apagar

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
        # Primero chequeamos si de verdad hay una fila seleccionada, no sea que estemos editando el aire
        if self.fila_apuntada is not None:
            # Sacamos los datos de la lista usando el índice de la fila que marcaste
            f = self.datos[self.fila_apuntada]

            # Ponemos el nombre en su sitio
            self.nomEnt.setText(f[0])

            # Aquí ponemos el DNI en su cuadro
            self.dniEnt.setText(f[1])

            # ¡OJO AQUÍ! Esta es la línea mágica para que no te toquen el DNI
            # Ponemos el campo en modo 'Solo lectura' para que lo vean pero no lo jodan
            self.dniEnt.setReadOnly(True)

            # También podrías usar setEnabled(False), pero se pone gris y a veces es un fastidio leerlo

            # Ajustamos el género en el combo box
            self.generoEnt.setCurrentIndex(self.generoEnt.findText(f[2]))

            # Marcamos si el bicho está fallecido o no
            self.fallecidoEnt.setChecked(f[3] == "True")

            # Activamos el modo edición (seguro aquí habilitas/deshabilitas botones)
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

    def pdf(self):
        self.crearPDF()
        print("Informe generado")

    def crearPDF (self):
        guion = []

        hojaEstilo = getSampleStyleSheet()
        cabecera = hojaEstilo["Heading4"]
        cabecera.pageBreakBefore = 0
        cabecera.keepWithNext = 0
        cabecera.backColor = colors.blanchedalmond

        parrafo = Paragraph("Listado de usuarios", cabecera)

        guion.append(parrafo)

        textoNormal = hojaEstilo["BodyText"]
        parrafo2 = Paragraph("A continuación se listan los usuarios recogidos en la aplicación", textoNormal)
        guion.append(parrafo2)
        guion.append(Spacer (0,20))

        tic = Image("tic.png", width=16, height=16)
        ex = Image("equis.png", width=16, height=16)

        datos = []
        datos.append(self.modelo.tabla[0])
        for i in range(1, len(self.modelo.tabla)):
            if self.modelo.tabla[i][3] == "True":
                datos.append(self.modelo.tabla[i])
                datos[i][3] = tic
            else :
                datos.append(self.modelo.tabla[i])
                datos[i][3] = ex

        tabla = Table(datos)

        columnas = len(self.modelo.tabla[0])
        estilo = [("TEXTCOLOR", (0,0), (columnas-1,0), colors.darkslategrey),
                  ("TEXTCOLOR", (0,1), (columnas-1,-1), colors.dimgrey),
                  ("BOX", (0,1), (-1,-1), 0.25, colors.grey),
                  ("INNERGRID", (0,1), (-1,-1), 0.15, colors.lightgrey),
                  ("ALIGN", (3,1), (3,-1), 'CENTER')]
        for i in range(1, len(self.modelo.tabla)):
            if self.modelo.tabla[i][2] == "Masculino":
                estilo.append(('BACKGROUND', (2,i), (2,i), colors.lightcyan))
            elif self.modelo.tabla[i][2] == "Femenino":
                estilo.append(('BACKGROUND', (2,i), (2,i), colors.lightpink))
            elif self.modelo.tabla[i][2] == "Indefinido":
                estilo.append(('BACKGROUND', (2,i), (2,i), colors.palegreen))
            elif self.modelo.tabla[i][2] == "Otro":
                estilo.append(('BACKGROUND', (2,i), (2,i), colors.lightgoldenrodyellow))



        tabla.setStyle(estilo)
        guion.append(tabla)

        documento = SimpleDocTemplate("tablaUsuario.pdf", pagesize = A4, showBoundary = 1)
        documento.build(guion)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())