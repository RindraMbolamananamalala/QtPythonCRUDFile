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

from PRESENTATION.HMI.ui_Treatment_Window import Ui_TreatmentWindow


class UI_CrossPinning(Ui_TreatmentWindow):

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

        # Configuring the Cross Pinning's Left Part's label
        self.label_left_part = QLabel(self.column_treatment)
        self.label_left_part.setObjectName(u"label_left_part")
        self.label_left_part.setGeometry(QRect(40, 120, 400, 400))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(16)
        self.label_left_part.setFont(font5)
        self.label_left_part.setStyleSheet(u"color: white;")
        self.label_left_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

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

        # Configuring the Cross Pinning's Middle part's label
        self.label_middle_part = QLabel(self.column_treatment)
        self.label_middle_part.setObjectName(u"label_middle_part")
        self.label_middle_part.setGeometry(QRect(660, 120, 400, 425))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(16)
        self.label_middle_part.setFont(font7)
        self.label_middle_part.setStyleSheet(u"color: white")
        self.label_middle_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # Configuring the Cross Pinning's Right part's label
        self.label_right_part = QLabel(self.column_treatment)
        self.label_right_part.setObjectName(u"label_right_part")
        self.label_right_part.setGeometry(QRect(1270, 120, 400, 400))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(14)
        self.label_right_part.setFont(font8)
        self.label_right_part.setStyleSheet(u"color: white;")
        self.label_right_part.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

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
        self.label_cross_pinning.setText(QCoreApplication.translate("MainWindow", u"Cross Pinning", None))
        self.label_left_part.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p>H4/144*1-B_V1.1 <span style=\" vertical-align:sub;\">[7B]</span></p><p><span>N12/2*1-B_V1.6 </span><span style=\" vertical-align:sub;\">[14H]</span></p></body></html>",
                                                                None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"9611_1 0.75 WH", None))
        self.label_middle_part.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<html><head/><body><p>N12/2*1-B_V1.6 <span style=\" vertical-align:sub;\">[14H]</span></p><p>N12/2*1-B_V1.7 <span style=\" vertical-align:sub;\">[14H]</span></p><p>N12/2*1-B_V1.8 <span style=\" vertical-align:sub;\">[14H]</span></p><p>N12/2*1-B_V1.12 <span style=\" vertical-align:sub;\">[14H]</span></p><p>N12/2*1-B_V1.13 <span style=\" vertical-align:sub;\">[14H]</span></p><p>N12/2*1-B_V1.14 <span style=\" vertical-align:sub;\">[14H]</span></p></body></html>",
                                                                  None))
        self.label_right_part.setText(QCoreApplication.translate("MainWindow",
                                                                 u"<html><head/><body><p>:Z7/107*1-L_V1.X</p><p>:Z7/107*2-L_V1.X</p></body></html>",
                                                                 None))
        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Done", None))
