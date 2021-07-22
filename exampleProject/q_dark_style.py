import sys
from PyQt5.QtWidgets import *  # imports section
import qdarkstyle


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.dark = False

        self.gbxDarkStyle = QGroupBox('Dark Style')
        self.gbxDarkStyle.setCheckable(True)

        self.rbtNormal = QRadioButton('Normal')
        self.rbtNormal.setChecked(True)
        self.rbtNormal.setStyleSheet(styleRadioButton(self.dark))
        self.rbtNormal.toggled.connect(self.evt_rbt_normal_toggled)

        self.rbtDark = QRadioButton('Dark Style')
        self.rbtDark.setStyleSheet(styleRadioButton(self.dark))

        self.txtStyle = QPlainTextEdit()

        self.lytButtons = QVBoxLayout()
        self.lytButtons.addWidget(self.rbtNormal)
        self.lytButtons.addWidget(self.rbtDark)

        self.lytGroupBox = QHBoxLayout()
        self.lytGroupBox.addLayout(self.lytButtons)
        self.lytGroupBox.addWidget(self.txtStyle)

        self.gbxDarkStyle.setLayout(self.lytGroupBox)

        self.lytMain = QHBoxLayout()
        self.lytMain.addWidget(self.gbxDarkStyle)

        self.setLayout(self.lytMain)

    def evt_rbt_normal_toggled(self, checked):
        if checked:
            app.setStyleSheet('')
            self.dark = False
        else:
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.dark = True

        self.txtStyle.setPlainText(app.styleSheet())
        self.rbtNormal.setStyleSheet(styleRadioButton(self.dark))
        self.rbtDark.setStyleSheet(styleRadioButton(self.dark))

def styleRadioButton(dark):
    if dark:
        sStyle = '''
        QRadioButton {
            background-color: white;
            color: black;
            padding: 10px;
        }
        QRadioButton::indicator {
            background-color: white;
            color: black;
            padding: 10px;
        }
    '''
    else:
        sStyle = '''
        QRadioButton {
            background-color: black;
            color: white;
            padding: 10px;
        }
        QRadioButton::indicator {
            background-color: black;
            color: white;
            padding: 10px;
        }
    '''

    return sStyle


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
