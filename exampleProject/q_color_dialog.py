import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Choose Color', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        color = QColorDialog.getColor(QColor(190, 0, 255, 255), self, 'Choose Color')
        print(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
