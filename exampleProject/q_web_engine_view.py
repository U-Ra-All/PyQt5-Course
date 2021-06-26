import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(1200, 800)

        self.lytMain = QVBoxLayout()
        self.setLayout(self.lytMain)

        self.wev = QWebEngineView()
        self.lytMain.addWidget(self.wev)

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
        self.wev.setHtml(html)

        self.ledClass = QLineEdit('QWebEngineView')
        self.lytMain.addWidget(self.ledClass)

        self.btnHtml = QPushButton('Go To The Page')
        self.lytMain.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btn_html_clicked)

        self.btnLocalHtml = QPushButton('Load HTML File')
        self.lytMain.addWidget(self.btnLocalHtml)
        self.btnLocalHtml.clicked.connect(self.evt_btn_local_html_clicked)

    def evt_btn_html_clicked(self):
        url = 'https://doc.qt.io/qt-5/{}.html'.format(self.ledClass.text().lower())
        self.wev.setUrl(QUrl.fromUserInput(url))

    def evt_btn_local_html_clicked(self):
        url = '/Users/yuriyallakhverdov/PyCharmProjects/PyQt5Course/exampleProject/html/test_text_browser.html'
        self.wev.setUrl(QUrl.fromLocalFile(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
