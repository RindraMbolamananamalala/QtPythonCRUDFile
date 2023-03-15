# -*- coding: utf-8 -*-

"""
ui_Treatment_Window_UI.py: The python file dedicated to the graphical definition of the abstract
Treatment Window of the application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

################################################################################
## Created with: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from threading import main_thread

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.WIDGET.crud_file_vertical_label import CRUDFileVerticalLabel


class Ui_TreatmentWindow(object):

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

    def get_combobox_fed_by_excel_sheet(self) -> QComboBox:
        """

        :return: The combobox fed by excel sheet present on the Current Treatment Window.
        """
        return self.combobox_fed_by_excel_sheet

    def get_text_comments(self) -> QPlainTextEdit:
        """

        :return: The Text Area dedicated to the Comments present on the Current Treatment Window.
        """
        return self.text_comments

    def get_button_confirm(self) -> QPushButton:
        """

        :return: The Confirm Button present on the Current Treatment Window.
        """
        return self.button_confirm

    def get_label_uut(self) -> QLabel:
        """

        :return: The UUT Label present on the Current Treatment Window.
        """
        return self.label_uut

    def get_label_fixed_strings(self) -> QLabel:
        """

        :return: The label dedicated to the combination of the two fixed Strings
        """
        return self.label_fixed_strings

    def __init__(self, main_window:QMainWindow):
        """
        Setting up the UI.

        :param main_window: a blank main window to be associated with the set of settings.
        """
        # General Settings Part I
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
            self.set_main_window(main_window)
        main_window.setFixedSize(1920, 1080)

        main_window.setAutoFillBackground(False)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")

        # The column for the Navigation
        self.column_navigation = QWidget(self.centralwidget)
        self.column_navigation.setObjectName(u"column_navigation")
        self.column_navigation.setGeometry(QRect(0, 0, 100, 1080))
        self.column_navigation.setStyleSheet(u"background: "
                                             u" qlineargradient( "
                                             u"     x1:1 y1:1"
                                             u"         , x2:1 y2:0"
                                             u"         , stop:0 #656565"
                                             u"         , stop:1 #020202"
                                             u");"
                                             u"border: 2.5px solid #909090;")

        # The list of Label Icons
        self.label_icon_1 = QLabel(self.column_navigation)
        self.label_icon_1.setObjectName(u"label_icon_1")
        self.label_icon_1.setGeometry(QRect(12.75, 7, 75, 75))
        self.label_icon_1.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon1_crosspinning_active.png"))
        self.label_icon_1.setStyleSheet(u"border: None;")

        self.label_icon_2 = QLabel(self.column_navigation)
        self.label_icon_2.setObjectName(u"label_icon_2")
        self.label_icon_2.setGeometry(QRect(12.75, 87, 75, 75))
        self.label_icon_2.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon2_open_active.png"))
        self.label_icon_2.setStyleSheet(u"border: None;")

        self.label_icon_3 = QLabel(self.column_navigation)
        self.label_icon_3.setObjectName(u"label_icon_3")
        self.label_icon_3.setGeometry(QRect(12.75, 167, 75, 75))
        self.label_icon_3.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon3_short_active.png"))
        self.label_icon_3.setStyleSheet(u"border: None;")

        self.label_icon_4 = QLabel(self.column_navigation)
        self.label_icon_4.setObjectName(u"label_icon_4")
        self.label_icon_4.setGeometry(QRect(12.75, 247, 75, 75))
        self.label_icon_4.setPixmap(QPixmap("RESOURCES\\IMAGES\\icon4_info_active.png"))
        self.label_icon_4.setStyleSheet(u"border: None;")

        # The Vertical label dedicated to the combination of the two fixed Strings
        self.label_fixed_strings = CRUDFileVerticalLabel(self.column_navigation)
        self.label_fixed_strings.setObjectName(u"label_fixed_strings")
        self.label_fixed_strings.setGeometry(QRect(20, 500, 72, 450))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_fixed_strings.setFont(font)
        self.label_fixed_strings.setLayoutDirection(Qt.LeftToRight)
        self.label_fixed_strings.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        self.label_fixed_strings.setStyleSheet(u"color: white; "
                                               u"background-color: None;"
                                               u"border: None;")
        self.label_fixed_strings.setTextFormat(Qt.AutoText)
        self.label_fixed_strings.setWordWrap(False)

        # The column for the Treatment
        self.column_treatment = QWidget(self.centralwidget)
        self.column_treatment.setObjectName(u"column_treatment")
        self.column_treatment.setGeometry(QRect(100, 0, 1860, 1080))
        self.column_treatment.setStyleSheet(u"QWidget#column_treatment{"
                                            u"background: "
                                             u" qlineargradient( "
                                             u"     x1:1 y1:1"
                                             u"         , x2:1 y2:0"
                                             u"         , stop:0 #656565"
                                             u"         , stop:1 #020202"
                                             u");"
                                            u"}")

        # The Logo box area
        self.widget_logo_box = QWidget(self.column_treatment)
        self.widget_logo_box.setObjectName(u"widget_logo_box")
        self.widget_logo_box.setGeometry(QRect(1540, 25, 265, 45))
        self.widget_logo_box.setStyleSheet(u"background-color: None;")
        self.label_logo_box = QLabel(self.widget_logo_box)
        self.label_logo_box.setGeometry(QRect(0, 0, 350, 45))
        self.label_logo_box.setPixmap(QPixmap("RESOURCES\\IMAGES\\aptiv-logo_white.png"))
        self.label_logo_box.setObjectName(u"label_logo_box")
        self.label_logo_box.setStyleSheet(u"background-color: None;")

        # The settings related to the Combo-Box fed by a specific Excel Sheet to be provided
        self.combobox_fed_by_excel_sheet = QComboBox(self.column_treatment)
        self.combobox_fed_by_excel_sheet.setObjectName(u"combobox_fed_by_excel_sheet")
        self.combobox_fed_by_excel_sheet.setGeometry(QRect(17, 580, 1391, 151))
        font_combo_box = QFont()
        font_combo_box.setFamily(u"Consolas")
        font_combo_box.setPointSize(15)
        self.combobox_fed_by_excel_sheet.setFont(font_combo_box)
        self.combobox_fed_by_excel_sheet.setStyleSheet(u"background-color: lightgrey; color:black;")

        # Comments Text area's settings
        self.text_comments = QPlainTextEdit(self.column_treatment)
        self.text_comments.setObjectName(u"text_comments")
        self.text_comments.setGeometry(QRect(17, 740, 1391, 241))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        self.text_comments.setFont(font1)
        self.text_comments.setStyleSheet(u"background-color: white; color: black;")

        # Configuring the Button Confirm
        self.button_confirm = QPushButton(self.column_treatment)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setGeometry(QRect(1425, 580, 245, 400))
        font2 = QFont()
        font2.setFamily(u"Yu Gothic UI Light")
        font2.setPointSize(25)
        font2.setBold(False)
        font2.setWeight(50)
        self.button_confirm.setFont(font2)
        self.button_confirm.setStyleSheet(u"background-color: #d9d9d9; color: #4b4b4b;")
        self.button_confirm.setCursor(QCursor(Qt.PointingHandCursor))

        # Configuring the Vertical Label dedicated to the UUT of the current file read by the Application
        self.label_uut = CRUDFileVerticalLabel(self.column_treatment)
        self.label_uut.setObjectName(u"label_uut")
        self.label_uut.setGeometry(QRect(1670, 485, 161, 450))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(43)
        font3.setBold(False)
        font3.setWeight(75)
        self.label_uut.setFont(font3)
        self.label_uut.setStyleSheet(u"color: white; background-color: None")

        # General Settings Part II
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Comments", None))
        self.button_confirm.setText(QCoreApplication.translate("MainWindow", u"Potvrdi", None))
    # retranslateUi
