import random
import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        # Create Widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(3)
        self.trwQt.setHeaderLabels(['Qt Class', 'Methods', 'Signals'])
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
                .addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add SubItems To QGui Module
        lstQGui = ['QBitmap', 'QColor', 'QFont', 'QIcon', 'QImage']
        for cls in lstQGui:
            self.twiQGui \
                .addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add SubItems To QCore Module
        lstQCore = ['QThread', 'QDateTime', 'QPixmap', 'QUrl', 'QFile']
        for cls in lstQCore:
            self.twiQCore \
                .addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add SubItems To QDialog SubItem
        twiQDialog = self.trwQt.findItems('QDialog', Qt.MatchRecursive)[0]
        lstQDialog = ['QFileDialog', 'QColorDialog', 'QFontDialog', 'QMessageBox']
        for cls in lstQDialog:
            twiQDialog \
                .addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Sort trwQt
        self.trwQt.sortItems(0, Qt.AscendingOrder)

        # Resize the first column
        self.trwQt.setColumnWidth(0, 200)

        # Expand QWidget by default
        self.trwQt.expandItem(self.twiQWidget)

        # Setup Layout
        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.trwQt)

        self.setLayout(self.lytMain)

    # Custom Slots
    def evt_trw_qt_double_clicked(self, twi, col):
        QMessageBox.information(self, 'Qt Classes', 'You have clicked on the {} class'.format(twi.text(0)))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
