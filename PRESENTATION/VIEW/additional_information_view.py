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

    def __init__(self, *args):
        # Calling the constructor of the Superclass in order to obtain the needed default behaviors
        super(AdditionalInformationView, self).__init__(*args)

        if len(args) == 1:
            # All the configurations have been managed during the call of the Superclass' Constructor

            # At the beginning, the 2 buttons are disabled
            self.get_window_ui().get_button_confirm().setEnabled(False)
            self.get_window_ui().get_button_done().setEnabled(False)
            self.get_window_ui().get_button_confirm().setStyleSheet("background-color: lightgrey;")
            self.get_window_ui().get_button_done().setStyleSheet("background-color: lightgrey;")

            # Management of Events
            self.manage_events()

    def manage_events(self):
        """
        Managing the various events related to the different components to bring the necessary general updates
        one the Window.

        :return:
        """
        self.get_window_ui().get_combobox_fed_by_excel_sheet().currentIndexChanged.connect(
            self.update_buttons_availabilities
        )
        self.get_window_ui().get_text_comments().textChanged.connect(self.update_buttons_availabilities)
        self.get_window_ui().get_button_confirm().clicked.connect(self.update_buttons_availabilities)
        self.get_window_ui().get_button_done().clicked.connect(self.update_buttons_availabilities)

    def update_buttons_availabilities(self):
        """
        The availabilities of the "Confirm" and "Done" Buttons relies on the validity of the information provided
        as the User's inputs.

        :return: None
        """
        combobox_fed_by_excel_sheet = self.get_window_ui().get_combobox_fed_by_excel_sheet()
        text_comments = self.get_window_ui().get_text_comments()
        button_confirm = self.get_window_ui().get_button_confirm()
        button_done = self.get_window_ui().get_button_done()
        buttons_availabilities = (len(combobox_fed_by_excel_sheet.currentText()) > 0) \
                                 & (len(text_comments.toPlainText()) > 0)
        button_confirm.setEnabled(buttons_availabilities)
        button_done.setEnabled(buttons_availabilities)
        if not buttons_availabilities:
            button_confirm.setStyleSheet("background-color: lightgrey;")
            button_done.setStyleSheet("background-color: lightgrey;")
        else:
            button_confirm.setStyleSheet("background-color: grey;")
            button_done.setStyleSheet("background-color: grey;")

    def clear_data(self):
        """
        Resetting the data contained on the Window

        :return: None
        """
        self.get_window_ui().get_text_comments().setPlainText("")
