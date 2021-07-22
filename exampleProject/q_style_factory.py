import random
import sys
import time

from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.btn1 = QPushButton('Button 1')
        self.btn2 = QPushButton('Button 2')
        self.btn3 = QPushButton('Button 3')

        self.chk = QCheckBox('Checkbox')
        self.led1 = QLineEdit('Editable')
        self.led2 = QLineEdit('Read Only')
        self.prg = QProgressBar()
        self.prg.setStyle(QStyleFactory.create('Windows'))
        self.prg.setValue(50)
        self.dial = QDial()
        self.dial.setStyle(QStyleFactory.create('Fusion'))
        self.lst = QListWidget()
        self.lst.addItems(QStyleFactory.keys())
        self.lst.itemDoubleClicked.connect(self.evt_lst_double_clicked)
        self.led2.setReadOnly(True)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btn1)
        self.lytMain.addWidget(self.btn2)
        self.lytMain.addWidget(self.btn3)
        self.lytMain.addWidget(self.chk)
        self.lytMain.addWidget(self.led1)
        self.lytMain.addWidget(self.led2)
        self.lytMain.addWidget(self.prg)
        self.lytMain.addWidget(QSlider())
        self.lytMain.addWidget(self.dial)
        self.lytMain.addWidget(self.lst)

        self.setLayout(self.lytMain)

    def evt_lst_double_clicked(self, item):
        app.setStyle(QStyleFactory.create(item.text()))
        QMessageBox.information(self, 'Set Style', 'You have selected the "{}" style'.format(item.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
