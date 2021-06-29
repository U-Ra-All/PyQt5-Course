import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(500, 150)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.display(130)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet('background-color: red; color: yellow')
        self.lcd.setBinMode()

        self.lytMain = QHBoxLayout()
        self.lytMain.addWidget(self.lcd)
        self.setLayout(self.lytMain)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
