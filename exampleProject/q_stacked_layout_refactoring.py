import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.create_main_widgets()

        self.create_general_widgets()

        self.create_species_widgets()

        self.create_location_widgets()

        self.create_survey_widgets()

        self.setup_layout()

    def setup_layout(self):

        self.setup_main_layout()

        self.add_widgets_to_left_layout()

        self.add_widgets_to_right_layout()

        self.setup_general_widget()

        self.setup_species_widget()

        self.setup_location_widget()

        self.setup_surveys_widget()

        self.setLayout(self.lytMain)

    def evt_cmb_selector_changed(self, idx):
        self.lytRight.setCurrentIndex(idx)

    def create_main_widgets(self):
        # Create Main Widgets
        self.cmbSelector = QComboBox()
        self.cmbSelector.addItems(['General', 'Species', 'Location', 'Surveys'])
        self.cmbSelector.currentIndexChanged.connect(self.evt_cmb_selector_changed)

        self.wdgGeneral = QWidget()
        self.wdgSpecies = QWidget()
        self.wdgLocation = QWidget()
        self.wdgSurveys = QWidget()

    def create_general_widgets(self):
        # General Widgets
        self.lblNestID = QLabel('24')
        self.dteFound = QDateTimeEdit(QDate(2017, 7, 11))
        self.dteLast = QDateTimeEdit(QDate(2021, 6, 19))
        self.chkActive = QCheckBox()

    def create_species_widgets(self):
        # Species Widgets
        self.cmbSpecies = QComboBox()
        self.cmbSpecies.addItem('Rhesus macaque', 123)
        self.cmbSpecies.addItem('Emperor tamarin', 321)
        self.cmbSpecies.addItem('Other', 333)

        self.ledSpecies = QLineEdit()
        self.spbCodes = QSpinBox()
        self.spbCodes.setValue(123)

    def create_location_widgets(self):
        # Location Widgets
        self.spbLatitude = QDoubleSpinBox()
        self.spbLongitude = QDoubleSpinBox()

    def create_survey_widgets(self):
        # Survey Widgets
        self.lstSurveys = QListWidget()
        self.lstSurveys.addItem('02/25/2020 - INACTIVE')
        self.lstSurveys.addItem('03/21/2020 - INACTIVE')
        self.lstSurveys.addItem('05/15/2020 - INACTIVE')
        self.lstSurveys.addItem('06/10/2020 - ACTIVE')
        self.btnAddSurvey = QPushButton('Add Survey')

    def setup_main_layout(self):
        # Setup Main Layout
        self.lytMain = QHBoxLayout()
        self.lytLeft = QVBoxLayout()
        self.lytRight = QStackedLayout()

        self.lytMain.addLayout(self.lytLeft)
        self.lytMain.addLayout(self.lytRight)

    def add_widgets_to_left_layout(self):
        # Add Widgets To Left Layout
        self.lytLeft.addWidget(self.cmbSelector)
        self.lytLeft.addStretch()

    def add_widgets_to_right_layout(self):
        # Add Widgets To Right Layout
        self.lytRight.addWidget(self.wdgGeneral)
        self.lytRight.addWidget(self.wdgSpecies)
        self.lytRight.addWidget(self.wdgLocation)
        self.lytRight.addWidget(self.wdgSurveys)

    def setup_general_widget(self):
        # Setup General Widget
        self.lytGeneral = QFormLayout()
        self.lytGeneral.addRow('Nest ID', self.lblNestID)
        self.lytGeneral.addRow('Date Found', self.dteFound)
        self.lytGeneral.addRow('Date Last Surveyed', self.dteLast)
        self.lytGeneral.addRow('Currently Active', self.chkActive)
        self.wdgGeneral.setLayout(self.lytGeneral)

    def setup_species_widget(self):
        # Setup Species Widget
        self.lytSpecies = QFormLayout()
        self.lytSpecies.addRow('Species', self.cmbSpecies)
        self.lytSpecies.addRow('Species', self.ledSpecies)
        self.lytSpecies.addRow('Codes', self.spbCodes)
        self.wdgSpecies.setLayout(self.lytSpecies)

    def setup_location_widget(self):
        # Setup Location Widget
        self.lytLocation = QFormLayout()
        self.lytLocation.addRow('Latitude', self.spbLatitude)
        self.lytLocation.addRow('Longitude', self.spbLongitude)
        self.wdgLocation.setLayout(self.lytLocation)

    def setup_surveys_widget(self):
        # Setup Surveys Widget
        self.lytSurveys = QVBoxLayout()
        self.lytSurveys.addWidget(self.lstSurveys)
        self.lytSurveys.addWidget(self.btnAddSurvey)
        self.wdgSurveys.setLayout(self.lytSurveys)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
