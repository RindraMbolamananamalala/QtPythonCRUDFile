# -*- coding: utf-8 -*-

"""
open_wires_view_.py: The python file dedicated to the Open Wires "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from PRESENTATION.HMI.ui_Open_Wires import UI_OpenWires
from PRESENTATION.VIEW.crud_file_view import CRUDFileView


def deduce_label_left_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Left Part of the Window's content.
    """
    try:
        line_from_pins = line_to_display.get_from_pins()
        line_from_pins_comment = line_to_display.get_from_pins_comment()
        line_to_pins = line_to_display.get_to_pins()
        line_to_pins_comment = line_to_display.get_to_pins_comment()
        content_to_return = "<html>" \
                                "<body>" \
                                    "<p>" \
                                        + line_from_pins + \
                                        "<BR>" \
                                        +"[" + line_from_pins_comment + "]" + \
                                        "</BR>" \
                                        "<BR>" \
                                        "</BR>" \
                                    "</p>" \
                                    "<p>" \
                                        "<span>" \
                                            + line_to_pins +\
                                        "</span>" \
                                        "<BR>" \
                                        + "[" + line_to_pins_comment+ "]" + \
                                        "</BR>" \
                                    "</p>" \
                                "</body>" \
                            "</html>"
        return content_to_return
    except:
        return ""


def deduce_label_middle_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Middle Part of the Window's content.
    """
    try:
        color = line_to_display.get_name().split("`")[1]
        return color
    except:
        return ""


def deduce_label_right_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Right Part of the Window's content.
    """
    try:
        wire_name_plus_cross_section = line_to_display.get_name().split("`")[0]
        return wire_name_plus_cross_section
    except:
        return ""


class OpenWiresView(CRUDFileView):

    def set_window_ui(self, window_ui: UI_OpenWires):
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_OpenWires.

        :param window_ui: The UI_OpenWires to be managed by the Current View.
        :return: None
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> UI_OpenWires:
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_OpenWires.

        :return: The window UI managed by the Current View.
        """
        return self.window_ui

    def update_content(self, line_to_display: LineToRead) -> None:
        """
        Updating the current content of the Open Wires Window from a given Line of information.

        :param line_to_display: The line the information of which are to be displayed on the Open Wires Window
        :return:  None
        """
        try:
            # First, let's clear the data
            self.clear_data()

            # Left Part for the Pins
            self.get_window_ui().get_label_left_part().setText(deduce_label_left_part_content(line_to_display))
            # However, we need to store the original main information on the Pins in order to use them later (for the
            # WRITE).
            # We're gonna exploit the Left Label's Tooltip for that.
            pins_info = line_to_display.get_from_pins() + "[" + line_to_display.get_from_pins_comment() + "]" \
                                + "->" \
                                + line_to_display.get_to_pins() + "[" + line_to_display.get_to_pins_comment() + "]"
            self.get_window_ui().get_label_left_part().setToolTip(pins_info)

            # Middle Part for the Color
            self.get_window_ui().get_label_middle_part().setText(deduce_label_middle_part_content(line_to_display))

            # Right part for Wire Name & Cross Section
            self.get_window_ui().get_label_right_part().setText(deduce_label_right_part_content(line_to_display))
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Update Process related to the Open Wires Window. "
            )
            raise

    def __init__(self, *args):
        # Calling the constructor of the Superclass in order to obtain the needed default behaviors
        super(OpenWiresView, self).__init__(*args)

        if len(args) == 1:
            # All the configurations have been managed during the call of the Superclass' Constructor

            # At the beginning, the Confirm button is disabled
            self.get_window_ui().get_button_confirm().setEnabled(False)
            self.get_window_ui().get_button_confirm().setStyleSheet("background-color: lightgrey;")

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

    def update_buttons_availabilities(self):
        """
        The availabilities of the "Confirm" and "Done" Buttons relies on the validity of the information provided
        as the User's inputs.

        :return: None
        """
        combobox_fed_by_excel_sheet = self.get_window_ui().get_combobox_fed_by_excel_sheet()
        text_comments = self.get_window_ui().get_text_comments()
        button_confirm = self.get_window_ui().get_button_confirm()
        button_availability = (len(combobox_fed_by_excel_sheet.currentText()) > 0) \
                                 & (len(text_comments.toPlainText()) > 0)
        button_confirm.setEnabled(button_availability)
        if not button_availability:
            button_confirm.setStyleSheet("background-color: lightgrey;")
        else:
            button_confirm.setStyleSheet("background-color: grey;")

    def clear_data(self):
        """
        Resetting the data contained on the Window

        :return: None
        """
        self.get_window_ui().get_text_comments().setPlainText("")



