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

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_Shorts, self).__init__(main_window)

        # All the first 2 Label Icons have to be disabled at this level
        self.label_icon_1.setDisabled(True)
        self.label_icon_1.setStyleSheet(u"background-color: lightgrey;")
        self.label_icon_2.setDisabled(True)
        self.label_icon_2.setStyleSheet(u"background-color: lightgrey;")

        # Configuring the Shorts' label
        self.label_shorts = QLabel(self.column_treatment)
        self.label_shorts.setObjectName(u"label_shorts")
        self.label_shorts.setGeometry(QRect(40, 50, 500, 50))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_shorts.setFont(font4)
        self.label_shorts.setStyleSheet(u"color: white;")

        # Configuring the Shorts' Left Part's label
        self.label_left_part = QLabel(self.column_treatment)
        self.label_left_part.setObjectName(u"label_left_part")
        self.label_left_part.setGeometry(QRect(40, 120, 700, 400))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(16)
        self.label_left_part.setFont(font5)
        self.label_left_part.setStyleSheet(u"color: white;")
        self.label_left_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        # Temporary data are used to feed the UI, will be seriously managed latter
        self.label_shorts.setText(QCoreApplication.translate("MainWindow", u"Extra Wires - Shorts", None))
        self.label_left_part.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p>X35/1*1-B_V1.6<BR><span style=\" font-size: 18px;\">[64K/J]</span><BR></BR></p><p><span>N10/6*RB2-B_V1.20</span><BR><span style=\" font-size: 18px;\">[59M]</span></p></body></html>",
                                                                None))
