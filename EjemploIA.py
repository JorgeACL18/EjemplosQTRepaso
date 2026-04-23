import sys
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


class Colores(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Colores - Solución Final")
        self.setGeometry(300, 300, 400, 400)  # Un pelo más grande para que se aprecie bien

        # 1. Creamos el Grid
        self.grid = QGridLayout()
        # El spacing es el espacio entre las celdas, ponlo a tu gusto
        self.grid.setSpacing(10)

        # ------- COLUMNA 1 (Izquierda) -------
        # Rojo, Amarillo, Morado. Cada uno en su fila (0, 1, 2)
        self.grid.addWidget(self.crear_panel(QColor(255, 0, 0)), 0, 0)
        self.grid.addWidget(self.crear_panel(QColor(255, 255, 0)), 1, 0)
        self.grid.addWidget(self.crear_panel(QColor(131, 12, 123)), 2, 0)

        # ------- COLUMNA 2 (Centro) -------
        # El Verde que se cree muy importante y ocupa las 3 filas
        # addWidget(widget, fila, columna, filas_que_ocupa, columnas_que_ocupa)
        self.grid.addWidget(self.crear_panel(QColor(0, 127, 0)), 0, 1, 3, 1)

        # ------- COLUMNA 3 (Derecha) -------
        # Aquí es donde estaba el peo. Vamos a ponerlos simple:

        # Rojo 2: Solo en la fila 0
        self.grid.addWidget(self.crear_panel(QColor(255, 0, 0)), 0, 2)

        # FILA 1, COLUMNA 2: ¡LA DEJAMOS VACÍA!
        # Al no poner nada aquí, se verá el fondo gris de la ventana,
        # creando el efecto de separación que sale en tu captura.

        # Morado 2: Solo en la fila 2
        self.grid.addWidget(self.crear_panel(QColor(131, 12, 123)), 2, 2)

        # --- AJUSTE DE PROPORCIONES (IMPORTANTE) ---
        # Si las filas se ven muy flacas, les damos "peso".
        # Esto obliga a que las tres filas tengan la misma importancia.
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 1)

        # También le damos peso a las columnas para que no se achoponen
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 1)
        self.grid.setColumnStretch(2, 1)

        # Contenedor central
        self.container = QWidget()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

    def crear_panel(self, color_obj):
        """Método para crear los cuadros de colores sin repetir código basura."""
        p = QWidget()
        p.setAutoFillBackground(True)
        pal = p.palette()
        pal.setColor(QPalette.ColorRole.Window, color_obj)
        p.setPalette(pal)
        # Le ponemos un tamaño mínimo para que el Grid no lo aplaste
        p.setMinimumSize(50, 50)
        return p


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Colores()
    window.show()
    sys.exit(app.exec())