import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)
        self.mainLayout = QGridLayout()

        # Create Widgets
        self.btn0 = QPushButton('0')
        self.btn1 = QPushButton('1')
        self.btn2 = QPushButton('2')
        self.btn3 = QPushButton('3')
        self.btn4 = QPushButton('4')
        self.btn5 = QPushButton('5')
        self.btn6 = QPushButton('6')
        self.btn7 = QPushButton('7')
        self.btn8 = QPushButton('8')
        self.btn9 = QPushButton('9')
        self.btnCalc = QPushButton('Calculate')

        self.setup_layout()

    def setup_layout(self):
        # Setup Layout

        self.mainLayout.addWidget(self.btn1, 4, 0)
        self.mainLayout.addWidget(self.btn2, 4, 1)
        self.mainLayout.addWidget(self.btn3, 4, 2)
        self.mainLayout.addWidget(self.btn4, 3, 0)
        self.mainLayout.addWidget(self.btn5, 3, 1)
        self.mainLayout.addWidget(self.btn6, 3, 2)
        self.mainLayout.addWidget(self.btn7, 2, 0)
        self.mainLayout.addWidget(self.btn8, 2, 1)
        self.mainLayout.addWidget(self.btn9, 2, 2)
        self.mainLayout.addWidget(self.btn0, 5, 1)
        self.mainLayout.addWidget(self.btnCalc, 0, 0, 1, 3)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
