# -*- coding: utf-8 -*-

"""
additional_information_view_.py: The python file dedicated to the Additional Information "View" part of the MVC pattern
implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.HMI.ui_Additional_Information_Window import UI_AdditionalInformationWindow
from PRESENTATION.VIEW.crud_file_view import CRUDFileView

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead


class AdditionalInformationView(CRUDFileView):

    def set_window_ui(self, window_ui: UI_AdditionalInformationWindow):
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_AdditionalInformationWindow.

        :param window_ui: The UI_AdditionalInformationWindow to be managed by the Current View.
        :return: None
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> UI_AdditionalInformationWindow:
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_AdditionalInformationWindow.

        :return: The window UI managed by the Current View.
        """
        return self.window_ui

    def update_content(self, line_to_display: LineToRead) -> None:
        """

        No specific Line is needed to feed the corresponding Window.

        The user only have to provide The Defect Code and the Comments as Inputs.

        :param line_to_display :
        :return: None
        """
        # We're just going to pass then...
        pass
