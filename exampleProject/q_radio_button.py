import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.lbl = QLabel('Label Text', self)
        self.lbl.setStyleSheet('color:red; font-size: 10px')
        self.lbl.move(50, 20)
        self.lbl.resize(100, 30)

        # Color Button Group
        self.btgColor = QButtonGroup()

        self.rbtRed = QRadioButton('Red', self)
        self.rbtRed.move(50, 70)
        self.rbtRed.setChecked(True)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtRed)

        self.rbtGreen = QRadioButton('Green', self)
        self.rbtGreen.move(50, 100)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtGreen)

        self.rbtBlue = QRadioButton('Blue', self)
        self.rbtBlue.move(50, 130)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtBlue)

        # Text Size Button Group
        self.btgTextSize = QButtonGroup()

        self.rbtSmall = QRadioButton('Small Text', self)
        self.rbtSmall.move(150, 70)
        self.rbtSmall.setChecked(True)
        self.rbtSmall.clicked.connect(self.evt_rbt_clicked)
        self.btgTextSize.addButton(self.rbtSmall, 10)

        self.rbtMedium = QRadioButton('Medium Text', self)
        self.rbtMedium.move(150, 100)
        self.rbtMedium.clicked.connect(self.evt_rbt_clicked)
        self.btgTextSize.addButton(self.rbtMedium, 15)

        self.rbtLarge = QRadioButton('Large Text', self)
        self.rbtLarge.move(150, 130)
        self.rbtLarge.clicked.connect(self.evt_rbt_clicked)
        self.btgTextSize.addButton(self.rbtLarge, 20)

    def evt_rbt_clicked(self):
        checked_btg_color_rbt = self.btgColor.checkedButton()
        checked_btg_text_size_rbt_id = self.btgTextSize.checkedId()
        str_style_sheet = 'color:' + checked_btg_color_rbt.text() + '; font-size:' \
                          + str(checked_btg_text_size_rbt_id) + 'px'
        print(str_style_sheet)
        self.lbl.setStyleSheet(str_style_sheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
