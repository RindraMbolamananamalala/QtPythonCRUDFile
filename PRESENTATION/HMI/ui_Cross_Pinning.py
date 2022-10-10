# -*- coding: utf-8 -*-

"""
ui_Cross_Pinning.py: The python file dedicated to the graphical definition of the Cross Pinning Window of the
application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER
from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow
from PRESENTATION.HMI.WIDGET.cross_pinning_selectable_label import CrossPinningSelectableLabel


class UI_CrossPinning(Ui_TreatmentWindow):

    def get_widget_left_part(self) -> QWidget:
        return self.widget_left_part

    def get_label_middle_part(self) -> QLabel:
        return self.label_middle_part

    def get_label_right_part(self) -> QLabel:
        return self.label_right_part

    def set_label_items(self, label_items: list):
        self.label_items = label_items

    def get_label_items(self) -> list:
        return self.label_items

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_CrossPinning, self).__init__(main_window)

        # Configuring the Cross Pinning's label
        self.label_cross_pinning = QLabel(self.column_treatment)
        self.label_cross_pinning.setObjectName(u"label_cross_pinning")
        self.label_cross_pinning.setGeometry(QRect(40, 50, 300, 50))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_cross_pinning.setFont(font4)
        self.label_cross_pinning.setStyleSheet(u"color: white;")

        """
        Configurations of the Parts dedicated to the Lines' treatment
        """
        # Initializing the specific list of Label Items for specific this Part
        self.set_label_items([])

        # Configuring the Cross Pinning's Left Part
        self.widget_left_part = QWidget(self.column_treatment)
        self.widget_left_part.setObjectName(u"widget_left_part")
        self.widget_left_part.setGeometry(QRect(40, 120, 400, 400))

        # Configuring the Cross Pinning's name's label
        self.label_name = QLabel(self.column_treatment)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(660, 50, 375, 50))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(22)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_name.setFont(font6)
        self.label_name.setStyleSheet(u"color: white")
        self.label_name.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Configuring the Cross Pinning's Middle part
        self.widget_middle_part = QWidget(self.column_treatment)
        self.widget_middle_part.setObjectName(u"widget_middle_part")
        self.widget_middle_part.setGeometry(QRect(660, 120, 400, 425))

        # Configuring the Cross Pinning's Right part's label
        self.widget_right_part = QWidget(self.column_treatment)
        self.widget_right_part.setObjectName(u"widget_right_part")
        self.widget_right_part.setGeometry(QRect(1270, 120, 400, 400))

        # Configuring the Cross Pinning's "Done" Button
        self.button_done = QPushButton(self.column_treatment)
        self.button_done.setObjectName(u"button_done")
        self.button_done.setGeometry(QRect(1700, 160, 111, 221))
        font9 = QFont()
        font9.setFamily(u"Open Sans Semibold")
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setWeight(75)
        self.button_done.setFont(font9)
        self.button_done.setStyleSheet(u"background-color: grey;")
        self.button_done.setCursor(QCursor(Qt.PointingHandCursor))

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        # Temporary data are used to feed the UI, will be seriously managed latter

        self.label_name.setText(QCoreApplication.translate("MainWindow", u"9611_1 0.75 WH", None))

        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Done", None))

    def feed_widget_left_part(self, list_of_lines: list):
        """
        Feeding the Widget dedicated to the Left Part of the Treatment area withe the corresponding lines.

        :param list_of_lines: The lines to use to feed the Widget dedicated to the Left Part of the Treatment area
        :return: None
        """
        try:
            i = 0
            for line in list_of_lines:
                font = QFont()
                font.setFamily(u"Consolas")
                font.setPointSize(16)
                label_from_pin = CrossPinningSelectableLabel(self.widget_left_part)
                label_from_pin.setGeometry(0, (i * 50), 400, 50)
                label_from_pin.set_label_normal_font(font)
                label_from_pin.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
                label_from_pin.setText(line)
                self.get_label_items().append(label_from_pin)
                i = i + 1
        except Exception as exception:
            # At least one error has occurred, therefore, stop the feeding process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Feeding Process. "
            )
            raise

    def feed_widget_middle_part(self, list_of_lines: list):
        """
        Feeding the Widget dedicated to the Middle Part of the Treatment area withe the corresponding lines.

        :param list_of_lines: The lines to use to feed the Widget dedicated to the Middle Part of the Treatment area
        :return: None
        """
        try:
            i = 0
            for line in list_of_lines:
                font = QFont()
                font.setFamily(u"Consolas")
                font.setPointSize(16)
                label_to_pin = CrossPinningSelectableLabel(self.widget_middle_part)
                label_to_pin.setGeometry(0, (i * 50), 400, 50)
                label_to_pin.set_label_normal_font(font)
                label_to_pin.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
                label_to_pin.setText(line)
                self.get_label_items().append(label_to_pin)
                i = i + 1
        except Exception as exception:
            # At least one error has occurred, therefore, stop the feeding process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Feeding Process. "
            )
            raise

    def feed_widget_right_part(self, list_of_lines: list):
        """
        Feeding the Widget dedicated to the Right Part of the Treatment area withe the corresponding lines.

        :param list_of_lines: The lines to use to feed the Widget dedicated to the Right Part of the Treatment area
        :return: None
        """
        try:
            i = 0
            for line in list_of_lines:
                font = QFont()
                font.setFamily(u"Consolas")
                font.setPointSize(16)
                label_splice = CrossPinningSelectableLabel(self.widget_right_part)
                label_splice.setGeometry(0, (i * 50), 400, 50)
                label_splice.set_label_normal_font(font)
                label_splice.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
                label_splice.setText(line)
                self.get_label_items().append(label_splice)
                i = i + 1
        except Exception as exception:
            # At least one error has occurred, therefore, stop the feeding process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Feeding Process. "
            )
            raise

    def reset_all_items_labels_color(self):
        """
        Resetting the colors of all the Items' Labels to the default one (White)

        :return: None
        """
        for label in self.get_label_items():
            label.setStyleSheet("color: white")
