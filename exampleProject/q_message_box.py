import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Message', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # res = QMessageBox.question(self, 'Disk Full', 'Your disk drive is almost full')
        # if res == QMessageBox.Yes:
        #     QMessageBox.information(self, '', "You've clicked 'Yes' button")
        # elif res == QMessageBox.No:
        #     QMessageBox.information(self, '', "You've clicked 'No' button")
        msgDiskFull = QMessageBox()
        msgDiskFull.setText('Your hard drive is almostfull')
        msgDiskFull.setDetailedText('Please free up disk space')
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setWindowTitle('Full Drive')
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
