# -*- coding: utf-8 -*-

"""
open_wires_view_.py: The python file dedicated to the Open Wires "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from PRESENTATION.HMI.ui_Open_Wires import UI_OpenWires
from PRESENTATION.VIEW.crud_file_view import CRUDFileView


def deduce_label_left_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Left Part of the Window's content.
    """
    try:
        wire_name_plus_cross_section = line_to_display.get_name().split("`")[0]
        wire_name = wire_name_plus_cross_section.split("/")[0]
        cross_section = wire_name_plus_cross_section.split("/")[1]
        color = line_to_display.get_name().split("`")[1]
        content_to_return = wire_name + "   " + cross_section + "   " + color
        return content_to_return
    except:
        # Impossible decomposition into different parts of the line's name, so let's use the latter in its raw format
        return line_to_display.get_name()


def deduce_label_middle_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Middle Part of the Window's content.
    """
    try:
        line_from_pins = line_to_display.get_from_pins()
        return line_from_pins
    except:
        return ""


def deduce_label_right_part_content(line_to_display: LineToRead) -> str:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A formatted text for the Label at the Right Part of the Window's content.
    """
    try:
        line_to_pins = line_to_display.get_to_pins()
        return line_to_pins
    except:
        return ""


def does_text_need_button_skip_activation(text: str) -> bool:
    """
    Deteremining if YES or NO given text does require the activation of the Open Wires'"Skip" button
    :param text: The concerned text
    :return: TRUE if the concerned text requires the activation of the Open Wires'"Skip" button, FALSE otherwise.
    """
    exclusion_list = get_application_property("open_wires_exclusion_list").split(",")
    return text in exclusion_list


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

    def set_current_lines_list_total_length(self, current_lines_list_total_length: int):
        self.current_lines_list_total_length = current_lines_list_total_length

    def get_current_lines_list_total_length(self) -> int:
        return self.current_lines_list_total_length

    def update_content(self, line_to_display: LineToRead, current_lines_list_updated_length: int) -> None:
        """
        Updating the current content of the Open Wires Window from a given Line of information.

        :param line_to_display: The line the information of which are to be displayed on the Open Wires Window
        :param current_lines_list_updated_length: The updated length of the current List of Lines to be displayed
        :return:  None
        """
        try:
            # First, let's clear the data
            self.clear_data()

            # Updating the Lines Treated Counter's Label
            current_line_order = self.get_current_lines_list_total_length() - current_lines_list_updated_length
            self.get_window_ui().get_label_lines_treated_counter().setText(
                str(current_line_order) + "/" + str(self.get_current_lines_list_total_length())
            )

            # Left Part for the <WIRE_NAME   CROSS_SECTION   COLOR>
            self.get_window_ui().get_label_left_part().setText(deduce_label_left_part_content(line_to_display))
            # An update of the buttons' availabilities is required after the update of the Label of the Left Part
            self.update_buttons_availabilities()
            # However, we need to store the original main information on the Pins in order to use them later (for the
            # WRITE).
            # We're gonna exploit the Left Label's Tooltip for that.
            pins_info = line_to_display.get_from_pins() + "[" + line_to_display.get_from_pins_comment() + "]" \
                                + "->" \
                                + line_to_display.get_to_pins() + "[" + line_to_display.get_to_pins_comment() + "]"
            self.get_window_ui().get_label_left_part().setToolTip(pins_info)

            # Middle Part for the FROM PINS
            self.get_window_ui().get_label_middle_part().setText(deduce_label_middle_part_content(line_to_display))

            # Right part for TO PINS
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

            # At the beginning, the "Confirm" and "Skip" buttons are disabled
            self.get_window_ui().get_button_confirm().setEnabled(False)
            self.get_window_ui().get_button_confirm().setStyleSheet("background-color: lightgrey;")
            self.get_window_ui().get_button_skip().setEnabled(False)
            self.get_window_ui().get_button_skip().setStyleSheet("background-color: lightgrey;")

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
        self.get_window_ui().get_button_confirm().clicked.connect(self.update_buttons_availabilities)

    def update_buttons_availabilities(self):
        """
        The availabilities of the "Confirm", "Done" and "Skip" Buttons rely on the the information provided as the
        User's inputs.

        :return: None
        """
        combobox_fed_by_excel_sheet = self.get_window_ui().get_combobox_fed_by_excel_sheet()
        text_label_left_part = self.get_window_ui().get_label_left_part().text()
        # Availability of the button "Confirm"
        button_confirm = self.get_window_ui().get_button_confirm()
        button_confirm_availability = (len(combobox_fed_by_excel_sheet.currentText()) > 0)
        button_confirm.setEnabled(button_confirm_availability)
        if not button_confirm_availability:
            button_confirm.setStyleSheet("background-color: lightgrey;")
        else:
            button_confirm.setStyleSheet("background-color: #d9d9d9; color: #4b4b4b;")
        # Availability of the button "Skip"
        button_skip = self.get_window_ui().get_button_skip()
        button_skip_availability = (len(text_label_left_part) > 0)\
                                   & does_text_need_button_skip_activation(text_label_left_part)
        button_skip.setEnabled(button_skip_availability)
        if not button_skip_availability:
            button_skip.setStyleSheet("background-color: lightgrey;")
        else:
            button_skip.setStyleSheet("background-color: #d9d9d9; color: #4b4b4b;")

    def clear_data(self):
        """
        Resetting the data contained on the Window

        :return: None
        """
        self.get_window_ui().get_text_comments().setPlainText("")



