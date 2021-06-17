import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.chk_enabled = QCheckBox('Enabled', self)
        self.chk_enabled.move(50, 50)
        self.chk_enabled.setChecked(True)
        self.chk_enabled.toggled.connect(self.evt_chk_enabled_toggled)

        self.chk_3_states = QCheckBox('3 state checkbox', self)
        self.chk_3_states.move(50, 70)
        self.chk_3_states.setTristate(True)
        self.chk_3_states.stateChanged.connect(self.evt_chk_3_states_changed)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(60, 100)
        self.lbl.resize(320, 176)
        font = QFont('Times New Roman', 24, 75, True)
        self.lbl.setFont(font)

    def evt_chk_enabled_toggled(self, is_checked):
        if is_checked:
            self.lbl.setEnabled(True)
        else:
            self.lbl.setDisabled(True)

    def evt_chk_3_states_changed(self, state):
        if state == 0:
            QMessageBox.information(self, 'State', 'Unchecked')
        elif state == 1:
            QMessageBox.information(self, 'State', 'Partially checked')
        else:
            QMessageBox.information(self, 'State', 'Checked')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
