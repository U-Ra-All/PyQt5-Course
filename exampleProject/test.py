# import sys
# from PyQt5.QtWidgets import *  # imports section
#
# app = QApplication(sys.argv)  # create application
# dlgMain = QDialog()  # create main GUI window
# dlgMain.setWindowTitle('First GUI')
# dlgMain.show()  # show the GUI
#
# sys.exit(app.exec_())  # execute the app

import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second GUI')  # add widgets, set properties
        self.resize(300, 200)

        self.ledText = QLineEdit('Default Text', self)
        self.ledText.move(90, 50)

        self.btnUpdate = QPushButton('Update Window Title', self)
        self.btnUpdate.move(70, 80)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)

    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application



