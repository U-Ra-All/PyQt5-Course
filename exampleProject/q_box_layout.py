import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        # Create Widgets
        self.lbl_1 = QLabel('Label 1')
        self.btn_2 = QPushButton('Button 2')
        self.led_3 = QLineEdit('Line Edit 3')
        self.cmb_4 = QComboBox()
        self.cmb_4.addItems(['Item 1', 'Item 2', 'Item 3', 'Item 4'])

        # Setup Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.lbl_1)
        self.main_layout.addWidget(self.btn_2)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.led_3)
        self.main_layout.addWidget(self.cmb_4)
        self.main_layout.addStretch()

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
