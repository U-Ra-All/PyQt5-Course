import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.dteDate = QDateTimeEdit(QDate().currentDate(), self)
        self.dteDate.move(50, 50)
        self.dteDate.setCalendarPopup(True)

        self.dteTime = QDateTimeEdit(QTime.currentTime(), self)
        self.dteTime.move(50, 80)

        self.dteDateTime = QDateTimeEdit(QDateTime().currentDateTime(), self)
        self.dteDateTime.move(50, 110)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
