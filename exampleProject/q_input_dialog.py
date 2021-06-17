import sys
from PyQt5.QtWidgets import *  # imports section


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Input', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        s_color, b_ok = QInputDialog.getItem(self, 'Title', 'Enter your favorite color: ', colors)
        if b_ok:
            QMessageBox.information(self, 'Color', 'Your favorite color is ' + s_color)
        else:
            QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
