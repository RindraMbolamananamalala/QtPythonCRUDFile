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

    def get_button_done(self) -> QPushButton:
        return self.button_done

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_AdditionalInformationWindow, self).__init__(main_window)

        # All the first 3 Label Icons have to be disabled at this level
        self.label_icon_1.setDisabled(True)
        self.label_icon_1.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon1_crosspinning_inactive.png"))
        self.label_icon_2.setDisabled(True)
        self.label_icon_2.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon2_open_inactive.png"))
        self.label_icon_3.setDisabled(True)
        self.label_icon_3.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon3_short_inactive.png"))

        # Configuring the Additional Information' s label
        """Part 1"""
        self.label_additional_information_part_1 = QLabel(self.column_treatment)
        self.label_additional_information_part_1.setObjectName(u"label_additional_information_part_1")
        self.label_additional_information_part_1.setGeometry(QRect(40, 20, 250, 90))
        font4 = QFont()
        font4.setFamily(u"Yu Gothic UI Light")
        font4.setPointSize(35)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_additional_information_part_1.setFont(font4)
        self.label_additional_information_part_1.setStyleSheet(u"color: white; background-color: None;")
        """Part 2"""
        self.label_additional_information_part_2 = QLabel(self.column_treatment)
        self.label_additional_information_part_2.setObjectName(u"label_additional_information_part_2")
        self.label_additional_information_part_2.setGeometry(QRect(268, 20, 290, 90))
        font4_part_2 = QFont()
        font4_part_2.setFamily(u"Yu Gothic UI Light")
        font4_part_2.setPointSize(35)
        font4_part_2.setBold(True)
        font4_part_2.setWeight(75)
        self.label_additional_information_part_2.setFont(font4_part_2)
        self.label_additional_information_part_2.setStyleSheet(u"color: #f00000; background-color: None;")

        # The Additional Information Window doesn't have lines to display, so, let's adjust the position of
        # the remaining components
        self.combobox_fed_by_excel_sheet.setGeometry(QRect(60, 204, 1591, 125))
        self.text_comments.setGeometry(QRect(60, 340, 1591, 300))
        self.button_confirm.setGeometry(QRect(60, 650, 1291, 335))

        # However, the Additional Information Window has a Done "Button" on it, let's configure the latter then
        self.button_done = QPushButton(self.column_treatment)
        self.button_done.setObjectName(u"button_confirm")
        self.button_done.setGeometry(QRect(1360, 650, 290, 335))
        font_button_done = QFont()
        font_button_done.setFamily(u"Yu Gothic UI Light")
        font_button_done.setPointSize(25)
        font_button_done.setBold(False)
        font_button_done.setWeight(50)
        self.button_done.setFont(font_button_done)
        self.button_done.setStyleSheet(u"background-color: #d9d9d9; color: #4b4b4b;")
        self.button_done.setCursor(QCursor(Qt.PointingHandCursor))

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        self.label_additional_information_part_1.setText(
            QCoreApplication.translate("MainWindow", u"Dodatne", None)
        )
        self.label_additional_information_part_2.setText(
            QCoreApplication.translate("MainWindow", u"Informacije", None)
        )
        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Kraj", None))

