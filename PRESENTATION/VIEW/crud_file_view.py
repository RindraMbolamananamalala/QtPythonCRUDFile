# -*- coding: utf-8 -*-

"""
crud_file_view.py: The python file dedicated to the "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.ui_Main_Window_UI import Ui_MainWindow


class CRUDFileView:

    def set_main_window_ui(self, main_window_ui: Ui_MainWindow):
        """

        :param main_window_ui: The UI instance to be associated to the View Part of the MVC Implementation
        within the PRESENTATION layer of the Project.
        :return:
        """
        self.main_window_ui = main_window_ui

    def get_main_window_ui(self) -> Ui_MainWindow:
        """

        :return: The UI instance associated to the View Part of the MVC Implementation within the PRESENTATION layer of
        the Project.
        """
        return self.main_window_ui

    def __init__(self, *args):
        """
        :param window: The main window of the application.
        """
        if len(args) == 0:
            # No specific definition of a specific UI was provided and has to be be proved later by the Developer
            pass
        elif len(args) == 1:
            # A specific definition of a specific UI was provided with the latter's Main window having been provided
            self.set_main_window_ui(
                # The main window of the application.
                args[0]
            )
        else:
            # An invalid number of arguments was provided
            msg_error = "Invalid number of arguments given for the instantiation of a View"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception
