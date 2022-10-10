# -*- coding: utf-8 -*-

"""
crud_file_vertical_label.py: The python file dedicated to a customized version (vertical) graphical definition of the
QLabel
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class CRUDFileVerticalLabel(QLabel):

    def __init__(self, *args):
        """
        First, let's initialize the Label with the default behaviors & data of a QLabel

        :param args:
        """
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        """
        Managing the Vertical orientation of the Label

        :param event:
        :return:
        """
        painter = QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        painter.drawText(0, self.width() / 2, self.text())
        painter.end()
