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

        self.lytMain = QHBoxLayout()
        self.setLayout(self.lytMain)

        self.lblColor = QLabel()
        self.pxm = QPixmap(50, 50)

        self.lstColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.pxm.fill(QColor(random.choice(self.lstColors)))
        self.lblColor.setPixmap(self.pxm)
        self.lytMain.addWidget(self.lblColor)

        self.btnStart = QPushButton('Start')
        self.lytMain.addWidget(self.btnStart)
        self.btnStart.clicked.connect(self.evt_btn_start_clicked)

        self.btnStop = QPushButton('Stop')
        self.lytMain.addWidget(self.btnStop)
        self.btnStop.clicked.connect(self.evt_btn_stop_clicked)

        self.tmr = QTimer()
        self.tmr.timeout.connect(self.evt_tmr_timeout)

    def evt_tmr_timeout(self):
        self.pxm.fill(QColor(random.choice(self.lstColors)))
        self.lblColor.setPixmap(self.pxm)
        print(random.choice(self.lstColors))

    def evt_btn_start_clicked(self):
        self.tmr.start(100)

    def evt_btn_stop_clicked(self):
        self.tmr.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
