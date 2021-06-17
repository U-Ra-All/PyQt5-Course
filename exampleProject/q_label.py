import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.btn = QPushButton('Change Label', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(60, 100)
        self.lbl.resize(320, 176)
        font = QFont('Times New Roman', 24, 75, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        rich_text = """
        <h1>Fruits</h1>
        <ul>
            <li>Apple</li>
            <li>Orange</li>
        </ul>
        """
        self.lbl.setText(rich_text)
        pxm = QPixmap('pictures/orange.jpg').scaled(320, 176)
        self.lbl.setPixmap(pxm)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
