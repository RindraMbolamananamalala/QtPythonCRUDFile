# -*- coding: utf-8 -*-

"""
ui_Main_Window_UI.py: The python file dedicated to the graphical definition of the Main Window of the application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


################################################################################
## Created with: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):

    def set_main_window(self, main_window: QMainWindow):
        """

        :param main_window: The Qt Main Window to be used by the the current Main Window.
        :return:
        """
        self.main_window = main_window

    def get_main_window(self) -> QMainWindow:
        """

        :return: The Qt Main Window used by the the current Main Window.
        """
        return self.main_window

    def set_label_file_id(self, label_file_id: QLabel):
        self.label_file_id = label_file_id

    def get_label_file_id(self) -> QLabel:
        return self.label_file_id

    def label_for_the_specific_fixed_string(self, label_for_the_specific_fixed_string: QLabel):
        self.label_for_the_specific_fixed_string = label_for_the_specific_fixed_string

    def get_label_for_the_specific_fixed_string(self) -> QLabel:
        return self.label_for_the_specific_fixed_string

    def set_combo_box_F(self, combo_box_F: QComboBox):
        self.combo_box_F = combo_box_F

    def get_combo_box_F(self) -> QComboBox:
        return self.combo_box_F

    def set_list_open_connections_name(self, list_open_connections_name: QListWidget):
        self.list_open_connections_name = list_open_connections_name

    def get_list_open_connections_name(self) -> QListWidget:
        return self.list_open_connections_name

    def get_text_wire_name(self) -> QPlainTextEdit:
        return self.text_wire_name

    def get_text_cross_section(self) -> QPlainTextEdit:
        return self.text_cross_section

    def get_text_color(self) -> QPlainTextEdit:
        return self.text_color

    def get_text_position_1(self) -> QPlainTextEdit:
        return self.text_position_1

    def get_text_cavity_1(self):
        return self.text_cavity_1

    def get_text_position_2(self) -> QPlainTextEdit:
        return self.text_position_2

    def get_text_cavity_2(self):
        return self.text_cavity_2

    def set_combo_box_open_connections_W(self, combo_box_open_connections_W: QComboBox):
        self.combo_box_open_connection_W = combo_box_open_connections_W

    def get_combo_box_open_connections_W(self) -> QComboBox:
        return self.combo_box_open_connection_W

    def get_text_open_connections_comments(self) -> QPlainTextEdit:
        return self.text_open_connections_comments

    def get_button_open_connections_confirm(self) -> QPushButton:
        return self.button_open_connections_confirm

    def set_list_shorts_name(self, list_shorts_name: QListWidget):
        self.list_shorts_name = list_shorts_name

    def get_list_shorts_name(self) -> QListWidget:
        return self.list_shorts_name

    def set_combo_box_shorts_W(self, combo_box_shorts_W: QComboBox):
        self.combo_box_shorts_W = combo_box_shorts_W

    def get_combo_box_shorts_W(self) -> QComboBox:
        return self.combo_box_shorts_W

    def get_text_shorts_comments(self) -> QPlainTextEdit:
        return self.text_shorts_comments

    def get_button_shorts_confirm(self) -> QPushButton:
        return self.button_shorts_confirm

    def get_button_cancel(self) -> QPushButton:
        return self.button_cancel

    def get_button_add_additional_information(self) -> QPushButton:
        return self.button_add_additional_information

    def __init__(self, main_window: QMainWindow):
        """
        Setting up the UI.

        :param main_window: a blank main window to be associated to the set of settings.
        """
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(1423, 800)
        self.set_main_window(main_window)

        """General settings related to the Main Frame"""
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 10, 1421, 771))
        font = QFont()
        font.setKerning(True)
        self.main_frame.setFont(font)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.label_open_connections = QLabel(self.main_frame)
        self.label_open_connections.setObjectName(u"label_open_connections")
        self.label_open_connections.setGeometry(QRect(40, 90, 171, 21))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setKerning(True)

        """Open Connections Part"""
        self.label_open_connections.setFont(font1)
        self.combo_box_open_connection_W = QComboBox(self.main_frame)
        self.combo_box_open_connection_W.addItem("")
        self.combo_box_open_connection_W.addItem("")
        self.combo_box_open_connection_W.setObjectName(u"combo_box_open_connection_W")
        self.combo_box_open_connection_W.setGeometry(QRect(340, 200, 281, 121))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        font2.setKerning(True)
        self.combo_box_open_connection_W.setFont(font2)
        self.text_open_connections_comments = QPlainTextEdit(self.main_frame)
        self.text_open_connections_comments.setObjectName(u"text_open_connections_comments")
        self.text_open_connections_comments.setGeometry(QRect(630, 200, 631, 121))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(9)
        font3.setKerning(True)
        self.text_open_connections_comments.setFont(font3)
        self.button_open_connections_confirm = QPushButton(self.main_frame)
        self.button_open_connections_confirm.setObjectName(u"button_open_connections_confirm")
        self.button_open_connections_confirm.setGeometry(QRect(1270, 200, 111, 121))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(10)
        font4.setKerning(True)
        self.button_open_connections_confirm.setFont(font4)
        self.button_open_connections_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.text_wire_name = QPlainTextEdit(self.main_frame)
        self.text_wire_name.setObjectName(u"text_wire_name")
        self.text_wire_name.setGeometry(QRect(340, 120, 141, 71))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(10)
        font5.setKerning(True)
        self.text_wire_name.setFont(font5)
        self.text_cross_section = QPlainTextEdit(self.main_frame)
        self.text_cross_section.setObjectName(u"text_cross_section")
        self.text_cross_section.setGeometry(QRect(490, 120, 141, 71))
        self.text_cross_section.setFont(font5)
        self.text_color = QPlainTextEdit(self.main_frame)
        self.text_color.setObjectName(u"text_color")
        self.text_color.setGeometry(QRect(640, 120, 141, 71))
        self.text_color.setFont(font5)
        self.text_position_1 = QPlainTextEdit(self.main_frame)
        self.text_position_1.setObjectName(u"text_position_1")
        self.text_position_1.setGeometry(QRect(790, 120, 141, 71))
        self.text_position_1.setFont(font5)
        self.text_cavity_1 = QPlainTextEdit(self.main_frame)
        self.text_cavity_1.setObjectName(u"text_cavity_1")
        self.text_cavity_1.setGeometry(QRect(940, 120, 141, 71))
        self.text_cavity_1.setFont(font5)
        self.text_position_2 = QPlainTextEdit(self.main_frame)
        self.text_position_2.setObjectName(u"text_position_2")
        self.text_position_2.setGeometry(QRect(1090, 120, 141, 71))
        self.text_position_2.setFont(font5)
        self.text_cavity_2 = QPlainTextEdit(self.main_frame)
        self.text_cavity_2.setObjectName(u"text_cavity_2")
        self.text_cavity_2.setGeometry(QRect(1240, 120, 141, 71))
        self.text_cavity_2.setFont(font5)
        self.label_wire_name = QLabel(self.main_frame)
        self.label_wire_name.setObjectName(u"label_wire_name")
        self.label_wire_name.setGeometry(QRect(340, 90, 111, 21))
        self.label_wire_name.setFont(font1)
        self.label_cross_section = QLabel(self.main_frame)
        self.label_cross_section.setObjectName(u"label_cross_section")
        self.label_cross_section.setGeometry(QRect(490, 90, 111, 21))
        self.label_cross_section.setFont(font1)
        self.label_color = QLabel(self.main_frame)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setGeometry(QRect(640, 90, 111, 21))
        self.label_color.setFont(font1)
        self.label_position_1 = QLabel(self.main_frame)
        self.label_position_1.setObjectName(u"label_position_1")
        self.label_position_1.setGeometry(QRect(790, 90, 111, 21))
        self.label_position_1.setFont(font1)
        self.label_cavity_1 = QLabel(self.main_frame)
        self.label_cavity_1.setObjectName(u"label_cavity_1")
        self.label_cavity_1.setGeometry(QRect(940, 90, 111, 21))
        self.label_cavity_1.setFont(font1)
        self.label_position_2 = QLabel(self.main_frame)
        self.label_position_2.setObjectName(u"label_position_2")
        self.label_position_2.setGeometry(QRect(1090, 90, 111, 21))
        self.label_position_2.setFont(font1)
        self.label_cavity_2 = QLabel(self.main_frame)
        self.label_cavity_2.setObjectName(u"label_cavity_2")
        self.label_cavity_2.setGeometry(QRect(1240, 90, 111, 21))
        self.label_cavity_2.setFont(font1)

        """Shorts Part"""
        self.label_shorts = QLabel(self.main_frame)
        self.label_shorts.setObjectName(u"label_shorts")
        self.label_shorts.setGeometry(QRect(40, 370, 111, 21))
        self.label_shorts.setFont(font1)
        self.list_shorts_name = QListWidget(self.main_frame)
        self.list_shorts_name.setObjectName(u"list_shorts_name")
        self.list_shorts_name.setGeometry(QRect(40, 400, 461, 201))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(13)
        font6.setKerning(True)
        self.list_shorts_name.setFont(font6)
        self.combo_box_shorts_W = QComboBox(self.main_frame)
        self.combo_box_shorts_W.addItem("")
        self.combo_box_shorts_W.addItem("")
        self.combo_box_shorts_W.setObjectName(u"combo_box_shorts_W")
        self.combo_box_shorts_W.setGeometry(QRect(510, 400, 281, 201))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(12)
        font7.setKerning(False)
        self.combo_box_shorts_W.setFont(font7)
        self.combo_box_shorts_W.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.button_shorts_confirm = QPushButton(self.main_frame)
        self.button_shorts_confirm.setObjectName(u"button_shorts_confirm")
        self.button_shorts_confirm.setGeometry(QRect(1270, 400, 111, 201))
        self.button_shorts_confirm.setFont(font4)
        self.button_shorts_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.text_shorts_comments = QPlainTextEdit(self.main_frame)
        self.text_shorts_comments.setObjectName(u"text_shorts_comments")
        self.text_shorts_comments.setGeometry(QRect(800, 400, 461, 201))
        self.text_shorts_comments.setFont(font3)

        """Additional information Part"""
        self.button_add_additional_information = QPushButton(self.main_frame)
        self.button_add_additional_information.setObjectName(u"button_add_additional_information")
        self.button_add_additional_information.setGeometry(QRect(1170, 660, 211, 71))
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        font8.setKerning(True)
        self.button_add_additional_information.setFont(font8)
        self.button_add_additional_information.setCursor(QCursor(Qt.PointingHandCursor))

        """Cancel Part"""
        self.button_cancel = QPushButton(self.main_frame)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(950, 660, 211, 71))
        self.button_cancel.setFont(font4)
        self.button_cancel.setCursor(QCursor(Qt.PointingHandCursor))



        """Mocking Data (WILL BE MANAGED SERIOUSLY LATER)"""
        self.list_open_connections_name = QListWidget(self.main_frame)
        self.list_open_connections_name.setObjectName(u"list_open_connections_name")
        self.list_open_connections_name.setGeometry(QRect(40, 120, 291, 201))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(13)
        font9.setBold(False)
        font9.setWeight(50)
        font9.setKerning(True)
        self.list_open_connections_name.setFont(font9)
        self.combo_box_F = QComboBox(self.main_frame)
        self.combo_box_F.addItem("")
        self.combo_box_F.addItem("")
        self.combo_box_F.addItem("")
        self.combo_box_F.addItem("")
        self.combo_box_F.setObjectName(u"combo_box_F")
        self.combo_box_F.setGeometry(QRect(200, 40, 141, 31))
        self.combo_box_F.setFont(font5)
        self.label_file_id = QLabel(self.main_frame)
        self.label_file_id.setObjectName(u"label_file_id")
        self.label_file_id.setGeometry(QRect(10, 0, 191, 31))
        font10 = QFont()
        font10.setPointSize(15)
        font10.setBold(True)
        font10.setWeight(75)
        font10.setKerning(True)
        self.label_file_id.setFont(font10)
        self.label_for_the_specific_fixed_string = QLabel(self.main_frame)
        self.label_for_the_specific_fixed_string.setObjectName(u"label_for_the_specific_fixed_string")
        self.label_for_the_specific_fixed_string.setGeometry(QRect(10, 40, 191, 31))
        font11 = QFont()
        font11.setPointSize(15)
        font11.setBold(False)
        font11.setWeight(50)
        font11.setKerning(True)
        self.label_for_the_specific_fixed_string.setFont(font11)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1423, 26))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_open_connections.setText(QCoreApplication.translate("MainWindow", u"Open connections", None))
        self.combo_box_open_connection_W.setItemText(0, QCoreApplication.translate("MainWindow", u"W107 - Broken Wire",
                                                                                   None))
        self.combo_box_open_connection_W.setItemText(1,
                                                     QCoreApplication.translate("MainWindow", u"W109 - Another Reason",
                                                                                None))

        self.text_open_connections_comments.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Add comment", None))
        self.button_open_connections_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_wire_name.setText(QCoreApplication.translate("MainWindow", u"Wire Name", None))
        self.label_cross_section.setText(QCoreApplication.translate("MainWindow", u"Cross Section", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_position_1.setText(QCoreApplication.translate("MainWindow", u"Position 1", None))
        self.label_cavity_1.setText(QCoreApplication.translate("MainWindow", u"Cavity 1", None))
        self.label_position_2.setText(QCoreApplication.translate("MainWindow", u"Position 2", None))
        self.label_cavity_2.setText(QCoreApplication.translate("MainWindow", u"Cavity 2", None))
        self.label_shorts.setText(QCoreApplication.translate("MainWindow", u"Shorts", None))

        __sortingEnabled = self.list_shorts_name.isSortingEnabled()
        self.list_shorts_name.setSortingEnabled(False)
        self.list_shorts_name.setSortingEnabled(__sortingEnabled)

        self.combo_box_shorts_W.setItemText(0, QCoreApplication.translate("MainWindow", u"W107 - Broken Wire", None))
        self.combo_box_shorts_W.setItemText(1, QCoreApplication.translate("MainWindow", u"W109 - Another Reason", None))

        self.button_shorts_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.text_shorts_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add comment", None))
        self.button_add_additional_information.setText(
            QCoreApplication.translate("MainWindow", u"Add Additional Information", None))
        self.button_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))

        __sortingEnabled1 = self.list_open_connections_name.isSortingEnabled()
        self.list_open_connections_name.setSortingEnabled(False)
        self.list_open_connections_name.setSortingEnabled(__sortingEnabled1)

        self.combo_box_F.setItemText(0, QCoreApplication.translate("MainWindow", u"FA Team 1", None))
        self.combo_box_F.setItemText(1, QCoreApplication.translate("MainWindow", u"FA Team 2", None))
        self.combo_box_F.setItemText(2, QCoreApplication.translate("MainWindow", u"FA Team 3", None))
        self.combo_box_F.setItemText(3, QCoreApplication.translate("MainWindow", u"FA Team 4", None))

        self.label_file_id.setText(QCoreApplication.translate("MainWindow", u"B0008713866", None))
        self.label_for_the_specific_fixed_string.setText(QCoreApplication.translate("MainWindow", u"ROB 11", None))
