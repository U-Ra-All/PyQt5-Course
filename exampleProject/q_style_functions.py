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

        self.btnAdd1 = QPushButton('Add')
        self.btnAdd1.setStyleSheet(styleAddButton())
        self.btnAdd2 = QPushButton('Add')
        self.btnAdd2.setStyleSheet(styleAddButton())
        self.btnDelete1 = QPushButton('Delete')
        self.btnDelete1.setStyleSheet(styleDeleteButton())
        self.btnDelete2 = QPushButton('Delete')
        self.btnDelete2.setStyleSheet(styleDeleteButton())

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btnAdd1)
        self.lytMain.addWidget(self.btnAdd2)
        self.lytMain.addWidget(self.btnDelete1)
        self.lytMain.addWidget(self.btnDelete2)
        self.setLayout(self.lytMain)

def styleAddButton():
    sStyle = '''
        QPushButton {
            background-color: green;
            border-radius: 5px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: green;
            border-radius: 5px;
            border: 3px solid grey;
            padding: 10px;
        }
    '''
    return sStyle

def styleDeleteButton():
    sStyle = '''
        QPushButton {
            background-color: darkred;
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: darkred;
            color: white;
            border-radius: 5px;
            border: 3px solid grey;
            padding: 10px;
        }
    '''
    return sStyle


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
