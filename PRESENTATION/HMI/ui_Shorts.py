# -*- coding: utf-8 -*-

"""
ui_Shorts.py: The python file dedicated to the graphical definition of the Extra Wires - Shorts Window of the
application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow


class UI_Shorts(Ui_TreatmentWindow):

    def get_label_left_part(self) -> QLabel:
        return self.label_left_part

    def get_label_middle_part(self) -> QLabel:
        return self.label_middle_part

    def get_label_right_part(self) -> QLabel:
        return self.label_right_part

    def get_label_lines_treated_counter(self) -> QLabel:
        return self.label_lines_treated_counter

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_Shorts, self).__init__(main_window)

        # All the first 2 Label Icons have to be disabled at this level
        self.label_icon_1.setDisabled(True)
        self.label_icon_1.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon1_crosspinning_inactive.png"))
        self.label_icon_2.setDisabled(True)
        self.label_icon_2.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon2_open_inactive.png"))

        # Configuring the Shorts' labels
        """Part 1"""
        self.label_shorts_part_1 = QLabel(self.column_treatment)
        self.label_shorts_part_1.setObjectName(u"label_shorts_part_1")
        self.label_shorts_part_1.setGeometry(QRect(40, 20, 500, 90))
        font4 = QFont()
        font4.setFamily(u"Yu Gothic UI Light")
        font4.setPointSize(35)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_shorts_part_1.setFont(font4)
        self.label_shorts_part_1.setStyleSheet(u"color: white; background-color: None;")
        """Part 2"""
        self.label_shorts_part_2 = QLabel(self.column_treatment)
        self.label_shorts_part_2.setObjectName(u"label_shorts_part_2")
        self.label_shorts_part_2.setGeometry(QRect(265, 20, 500, 90))
        font4_part_2 = QFont()
        font4_part_2.setFamily(u"Yu Gothic UI Light")
        font4_part_2.setPointSize(35)
        font4_part_2.setBold(True)
        font4_part_2.setWeight(75)
        self.label_shorts_part_2.setFont(font4_part_2)
        self.label_shorts_part_2.setStyleSheet(u"color: #f00000; background-color: None;")

        # Configuring the Open Wires' label dedicated to the counting of lines treated
        self.label_lines_treated_counter = QLabel(self.column_treatment)
        self.label_lines_treated_counter.setObjectName(u"label_lines_treated_counter")
        self.label_lines_treated_counter.setGeometry(QRect(420, 20, 325, 90))
        font_lltc = QFont()  # LLTC = Label Lines Treated Counter
        font_lltc.setFamily(u"Yu Gothic UI Light")
        font_lltc.setPointSize(35)
        font_lltc.setBold(True)
        font_lltc.setWeight(75)
        self.label_lines_treated_counter.setFont(font_lltc)
        self.label_lines_treated_counter.setStyleSheet(u"color: white; background-color: None;")

        # Configuring the Shorts' Left Part's label
        self.label_left_part = QLabel(self.column_treatment)
        self.label_left_part.setObjectName(u"label_left_part")
        self.label_left_part.setGeometry(QRect(60, 200, 1000, 400))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(17.5)
        font5.setBold(False)
        self.label_left_part.setFont(font5)
        self.label_left_part.setStyleSheet(u"color: white; background-color: None;")
        self.label_left_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        self.label_shorts_part_1.setText(QCoreApplication.translate("MainWindow", u"Viskovi" + " / ", None))
        self.label_shorts_part_2.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        # a default value for the Label dedicated to the Open Wires' lines treated
        self.label_lines_treated_counter.setText(QCoreApplication.translate("MainWindow", u"X/M", None))

