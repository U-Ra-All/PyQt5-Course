import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.ted = QPlainTextEdit('''
        if __name__ == '__main__':
        app = QApplication(sys.argv)  # create application
        dlgMain = DlgMain()  # create main GUI window
        dlgMain.show()  # show GUI
        sys.exit(app.exec_())  # execute the application
        ''')

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.ted)
        self.setLayout(self.lytMain)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
