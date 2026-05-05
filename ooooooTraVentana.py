import sys

from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QGroupBox, QListWidget, QTabWidget, QCheckBox, QRadioButton, QSlider, QTextEdit, QComboBox


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WindowTitle")
        self.setMinimumSize(500,300)

        self.grid1 = QGridLayout()
        self.grid2 = QGridLayout()
        self.grid3 = QGridLayout()
        self.grid4 = QGridLayout()
        self.vBox = QVBoxLayout()
        self.vBox2 = QVBoxLayout()
        self.vBox3 = QVBoxLayout()
        self.hBox = QHBoxLayout()

        self.btn1 = QPushButton("ToolbarButton")
        self.grid1.addWidget(self.btn1,0,0,1,1)

        self.ChB = QCheckBox("ToolbarCheckButton")
        self.grid1.addWidget(self.ChB,0,1,1,1)

        self.grpBox = QGroupBox("PanelCaption")
        self.grid1.addWidget(self.grpBox,1,0,-1,-1)
        self.grpBox.setLayout(self.grid2)


        # ------ PRIMER CUADRO ------
        self.grpBox2 = QGroupBox("Panel")
        self.grid2.addWidget(self.grpBox2,0,0,1,1)
        self.grpBox2.setLayout(self.grid3)

        self.list = QListWidget()
        self.list.addItems(["Hoja 1", "Hoja 2", "Hoja 3"])
        self.grid3.addWidget(self.list,0,0,1,1)

        self.Radio1 = QRadioButton("RadioButton1")
        self.Radio2 = QRadioButton("RadioButton2")
        self.Radio3 = QRadioButton("RadioButton3")
        self.Radio4 = QRadioButton("InactiveRadio")
        self.Radio4.setDisabled(True)
        self.grid3.addLayout(self.vBox,0,1,1,1)
        self.vBox.addWidget(self.Radio1)
        self.vBox.addWidget(self.Radio2)
        self.vBox.addWidget(self.Radio3)
        self.vBox.addWidget(self.Radio4)

        self.btnButton = QPushButton("Button")
        self.grid3.addWidget(self.btnButton,1,1,1,1)
        # ------ PRIMER CUADRO ------

        # ------ SEGUNDO CUADRO ------
        self.tabs2 = QTabWidget()
        self.grid2.addWidget(self.tabs2,0,1,1,1)
        self.t1 = QWidget()
        self.t1.setLayout(self.grid4)
        self.tabs2.addTab(self.t1,"SelectedTab")
        self.t2 = QWidget()
        self.tabs2.addTab(self.t2,"OtherTab")

        self.grid4.addLayout(self.vBox2,0,0,1,1)
        self.ckBtn1 = QCheckBox("UncheckedCheckBox")
        self.ckBtn2 = QCheckBox("CheckedCheckBox")
        self.ckBtn3 = QCheckBox("InactiveCheckBox")
        self.ckBtn2.setChecked(True)
        self.ckBtn3.setDisabled(True)
        self.vBox2.addWidget(self.ckBtn1)
        self.vBox2.addWidget(self.ckBtn2)
        self.vBox2.addWidget(self.ckBtn3)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(20)
        self.slider.setFixedWidth(200)
        self.grid4.addWidget(self.slider, 1, 0,1,1)
        # ------ SEGUNDO CUADRO ------

        # ------ TERCER CUADRO ------
        self.grid2.addLayout(self.vBox3,1,0,1,1)
        self.txt = QLineEdit()
        self.txt.setPlaceholderText("TextField")
        self.vBox3.addWidget(self.txt)

        self.pss = QLineEdit()
        self.pss.setEchoMode(QLineEdit.EchoMode.Password)
        self.pss.setPlaceholderText("Introduce tu contraseña")
        self.vBox3.addWidget(self.pss)

        self.items = ['ítem 1', 'ítem 2', 'ítem 3']
        self.cmbBox = QComboBox()
        self.cmbBox.addItems(self.items)
        self.vBox3.addWidget(self.cmbBox)
        # ------ TERCER CUADRO ------

        # ------ CUARTO CUADRO ------
        self.grnTxt = QTextEdit()
        self.grnTxt.setPlaceholderText('TextArea')
        self.grid2.addWidget(self.grnTxt,1,1,1,1)


        self.tab1 = QWidget()
        self.tab1.setLayout(self.grid1)
        self.tab2 = QWidget()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab1,"MenuWidget1")
        self.tabs.addTab(self.tab2,"MenuWidget2")

        self.setCentralWidget(self.tabs)
        self.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    app.exec()