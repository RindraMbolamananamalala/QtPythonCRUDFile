# -*- coding: utf-8 -*-

"""
ui_Additional_Information_Window.py: The python file dedicated to the graphical definition of the Additional
Information Window of the application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMainWindow

from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow


class UI_AdditionalInformationWindow(Ui_TreatmentWindow):

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_AdditionalInformationWindow, self).__init__(main_window)

        # Configuring the Additional Information' s label
        self.label_additional_information = QLabel(self.column_treatment)
        self.label_additional_information.setObjectName(u"label_shorts")
        self.label_additional_information.setGeometry(QRect(40, 50, 550, 50))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_additional_information.setFont(font4)
        self.label_additional_information.setStyleSheet(u"color: white;")

        # The Additional Information Window doesn't have lines to display, so, let's adjust the position of
        # the remaining components
        self.combobox_fed_by_excel_sheet.setGeometry(QRect(10, 504, 1641, 51))
        self.text_comments.setGeometry(QRect(10, 564, 1641, 241))
        self.button_confirm.setGeometry(QRect(10, 814, 1641, 51))

        # However, the Additional Information Window has a Done "Button" on it, let's configure the latter then
        self.button_done = QPushButton(self.column_treatment)
        self.button_done.setObjectName(u"button_confirm")
        self.button_done.setGeometry(QRect(10, 875, 1641, 51))
        font_button_done = QFont()
        font_button_done.setFamily(u"Open Sans Semibold")
        font_button_done.setPointSize(14)
        font_button_done.setBold(False)
        font_button_done.setWeight(50)
        self.button_done.setFont(font_button_done)
        self.button_done.setStyleSheet(u"background-color: grey;")

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        # Temporary data are used to feed the UI, will be seriously managed latter
        self.label_additional_information.setText(
            QCoreApplication.translate("MainWindow", u"Additional Information", None)
        )
        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Done", None))

