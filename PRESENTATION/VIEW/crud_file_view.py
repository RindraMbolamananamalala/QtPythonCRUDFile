# -*- coding: utf-8 -*-

"""
crud_file_view_.py: The python file dedicated to the abstract "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
Any "View" class should be a child of this abstract "View" class.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import abstractmethod
from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead


class CRUDFileView:

    def set_window_ui(self, window_ui: object):
        """

        :param window_ui: The window UI to be managed by the Current View.
        :return:
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> object:
        """

        :return: The window UI managed by the Current View.
        """
        return self.window_ui

    @abstractmethod
    def update_content(self, line_to_display: LineToRead) -> None:
        """
        Updating the content of the current CRUD View from a line given as parameter.

        :param line_to_display:  The Line from which he content of the current CRUD View will be updated
        :return: None
        """
        # We'll let the Child class manage the full implementation
        pass

    def __init__(self, *args):
        """
        :param window: The window UI to be managed by the Current View.
        """
        if len(args) == 0:
            # No specific definition of a specific UI was provided and has to be be proved later by the Developer then
            pass
        elif len(args) == 1:
            # A specific definition of a specific UI was provided
            self.set_window_ui(
                # The window UI provided.
                args[0]
            )
        else:
            # An invalid number of arguments was provided
            msg_error = "Invalid number of arguments given for the instantiation of a View"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception
