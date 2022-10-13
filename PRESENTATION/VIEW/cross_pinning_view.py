# -*- coding: utf-8 -*-

"""
cross_pinning_view.py: The python file dedicated to the Cross Pinning "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from functools import partial

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.ui_Cross_Pinning import UI_CrossPinning
from PRESENTATION.VIEW.crud_file_view import CRUDFileView

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read_cross_pinning import LineToReadCrossPinning


def deduce_left_part_content(line_to_display: LineToReadCrossPinning) -> list:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A list of formatted texts to be displayed on the Left Part
    """
    try:
        i = 0
        texts_to_return = []
        for from_pin in line_to_display.get_from_pins():
            line_from_pins = from_pin
            line_from_pins_comment = line_to_display.get_from_pins_comment()[i]
            texts_to_return.append(
                "<html>" \
                "<body>" \
                "<p>" \
                + line_from_pins \
                + "<span style=\" vertical-align:sub;\">" \
                + "[" + line_from_pins_comment + "]" \
                + "</span>" \
                  "</p>" \
                  "</body>" \
                  "</html>")
            # Next Line of From Pin
            i = i + 1
        return texts_to_return
    except Exception as ex:
        error_msg = "A void list was returned." + " " + "An error was encountered : " + str(ex) + " ."
        LOGGER.error(error_msg)
        return []


