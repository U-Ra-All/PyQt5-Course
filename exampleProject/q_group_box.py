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

        self.lytMain = QHBoxLayout()

        self.gbxCheckable = QGroupBox('Checkable')
        self.rbtCheckTrue = QRadioButton('True')
        self.rbtCheckFalse = QRadioButton('False')
        self.lytCheckable = QVBoxLayout()
        self.lytCheckable.addWidget(self.rbtCheckTrue)
        self.lytCheckable.addWidget(self.rbtCheckFalse)
        self.gbxCheckable.setLayout(self.lytCheckable)
        self.lytMain.addWidget(self.gbxCheckable)
        self.rbtCheckTrue.toggled.connect(self.evt_rbt_check_true_toggled)

        self.gbxFlat = QGroupBox('Flat')
        self.rbtFlatTrue = QRadioButton('True')
        self.rbtFlatFalse = QRadioButton('False')
        self.lytFlat = QVBoxLayout()
        self.lytFlat.addWidget(self.rbtFlatTrue)
        self.lytFlat.addWidget(self.rbtFlatFalse)
        self.gbxFlat.setLayout(self.lytFlat)
        self.lytMain.addWidget(self.gbxFlat)
        self.rbtFlatTrue.toggled.connect(self.evt_rbt_flat_true_toggled)

        self.gbxAlignment = QGroupBox('Alignment')
        self.rbtAlignLeft = QRadioButton('Align Left')
        self.rbtAlignCenter = QRadioButton('Align Center')
        self.rbtAlignRight = QRadioButton('Align Right')
        self.lytAlignment = QVBoxLayout()
        self.lytAlignment.addWidget(self.rbtAlignLeft)
        self.lytAlignment.addWidget(self.rbtAlignCenter)
        self.lytAlignment.addWidget(self.rbtAlignRight)
        self.gbxAlignment.setLayout(self.lytAlignment)
        self.lytMain.addWidget(self.gbxAlignment)
        self.rbtAlignLeft.toggled.connect(self.evt_rbt_align_left_toggled)
        self.rbtAlignCenter.toggled.connect(self.evt_rbt_align_center_toggled)
        self.rbtAlignRight.toggled.connect(self.evt_rbt_align_right_toggled)

        self.setLayout(self.lytMain)

    def evt_rbt_check_true_toggled(self, sld):
        self.gbxCheckable.setCheckable(sld)

    def evt_rbt_flat_true_toggled(self, sld):
        self.gbxFlat.setFlat(sld)

    def evt_rbt_align_left_toggled(self, sld):
        if sld:
            self.gbxAlignment.setAlignment(Qt.AlignLeft)
            self.gbxAlignment.setTitle('Left Alignment')

    def evt_rbt_align_center_toggled(self, sld):
        if sld:
            self.gbxAlignment.setAlignment(Qt.AlignCenter)
            self.gbxAlignment.setTitle('Center Alignment')

    def evt_rbt_align_right_toggled(self, sld):
        if sld:
            self.gbxAlignment.setAlignment(Qt.AlignRight)
            self.gbxAlignment.setTitle('Right Alignment')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
