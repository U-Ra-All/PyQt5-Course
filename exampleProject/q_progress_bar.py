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

        self.prb = QProgressBar()
        self.prb.setTextVisible(True)

        self.btnStart = QPushButton('Start')
        self.btnStart.clicked.connect(self.evt_btn_start_clicked)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.prb)
        self.lytMain.addWidget(self.btnStart)
        self.setLayout(self.lytMain)

    def evt_btn_start_clicked(self):
        for x in range(100):
            print(x)
            time.sleep(0.1)
            self.prb.setValue(x)
            app.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