def deduce_middle_part_content(line_to_display: LineToReadCrossPinning) -> list:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A list of formatted texts to be displayed on the Middle Part
    """
    try:
        i = 0
        texts_to_return = []
        for to_pin in line_to_display.get_to_pins():
            line_to_pins = to_pin
            line_to_pins_comment = line_to_display.get_to_pins_comment()[i]
            texts_to_return.append(
                "<html>" \
                "<body>" \
                "<p>" \
                + line_to_pins \
                + "<span style=\" vertical-align:sub;\">" \
                + "[" + line_to_pins_comment + "]" \
                + "</span>" \
                  "</p>" \
                  "</body>" \
                  "</html>"
            )
            # Next Line of To Pin
            i = i + 1
        return texts_to_return
    except Exception as ex:
        error_msg = "A void list was returned." + " " + "An error was encountered : " + str(ex) + " ."
        LOGGER.error(error_msg)
        return []


def deduce_right_part_content(line_to_display: LineToReadCrossPinning) -> list:
    """

    :param line_to_display: The line from which the part of the content will be deduced
    :return: A list of formatted texts to be displayed on the Right Part
    """
    try:
        texts_to_return = []
        for splice in line_to_display.get_splices_list():
            texts_to_return.append(
                "<html>" \
                "<body>" \
                "<p>" \
                + splice + \
                "</p>" \
                "</body>" \
                "</html>"
            )
        return texts_to_return
    except Exception as ex:
        error_msg = "A void list was returned." + " " + "An error was encountered : " + str(ex) + " ."
        LOGGER.error(error_msg)
        return []


class CrossPinningView(CRUDFileView):
    # A specific Counter dedicated to the selection of items which will play the role of "POSITION 1" and "POSITION 2"
    label_color_cpt = 0

    def set_window_ui(self, window_ui: UI_CrossPinning):
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_CrossPinning.

        :param window_ui: The UI_CrossPinning to be managed by the Current View.
        :return: None
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> UI_CrossPinning:
        """
        Even though the setter/getter are already initialized at the level of the Superclass, it's better and convenient
        to always precise the type of Window UI to be managed by the current View: UI_CrossPinning.

        :return: The window UI managed by the Current View.
        """
        return self.window_ui

    def set_selected_from_item_label(self, selected_from_item_label: QLabel):
        """

        :param selected_from_item_label: The "From" item label selected
        :return: None
        """
        self.selected_from_item_label = selected_from_item_label
        if self.get_selected_from_item_label():
            # If not None, setting the color of the label to Green
            self.get_selected_from_item_label().setStyleSheet("color: green")

    def get_selected_from_item_label(self) -> QLabel:
        """

        :return: The "From" item label selected
        """
        return self.selected_from_item_label

    def set_selected_to_item_label(self, selected_to_item_label: QLabel):
        """

        :param selected_to_item_label: The "To" item label selected
        :return:
        """
        self.selected_to_item_label = selected_to_item_label
        if self.get_selected_to_item_label():
            # If not None, setting the color of the label to Red
            self.get_selected_to_item_label().setStyleSheet("color: red")

    def get_selected_to_item_label(self) -> QLabel:
        """

        :return: The "To" item label selected
        """
        return self.selected_to_item_label

    def __init__(self, *args):
        # Calling the constructor of the Superclass in order to obtain the needed default behaviors
        super(CrossPinningView, self).__init__(*args)

        if len(args) == 1:
            # All the configurations have been managed during the call of the Superclass' Constructor
            pass

        # At the beginning, no Item Label is selected on the Window
        self.set_selected_from_item_label(None)
        self.set_selected_to_item_label(None)

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
        selected_from_item_label = self.get_selected_from_item_label()
        selected_to_item_label = self.get_selected_to_item_label()
        button_confirm = self.get_window_ui().get_button_confirm()
        button_done = self.get_window_ui().get_button_done()
        buttons_availabilities = (len(combobox_fed_by_excel_sheet.currentText()) > 0) \
                                 & (len(text_comments.toPlainText()) > 0) \
                                 & (selected_to_item_label is not None) \
                                 & (selected_from_item_label is not None)
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
        self.reset_current_selections()

    def update_content(self, line_to_display: LineToReadCrossPinning) -> None:
        """
        Updating the current content of the Open Wires Window from a given Line of information.

        :param line_to_display: The line the information of which are to be displayed on the Open Wires Window
        :return:  None
        """
        try:
            """
            First, re-initialize the entire WINDOW
            """
            # No selected label or selectable label...
            self.set_selected_from_item_label(None)
            self.set_selected_to_item_label(None)
            self.get_window_ui().reset_all_items_labels_color()
            self.get_window_ui().set_label_items([])
            # Clearing the content of the Window
            self.get_window_ui().clear_window()
            self.clear_data()

            # Left Part for the possible From Pins
            self.get_window_ui().feed_widget_left_part(deduce_left_part_content(line_to_display))

            # Middle Part's Line's Name
            line_name_initial = line_to_display.get_name()
            color = line_name_initial.split("`")[1]
            wire_name = line_name_initial.split("`")[0].split("/")[0]
            cross_section = line_name_initial.split("`")[0].split("/")[1]
            line_name_transformed = wire_name + "  " + cross_section + "  " + color
            self.get_window_ui().get_label_name().setText(line_name_transformed)

            # Middle Part for possible To Pins
            self.get_window_ui().feed_widget_middle_part(deduce_middle_part_content(line_to_display))

            # Right part for the Splices
            self.get_window_ui().feed_widget_right_part(deduce_right_part_content(line_to_display))

            # Managing the Events related to the recently-added Items
            self.manage_cross_pinning_items_event()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Update Process related to the Cross Pinning Window. "
            )
            raise

    def manage_cross_pinning_items_event(self):
        """
        Managing any Event related to the Items present on the Cross Pinning window
        :return: None
        """
        # Each Label of Item present within the Treatment area could play the role of the "POSITION 1" or "POSITION2"
        # in function of the Client's selection
        for label in self.get_window_ui().get_label_items():
            label.clicked.connect(partial(self.update_item_selection, selected_label=label))

    def reset_current_selections(self):
        """
        Resetting the Window with no item selected
        :return:
        """
        # No item selected...
        self.set_selected_from_item_label(None)
        self.set_selected_to_item_label(None)

        # ... so the cpt of label selected is set to 0 again...
        self.label_color_cpt = 0

        # ... and finally, let's set the colors of the items to the default one (white)
        self.get_window_ui().reset_all_items_labels_color()

    def update_label_color_cpt(self):
        """
        A little implementation of an Automata with 2 states:
            - state "0"'s next state : state "1";
            - state "1"'s next state : state "O";

        :return: None
        """
        self.label_color_cpt = (self.label_color_cpt + 1) % 2

    def update_item_selection(self, selected_label: QLabel):
        """
        Based on the above Automata, the selection of labels will be managed in function of various situations to be
        considered when a new Label is newly selected.


        :param selected_label: The newly selected Label
        :return: None
        """
        try:
            if self.label_color_cpt == 0:
                # The current state is "0"
                if selected_label == self.get_selected_to_item_label():
                    """
                    The newly selected label is already selected as the "POSITION 2", so, the client is just asking
                    for a new selection of another item for the "POSITION 2" 
                    """
                    # so, first, let's change its color to white (again)...
                    self.get_selected_to_item_label().setStyleSheet("color: white")
                    # ... then, let's not select any item for the "POSITION 2"...
                    self.set_selected_to_item_label(None)
                    # ... finally, let's go back to the state "1" for the next step.
                    self.label_color_cpt = 1
                else:
                    # Not selected as the "POSITION 2" then...
                    if self.get_selected_from_item_label() is not None:
                        # ... and an Item is already selected for the "POSITION 1"...
                        # ... so, it's the current "POSITION 1" the problem....
                        # ... therefore, let's RESET the entire selection FIRST...
                        self.reset_current_selections()
                    # (... and) select teh new "POSITION 1"'item.
                    self.set_selected_from_item_label(selected_label)

                    # Transition to the Next state.
                    self.update_label_color_cpt()
            else:
                # The current state is "1"
                if selected_label == self.get_selected_from_item_label():
                    """
                    The newly selected label is already selected as the "POSITION 1"
                    """
                    # so, the Client has requested a RESET of all the selection.
                    self.reset_current_selections()
                else:
                    """
                    The newly selected label is not yet selected as the "POSITION 1"
                    """
                    if self.get_selected_to_item_label() is not None:
                        # and another item is already selected for the "POSITION 2"...

                        # ....so, just a little change of this item for the "POSITION 2" then...

                        # color: re-set to white (default)...
                        self.get_selected_to_item_label().setStyleSheet("color: white")

                        # and, let's not select any item for the "POSITION 2".
                        self.set_selected_to_item_label(None)
                    # Now, it's time to set the "POSITION 2" to the newly selected Item...
                    self.set_selected_to_item_label(selected_label)

                    # ... without forgetting the transition of state.
                    self.update_label_color_cpt()

            # Updating the availabilities of the Buttons
            self.update_buttons_availabilities()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the Update process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Update Process. "
            )
            raise
