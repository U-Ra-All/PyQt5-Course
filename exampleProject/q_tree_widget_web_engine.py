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

        # Create Widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(1)
        self.trwQt.setHeaderLabels(['Qt Class'])
        self.trwQt.itemDoubleClicked.connect(self.evt_trw_qt_double_clicked)

        # Populate Tree

        # Create Top Level Items
        self.twiQWidget = QTreeWidgetItem(self.trwQt, ['QWidget Module'])
        self.twiQGui = QTreeWidgetItem(self.trwQt, ['QGui Module'])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ['QCore Module'])

        # Add SubItems To QWidget Module
        lstQWidget = ['QDialog', 'QLabel', 'QLineEdit', 'QGroupBox', 'QFrame']
        for cls in lstQWidget:
            self.twiQWidget\
                .addChild(QTreeWidgetItem([cls]))

        # Add SubItems To QGui Module
        lstQGui = ['QBitmap', 'QColor', 'QFont', 'QIcon', 'QImage']
        for cls in lstQGui:
            self.twiQGui \
                .addChild(QTreeWidgetItem([cls]))

        # Add SubItems To QCore Module
        lstQCore = ['QThread', 'QDateTime', 'QPixmap', 'QUrl', 'QFile']
        for cls in lstQCore:
            self.twiQCore \
                .addChild(QTreeWidgetItem([cls]))

        # Add SubItems To QDialog SubItem
        twiQDialog = self.trwQt.findItems('QDialog', Qt.MatchRecursive)[0]
        lstQDialog = ['QFileDialog', 'QColorDialog', 'QFontDialog', 'QMessageBox']
        for cls in lstQDialog:
            twiQDialog \
                .addChild(QTreeWidgetItem([cls]))

        # Sort trwQt
        self.trwQt.sortItems(0, Qt.AscendingOrder)

        # Resize the first column
        self.trwQt.setColumnWidth(0, 200)

        # Expand QWidget by default
        self.trwQt.expandItem(self.twiQWidget)

        # Create lytWev Widgets
        self.wev = QWebEngineView()
        self.wev.setUrl(QUrl.fromUserInput('https://doc.qt.io/qt-5/qtmodules.html'))

        self.btnForward = QPushButton('-->')
        self.btnForward.clicked.connect(self.wev.forward)

        self.btnBack = QPushButton('<--')
        self.btnBack.clicked.connect(self.wev.back)

        self.btnHome = QPushButton('Home')
        self.btnHome.clicked.connect(self.evt_btn_home_clicked)

        # Setup Layout
        self.lytMain = QHBoxLayout()

        self.lytTree = QVBoxLayout()
        self.lytTree.addWidget(self.trwQt)

        self.lytButtons = QHBoxLayout()
        self.lytButtons.addWidget(self.btnBack)
        self.lytButtons.addWidget(self.btnForward)
        self.lytButtons.addWidget(self.btnHome)

        self.lytWev = QVBoxLayout()
        self.lytWev.addWidget(self.wev)
        self.lytWev.addLayout(self.lytButtons)

        self.lytMain.addLayout(self.lytTree)
        self.lytMain.addLayout(self.lytWev)

        self.setLayout(self.lytMain)

    # Custom Slots
    def evt_trw_qt_double_clicked(self, twi, col):
        url = 'https://doc.qt.io/qt-5/{}.html'.format(twi.text(0).lower())
        self.wev.setUrl(QUrl.fromUserInput(url))

    def evt_btn_home_clicked(self):
        self.wev.setUrl(QUrl.fromUserInput('https://doc.qt.io/qt-5/qtmodules.html'))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
