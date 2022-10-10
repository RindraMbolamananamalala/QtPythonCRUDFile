# -*- coding: utf-8 -*-

"""
cross_pinning_selectable_label.py: The python file dedicated to a customized version (selectable) graphical definition
of the QLabel, needed by the Cross Pinning window.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class CrossPinningSelectableLabel(QLabel):

    def set_label_normal_font(self, label_normal_font: QFont):
        """
        
        :param label_normal_font: The normal font (before effect|animation) of the Label. 
        :return: None
        """""
        self.label_normal_font = label_normal_font
        self.setFont(self.get_label_normal_font())

    def get_label_normal_font(self) -> QFont:
        """

        :return: The normal font (before effect|animation) of the Label.
        """
        return self.label_normal_font

    # Initializing a "clicked" Signal for the Label, in order to make it "Selectable"
    clicked = Signal()

    def mousePressEvent(self, ev):
        """
        When the Left Key of the Button is clicked...

        :param ev:
        :return:
        """
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()

    def enterEvent(self, event):
        """
        Managing the "hover" part...

        :param event:
        :return:
        """
        super().enterEvent(event)
        font = QFont(self.get_label_normal_font().family())
        font.setPointSize(20)
        self.setFont(font)

    def leaveEvent(self, event):
        """
        Managing the "after hover" part...

        :param event:
        :return:
        """
        super().leaveEvent(event)
        self.setFont(self.get_label_normal_font())

    def __init__(self, parent):
        # Calling the superclass' constructor to have teh default behaviors and data
        super().__init__(parent)

        # The Hand cursor will be displayed when "Hovering" over the Label
        self.setCursor(QCursor(Qt.PointingHandCursor))
