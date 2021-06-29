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
        self.resize(700, 300)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.display(0)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet('background-color: red; color: yellow')

        self.sld = QSlider(Qt.Vertical)
        self.sld.valueChanged.connect(self.evt_sld_value_changed)
        self.sld.setTickPosition(QSlider.TicksBothSides)
        self.sld.setTickInterval(20)

        self.dial = QDial()
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)
        self.dial.setNotchTarget(20)
        self.dial.valueChanged.connect(self.evt_sld_value_changed)

        self.lytMain = QVBoxLayout()
        self.setLayout(self.lytMain)

        self.gbxNumSys = QGroupBox()
        self.rbtDec = QRadioButton('Dec')
        self.rbtBin = QRadioButton('Bin')
        self.rbtOct = QRadioButton('Oct')
        self.rbtHex = QRadioButton('Hex')
        self.lytNumSys = QHBoxLayout()
        self.lytNumSys.addWidget(self.rbtDec)
        self.lytNumSys.addWidget(self.rbtBin)
        self.lytNumSys.addWidget(self.rbtOct)
        self.lytNumSys.addWidget(self.rbtHex)
        self.gbxNumSys.setLayout(self.lytNumSys)
        self.lytMain.addWidget(self.gbxNumSys)
        self.lytLCD = QHBoxLayout()
        self.lytLCD.addWidget(self.sld)
        self.lytLCD.addWidget(self.dial)
        self.lytLCD.addWidget(self.lcd)
        self.lytMain.addLayout(self.lytLCD)

        self.rbtDec.clicked.connect(self.evt_rbt_clicked)
        self.rbtBin.clicked.connect(self.evt_rbt_clicked)
        self.rbtOct.clicked.connect(self.evt_rbt_clicked)
        self.rbtHex.clicked.connect(self.evt_rbt_clicked)

    def evt_rbt_clicked(self):
        sender = self.sender()
        print(sender.text())
        if sender.text() == 'Dec':
            self.lcd.setDecMode()
        elif sender.text() == 'Bin':
            self.lcd.setBinMode()
        elif sender.text() == 'Oct':
            self.lcd.setOctMode()
        elif sender.text() == 'Hex':
            self.lcd.setHexMode()

    def evt_sld_value_changed(self, val):
        self.lcd.display(val)
        self.sld.setValue(val)
        self.dial.setValue(val)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
