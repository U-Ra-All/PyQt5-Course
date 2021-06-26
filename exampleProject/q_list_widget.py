import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.create_widgets()

        self.setup_layout()

    # Create UI

    def create_widgets(self):
        self.lwgProgrammingTopics = QListWidget()
        self.lwgProgrammingTopics.addItems(['Python', 'Java', 'JavaScript', 'TypeScript', 'HTML', 'CSS',
                                            'Django', 'Flask', 'Data Science', 'Machine Learning', 'Node.js',
                                            'Android Dev', 'iOS Dev', 'Bootstrap', 'Angular', 'React', 'Vue'])
        self.lwgProgrammingTopics.sortItems()
        self.lwgProgrammingTopics.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lwgProgrammingTopics.itemSelectionChanged.connect(self.evt_prog_top_selection)

        self.lwgProgrammingTopicsSelected = QListWidget()
        self.lwgProgrammingTopicsSelected.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lwgProgrammingTopicsSelected.itemSelectionChanged.connect(self.evt_prog_top_selected_selection)

        self.btnAdd = QPushButton('-->')
        self.btnAdd.clicked.connect(self.evt_btn_add_clicked)

        self.btnRemove = QPushButton('<--')
        self.btnRemove.clicked.connect(self.evt_btn_remove_clicked)

        self.btnEnroll = QPushButton('Enroll')
        self.btnEnroll.clicked.connect(self.evt_btn_enroll_clicked)

    def setup_layout(self):
        self.lytMain = QVBoxLayout()
        self.lytLists = QHBoxLayout()
        self.lytButtons = QVBoxLayout()

        self.add_widgets_to_lyt_lists()

        self.add_widgets_to_lyt_main()

        self.add_widgets_to_lyt_buttons()

        self.setLayout(self.lytMain)

    def add_widgets_to_lyt_lists(self):
        self.lytLists.addWidget(self.lwgProgrammingTopics)
        self.lytLists.addLayout(self.lytButtons)
        self.lytLists.addWidget(self.lwgProgrammingTopicsSelected)

    def add_widgets_to_lyt_main(self):
        self.lytMain.addLayout(self.lytLists)
        self.lytMain.addWidget(self.btnEnroll)

    def add_widgets_to_lyt_buttons(self):
        self.lytButtons.addStretch()
        self.lytButtons.addWidget(self.btnAdd)
        self.lytButtons.addWidget(self.btnRemove)
        self.lytButtons.addStretch()

    # Event Handlers (Slots)

    def evt_btn_add_clicked(self):
        lstItems = self.lwgProgrammingTopics.selectedItems()
        for item in lstItems:
            QLWI = self.lwgProgrammingTopics.takeItem(self.lwgProgrammingTopics.row(item))
            # self.lwgProgrammingTopicsSelected.addItem(item.text())
            self.lwgProgrammingTopicsSelected.addItem(QLWI)
            self.btnEnroll.setDefault(True)

    def evt_btn_remove_clicked(self):
        lstItems = self.lwgProgrammingTopicsSelected.selectedItems()
        for item in lstItems:
            QLWI = self.lwgProgrammingTopicsSelected.takeItem(self.lwgProgrammingTopicsSelected.row(item))
            self.lwgProgrammingTopics.addItem(QLWI)
            self.lwgProgrammingTopics.sortItems()
            self.btnEnroll.setDefault(True)

    def evt_prog_top_selection(self):
        self.btnAdd.setDefault(True)

    def evt_prog_top_selected_selection(self):
        self.btnRemove.setDefault(True)

    def evt_btn_enroll_clicked(self):
        if self.lwgProgrammingTopicsSelected.count() == 0:
            QMessageBox\
                .information(self, 'Topics', 'You have not selected any topics. Please select at least one')
        else:
            items = []
            for index in range(self.lwgProgrammingTopicsSelected.count()):
                items.append(self.lwgProgrammingTopicsSelected.item(index).text())
            QMessageBox \
                .information(self, 'Topics', 'You have selected following topics: {}'.format(items))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
