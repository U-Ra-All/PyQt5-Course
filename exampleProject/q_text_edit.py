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

        self.ted = QTextEdit()
        self.ted.setText('0123456789012345678901234567890123456789012345678901234567890123456789')
        self.lytMain.addWidget(self.ted)

        self.btnBackground = QPushButton('Set Background Color')
        self.lytMain.addWidget(self.btnBackground)
        self.btnBackground.clicked.connect(self.evt_btn_background_clicked)

        self.btnHtml = QPushButton('Add HTML')
        self.lytMain.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btn_html_clicked)

        curText = self.ted.textCursor()
        curText.setPosition(15, QTextCursor.MoveAnchor)
        curText.setPosition(25, QTextCursor.KeepAnchor)
        self.ted.setTextCursor(curText)
        self.ted.setTextColor(QColor('green'))

    def evt_btn_background_clicked(self):
        clr = QColorDialog.getColor(QColor('black'))
        self.ted.setTextBackgroundColor(QColor(clr))
        self.ted.setFontPointSize(20)

    def evt_btn_html_clicked(self):
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
        self.ted.setText(html)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
