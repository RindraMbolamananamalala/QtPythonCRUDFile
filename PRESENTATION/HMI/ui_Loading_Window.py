# -*- coding: utf-8 -*-

################################################################################
## Created with: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_window_loading(object):

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

    def __init__(self, main_window):
        """
        Setting up the UI.

        :param main_window: a blank main window to be associated to the set of settings.
        """
        # General settings Part 1
        if not main_window.objectName():
            main_window.setObjectName(u"window_loading")
            self.set_main_window(main_window)
        main_window.resize(1920, 1080)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")

        """
        Customizing the Loading Animation
        """
        # Preparing the Label
        self.label_loading_animation = QLabel(self.centralwidget)
        self.label_loading_animation.setObjectName(u"label_loading_animation")
        self.label_loading_animation.setGeometry(QRect(460, 200, 900, 600))
        # Preparing the Animation Movie to be associated with the Label.
        # To do so, we have to load the Image for the Animation from the RESOURCE and then associate it with
        # the Label.
        movie_loading_animation = QMovie("RESOURCES\\IMAGES\\Quarter-Circle-Loading-Image-1.gif")
        self.label_loading_animation.setMovie(movie_loading_animation)
        # Starting the Animation
        self.label_loading_animation.movie().start()

        # General settings Part 2
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

    def retranslateUi(self, window_loading):
        window_loading.setWindowTitle(QCoreApplication.translate("window_loading", u"MainWindow", None))


