import sys
from PyQt5.QtWidgets import *  # imports section
from ui.group_box2 import *


class DlgMain(QDialog, Ui_Dialog):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)

        self.rbtCheckTrue.toggled.connect(self.evt_rbt_check_true_toggled)
        self.rbtFlatTrue.toggled.connect(self.evt_rbt_flat_true_toggled)

    def evt_rbt_check_true_toggled(self, checked):
        self.gbxCheckable.setCheckable(checked)

    def evt_rbt_flat_true_toggled(self, checked):
        self.gbxFlat.setFlat(checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
