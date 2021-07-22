import sys, os
from PyQt5.QtWidgets import *  # imports section
from ui.menu_demo_ui import *
import q_tree_widget_web_engine


class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.splitter)
        self.centralwidget.setLayout(self.lytMain)

        self.btn = QPushButton('Click Me')
        self.statusbar.addPermanentWidget(self.btn)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create('Windows'))
        self.statusbar.addPermanentWidget(self.prg)

        self.listWidget.addItems(os.listdir('ui/'))

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.actionHelp.triggered.connect(self.evt_help_triggered)
        self.listWidget.itemDoubleClicked.connect(self.evt_list_widget_clicked)

    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, 'Open File', 'ui/', 'Any Text Files (*.*)')
        if sFile:
            f = open(sFile)
            self.plainTextEdit.setPlainText(f.read())
        else:
            print('Action was cancelled')

    def evt_quit_triggered(self):
        sys.exit(0)

    def evt_btn_display_clicked(self):
        self.statusbar.showMessage(self.ledMessage.text(), self.spbMsec.value())

    def evt_list_widget_clicked(self, lwi):
        # QMessageBox.information(self, 'File', 'You have selected {}'.format(lwi.text()))
        f = open('ui/' + lwi.text())
        self.plainTextEdit.setPlainText(f.read())

    def evt_help_triggered(self):
        dlgTrw = q_tree_widget_web_engine.DlgMain()
        dlgTrw.show()
        dlgTrw.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    menuMain = MenuMain()  # create main GUI window
    menuMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
