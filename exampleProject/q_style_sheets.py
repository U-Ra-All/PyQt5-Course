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

        style_sheet = """
            QPushButton {
                background-color: green;
                color: yellow;
                border-radius: 5px; 
                padding: 2px;
                margin: 10px
            }
            
            QPushButton:default {
                background-color: red; 
                color: white;
                border-radius: 5px; 
                padding: 2px
            }
            
            QPushButton:default:hover {
                background-color: white; 
                color: black;
                border-radius: 5px; 
                padding: 2px
            }
            
            QPushButton:hover {
                background-color: red; 
                color: white;
                border-radius: 5px; 
                border: 3px solid #000000;
                padding: 2px
            }
            
            QCheckBox {
                background-color: orange;
                color: white;
            }
            
            QCheckBox:checked {
                background-color: white;
                color: orange;
            }
            
            QCheckBox::indicator {
                background-color: yellow;
                color: orange;
            }
            
            QCheckBox::indicator:checked {
                background-color: green;
                color: orange;
            }
            
            QLineEdit:read-only {
                color: grey;
                font-style: italic;
            }
        """

        self.setStyleSheet(style_sheet)

        self.btn1 = QPushButton('Button 1')
        self.btn2 = QPushButton('Button 2')
        self.btn3 = QPushButton('Button 3')

        self.chk = QCheckBox('Checkbox')
        self.led1 = QLineEdit('Editable')
        self.led2 = QLineEdit('Read Only')
        self.led2.setReadOnly(True)

        # self.btn3.setStyleSheet('background-color: green; border-radius: 5px; padding: 2px')

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btn1)
        self.lytMain.addWidget(self.btn2)
        self.lytMain.addWidget(self.btn3)
        self.lytMain.addWidget(self.chk)
        self.lytMain.addWidget(self.led1)
        self.lytMain.addWidget(self.led2)

        self.setLayout(self.lytMain)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
