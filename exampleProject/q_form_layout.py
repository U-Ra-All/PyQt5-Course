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
        self.ledFirstName = QLineEdit('John')
        self.ledLastName = QLineEdit('Doe')
        self.dteStarted = QDateTimeEdit()
        self.spbAge = QSpinBox()
        self.btnSubmit = QPushButton('Submit')

        # Setup Layout
        self.mainLayout = QFormLayout()
        self.mainLayout.setLabelAlignment(Qt.AlignLeft)
        self.mainLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.mainLayout.addRow('First Name: ', self.ledFirstName)
        self.mainLayout.addRow('Last Name: ', self.ledLastName)
        self.mainLayout.addRow('Date started: ', self.dteStarted)
        self.mainLayout.addRow('Age: ', self.spbAge)
        self.mainLayout.addRow('', self.btnSubmit)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
