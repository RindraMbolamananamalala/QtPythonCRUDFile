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

    def set_widget_left_part(self, widget_left_part: QWidget):
        self.widget_left_part = widget_left_part

    def get_widget_left_part(self) -> QWidget:
        return self.widget_left_part

    def get_widget_middle_part(self) -> QWidget:
        return self.widget_middle_part

    def get_widget_right_part(self) -> QWidget:
        return self.widget_right_part

    def set_label_items(self, label_items: list):
        self.label_items = label_items

    def get_label_items(self) -> list:
        return self.label_items

    def get_label_name(self) -> QLabel:
        return self.label_name

    def get_button_done(self) -> QPushButton:
        return self.button_done

    def get_label_lines_treated_counter(self) -> QLabel:
        return self.label_lines_treated_counter

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UI_CrossPinning, self).__init__(main_window)

        """
        FOR THE NEW VERSION OF GUIs, Confirm Button for the Cross Pinning window will be exluded
        """
        self.get_button_confirm().close()

        # Configuring the Cross Pinning's label(s)
        self.label_cross_pinning_part_1 = QLabel(self.column_treatment)
        self.label_cross_pinning_part_1.setObjectName(u"label_cross_pinning_part_1")
        self.label_cross_pinning_part_1.setGeometry(QRect(40, 20, 300, 90))
        font4 = QFont()
        font4.setFamily(u"Yu Gothic UI Light")
        font4.setPointSize(35)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_cross_pinning_part_1.setFont(font4)
        self.label_cross_pinning_part_1.setStyleSheet(u"color: white; background-color: None;")
        self.label_cross_pinning_part_2 = QLabel(self.column_treatment)
        self.label_cross_pinning_part_2.setObjectName(u"label_cross_pinning_part_2")
        self.label_cross_pinning_part_2.setGeometry(QRect(290, 20, 300, 90))
        font4_part_2 = QFont()
        font4_part_2.setFamily(u"Yu Gothic UI Light")
        font4_part_2.setPointSize(35)
        font4_part_2.setBold(True)
        font4_part_2.setWeight(75)
        self.label_cross_pinning_part_2.setFont(font4_part_2)
        self.label_cross_pinning_part_2.setStyleSheet(u"color: #f00000; background-color: None;")

        # Configuring the Cross Pinning's label dedicated to the counting of lines treated
        self.label_lines_treated_counter = QLabel(self.column_treatment)
        self.label_lines_treated_counter.setObjectName(u"label_lines_treated_counter")
        self.label_lines_treated_counter.setGeometry(QRect(550, 20, 325, 90))
        font_lltc = QFont()  # LLTC = Label Lines Treated Counter
        font_lltc.setFamily(u"Yu Gothic UI Light")
        font_lltc.setPointSize(35)
        font_lltc.setBold(True)
        font_lltc.setWeight(75)
        self.label_lines_treated_counter.setFont(font_lltc)
        self.label_lines_treated_counter.setStyleSheet(u"color: white; background-color: None;")

        """
        Configurations of the Parts dedicated to the Lines' treatment
        """
        # Initializing the specific list of Label Items for specific this Part
        self.set_label_items([])

        # Configuring the Cross Pinning's Left Part
        self.widget_left_part = QWidget(self.column_treatment)
        self.widget_left_part.setObjectName(u"widget_left_part")
        self.widget_left_part.setGeometry(QRect(40, 150, 400, 400))
        self.widget_left_part.setStyleSheet(u"color: white; background-color: None;")

        # Configuring the Cross Pinning's name's label
        self.label_name = QLabel(self.column_treatment)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(900, 50, 625, 50))
        font6 = QFont()
        font6.setFamily(u"Yu Gothic UI Light")
        font6.setPointSize(22)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_name.setFont(font6)
        self.label_name.setStyleSheet(u"color: white; background-color: None;")
        self.label_name.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Configuring the Cross Pinning's Middle part
        self.widget_middle_part = QWidget(self.column_treatment)
        self.widget_middle_part.setObjectName(u"widget_middle_part")
        self.widget_middle_part.setGeometry(QRect(660, 150, 400, 425))
        self.widget_middle_part.setStyleSheet(u"color: white; background-color: None;")

        # Configuring the Cross Pinning's Right part's label
        self.widget_right_part = QWidget(self.column_treatment)
        self.widget_right_part.setObjectName(u"widget_right_part")
        self.widget_right_part.setGeometry(QRect(1270, 150, 400, 400))
        self.widget_right_part.setStyleSheet(u"color: white; background-color: None;")

        # Configuring the Cross Pinning's "Done" Button
        """
        FOR THE NEW VERSION OF GUIs, The "Done" button will be placed at the former position of the "Confirm" one
        """
        self.button_done = QPushButton(self.column_treatment)
        self.button_done.setObjectName(u"button_done")
        self.button_done.setGeometry(self.get_button_confirm().geometry())
        font9 = QFont()
        font9.setFamily(u"Yu Gothic UI Light")
        font9.setPointSize(25)
        font9.setBold(False)
        font9.setWeight(75)
        self.button_done.setFont(font9)
        self.button_done.setStyleSheet(u"background-color: #d9d9d9; color: #4b4b4b;")
        self.button_done.setCursor(QCursor(Qt.PointingHandCursor))

        # Finally, we have to Retranslate the current UI, independently of the Superclass
        self.retranslateCurrentUi(main_window)

    def clear_left_part(self):
        """
        Clearing the content of the left part.

        :return: None
        """
        try:
            widget_left_part = self.get_widget_left_part()
            for child in widget_left_part.children():
                child.close()
                child.setParent(None)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the clearing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Clearing Process. "
            )
            raise

    def clear_middle_part(self):
        """
        Clearing the content of the middle part.

        :return: None
        """
        try:
            widget_middle_part = self.get_widget_middle_part()
            for child in widget_middle_part.children():
                child.setParent(None)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the clearing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Clearing Process. "
            )
            raise

    def clear_right_part(self):
        """
        Clearing teh content of the Right Part.

        :return: None
        """
        try:
            widget_right_part = self.get_widget_right_part()
            for child in widget_right_part.children():
                child.setParent(None)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the clearing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Clearing Process. "
            )
            raise

    def clear_window(self):
        """
        Clearing the contents of all the Parts.

        :return: None
        """
        # Left Part
        self.clear_left_part()
        # Middle Part
        self.clear_middle_part()
        # Right Part
        self.clear_right_part()

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
                label_from_pin = CrossPinningSelectableLabel(self.get_widget_left_part())
                label_from_pin.setGeometry(0, (i * 50), 400, 50)
                label_from_pin.set_label_normal_font(font)
                label_from_pin.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
                label_from_pin.setText(line)
                label_from_pin.show()
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
                label_to_pin.show()
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
                label_splice.show()
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

    def retranslateCurrentUi(self, main_window: QMainWindow):
        """
        Defining a specific Retranslation of the current UI, independently of the Superclass.

        :param main_window: The main window of the current UI
        :return:
        """
        self.label_cross_pinning_part_1.setText(QCoreApplication.translate("MainWindow", u"Pogresno", None))
        self.label_cross_pinning_part_2.setText(QCoreApplication.translate("MainWindow", u"Pinovanje", None))
        # a default value for the Label dedicated to the Cross Pinning's lines treated
        self.label_lines_treated_counter.setText(QCoreApplication.translate("MainWindow", u"X/M", None))
        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Potvrdi", None))
