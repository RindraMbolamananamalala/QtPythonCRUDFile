# -*- coding: utf-8 -*-

"""
ui_Open_Wires.py: The python file dedicated to the graphical definition of the Open Wires Window of the
application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow


class UI_OpenWires(Ui_TreatmentWindow):

    def get_label_left_part(self) -> QLabel:
        return self.label_left_part

    def get_label_middle_part(self) -> QLabel:
        return self.label_middle_part

    def get_label_right_part(self) -> QLabel:
        return self.label_right_part

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_OpenWires, self).__init__(main_window)

        # All the first Label Icon has to be disabled at this level
        self.label_icon_1.setDisabled(True)
        self.label_icon_1.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon1_inactive.png"))

        # Configuring the Open Wires' label
        self.label_open_wires = QLabel(self.column_treatment)
        self.label_open_wires.setObjectName(u"label_open_wires")
        self.label_open_wires.setGeometry(QRect(40, 50, 300, 50))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_open_wires.setFont(font4)
        self.label_open_wires.setStyleSheet(u"color: white;")

        # Configuring the label_open_wires' Left Part's label
        self.label_left_part = QLabel(self.column_treatment)
        self.label_left_part.setObjectName(u"label_left_part")
        self.label_left_part.setGeometry(QRect(40, 120, 615, 400))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(16)
        self.label_left_part.setFont(font5)
        self.label_left_part.setStyleSheet(u"QLabel{color: white;}QLabel QWidget{color: black;};")
        self.label_left_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Configuring the Open Wires' Middle part's label
        self.label_middle_part = QLabel(self.column_treatment)
        self.label_middle_part.setObjectName(u"label_middle_part")
        self.label_middle_part.setGeometry(QRect(660, 120, 400, 425))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(16)
        self.label_middle_part.setFont(font7)
        self.label_middle_part.setStyleSheet(u"color: white;")
        self.label_middle_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Configuring the Open Wires' Right part's label
        self.label_right_part = QLabel(self.column_treatment)
        self.label_right_part.setObjectName(u"label_right_part")
        self.label_right_part.setGeometry(QRect(1055, 120, 615, 400))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(14)
        self.label_right_part.setFont(font8)
        self.label_right_part.setStyleSheet(u"color: white;")
        self.label_right_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        # Temporary data are used to feed the UI, will be seriously managed latter
        self.label_open_wires.setText(QCoreApplication.translate("MainWindow", u"Open Wires", None))

