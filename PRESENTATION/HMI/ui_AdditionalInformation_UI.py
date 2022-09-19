# -*- coding: utf-8 -*-

"""
ui_AdditionalInformation_UI.py: The python file dedicated to the graphical definition of the
Additional Information Window of the application.
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


class UI_AdditionalInformation(object):

    def set_main_window(self, main_window: QMainWindow):
        self.main_window = main_window

    def get_main_window(self) -> QMainWindow:
        return self.main_window

    def set_combo_box_additional_information_w(self, combo_box_additional_information_w: QComboBox):
        self.combo_box_additional_information_w = combo_box_additional_information_w

    def get_combo_box_additional_information_w(self) -> QComboBox:
        return self.combo_box_additional_information_w

    def set_text_additional_information_comments(self, text_additional_information_comments: QPlainTextEdit):
        self.text_additional_information_comments = text_additional_information_comments

    def get_text_additional_information_comments(self) -> QPlainTextEdit:
        return self.text_additional_information_comments

    def set_button_additional_information_confirm(self, button_additional_information_confirm: QPushButton):
        self.button_additional_information_confirm = button_additional_information_confirm

    def get_button_additional_information_confirm(self) -> QPushButton:
        return self.button_additional_information_confirm

    def set_button_additional_information_cancel(self, button_additional_information_cancel: QPushButton):
        self.button_additional_information_cancel = button_additional_information_cancel

    def get_set_button_additional_information_cancel(self) -> QPushButton:
        return self.button_additional_information_cancel

    def __init__(self, main_window):
        """
        Setting up the UI.

        :param main_window: a blank main window to be associated to the set of settings.
        """
        # First preparations
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(1159, 823)
        self.set_main_window(main_window)

        """General settings related to the Main Frame"""
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.combo_box_additional_information__W = QComboBox(self.centralwidget)
        self.combo_box_additional_information__W.setObjectName(u"combo_box_additional_information__W")
        self.combo_box_additional_information__W.setGeometry(QRect(50, 50, 551, 601))
        self.set_combo_box_additional_information_w(self.combo_box_additional_information__W)
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(11)

        """W Combo-Box part"""
        self.combo_box_additional_information__W.setFont(font)

        """Comments part"""
        self.text_additional_information_comments = QPlainTextEdit(self.centralwidget)
        self.text_additional_information_comments.setObjectName(u"text_additional_information_comments")
        self.text_additional_information_comments.setGeometry(QRect(610, 50, 361, 601))
        self.set_text_additional_information_comments(self.text_additional_information_comments)

        """Confirm button part"""
        self.button_additional_information_confirm = QPushButton(self.centralwidget)
        self.button_additional_information_confirm.setObjectName(u"button_additional_information_confirm")
        self.button_additional_information_confirm.setGeometry(QRect(980, 50, 141, 601))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        self.button_additional_information_confirm.setFont(font1)
        self.button_additional_information_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.set_button_additional_information_confirm(self.button_additional_information_confirm)

        """Cancel button part"""
        self.button_additional_information_cancel = QPushButton(self.centralwidget)
        self.button_additional_information_cancel.setObjectName(u"button_additional_information_cancel")
        self.button_additional_information_cancel.setGeometry(QRect(930, 670, 93, 91))
        self.button_additional_information_cancel.setFont(font1)
        self.button_additional_information_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.set_button_additional_information_cancel(self.button_additional_information_cancel)
        main_window.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1159, 26))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Additional Information Window", None))

        self.text_additional_information_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add comment", None))
        self.button_additional_information_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.button_additional_information_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))


