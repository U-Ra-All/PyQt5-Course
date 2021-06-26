import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.lytMain = QVBoxLayout()
        self.setLayout(self.lytMain)

        self.tbr = QTextBrowser()
        self.lytMain.addWidget(self.tbr)

        html = """
        <h1>Rainbow Colors</h1>
        <ul>
            <li>Red</li>
            <li><b>Bold Orange</b></li>
            <li>Yellow</li>
            <li><i>Italic Green</i></li>
            <li>Blue</li>
            <li>Indigo</li>
            <li>Violet</li>
        </ul>
        """
        self.tbr.setHtml(html)

        self.btnHtml = QPushButton('Load HTML')
        self.lytMain.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btn_html_clicked)

    def evt_btn_html_clicked(self):
        url = 'html/test_text_browser.html'
        self.tbr.setSource(QUrl.fromLocalFile(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
