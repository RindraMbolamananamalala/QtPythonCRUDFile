# -*- coding: utf-8 -*-

"""
crud_file_view_single_window.py: The python file dedicated to the "View" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.ui_Main_Window_UI import Ui_MainWindow

from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead


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

    def set_open_connections_lines(self, open_connections_lines: list):
        self.open_connections_lines = open_connections_lines

    def get_open_connections_lines(self) -> list:
        return self.open_connections_lines

    def set_shorts_lines(self, shorts_lines: list):
        self.shorts_lines = shorts_lines

    def get_shorts_lines(self) -> list:
        return self.shorts_lines

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

            # All the Boxes located in the Top sections must be set to ReadOnly
            self.disable_permanently_the_top_section_boxes()

            # First (default) check of the availabilities of all the Confirm Buttons
            self.update_the_availability_of_the_open_connections_button_confirm()
            self.update_the_availability_of_the_shorts_button_confirm()
            self.update_the_availability_of_the_additional_information_button_confirm()

            # Managing all the Events
            self.manage_events()
        else:
            # An invalid number of arguments was provided
            msg_error = "Invalid number of arguments given for the instantiation of a View"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception

    def update_main_window(self, file: FileToRead):
        # First of all, let's clear the whole Main Window
        self.clear_main_window()

        # Let's split the Lines contained under the file into 2, respectively for the Open Connections
        # and for the Shorts parts
        self.set_open_connections_lines([])
        self.set_shorts_lines([])

        for line in file.get_lines_to_read():
            if line.get_type().upper() in ["TESTSWITCH", "TESTCONNECTION"
                                            , "TESTBUSCONNECTORGROUP", "TESTBUSCONNECTORGROUPOPEN"
                                            , "TESTBUSCONNECTORGROUPDETECTION"]:
                self.get_open_connections_lines().append(line)
            elif line.get_type().upper() in ["ISOLATIONTEST"]:
                self.get_shorts_lines().append(line)
            else:
                LOGGER.info(str(line) + " is not concerned by the selection")

        # Updating the Label File Id
        self.get_main_window_ui().get_label_file_id().setText(file.get_uut())

        # Updating the Open Connections (Top) part
        self.update_open_connections_part()

        # Updating the Shorts (Bottom) part
        self.update_shorts_part()

    def update_open_connections_part(self):
        for line in self.get_open_connections_lines():
            self.get_main_window_ui().get_list_open_connections_name().addItem(line.get_name())
            # Making each Item identifiable by its "Line Item" number
            count = self.get_main_window_ui().get_list_open_connections_name().count()
            self.get_main_window_ui().get_list_open_connections_name().item(count - 1).setToolTip(str(line.get_item()))

    def update_shorts_part(self):
        for line in self.get_shorts_lines():
            self.get_main_window_ui().get_list_shorts_name().addItem(line.get_from_pins() + "|" + line.get_to_pins())
            # Making each Item identifiable by its "Line Item" number
            count = self.get_main_window_ui().get_list_shorts_name().count()
            self.get_main_window_ui().get_list_shorts_name().item(count - 1).setToolTip(str(line.get_item()))

    def manage_events(self):
        # List Open Connections Name
        self.get_main_window_ui().get_list_open_connections_name().clicked.connect(self.update_open_connections_boxes)
        self.get_main_window_ui().get_list_open_connections_name().clicked.connect(
            self.update_the_availability_of_the_open_connections_button_confirm
        )

        # Open Connections Comments  text area
        self.get_main_window_ui().get_text_open_connections_comments().textChanged.connect(
            self.update_the_availability_of_the_open_connections_button_confirm
        )

        # List Shorts Name
        self.get_main_window_ui().get_list_shorts_name().clicked.connect(
            self.update_the_availability_of_the_shorts_button_confirm
        )

        # Shorts Comments  text area
        self.get_main_window_ui().get_text_shorts_comments().textChanged.connect(
            self.update_the_availability_of_the_shorts_button_confirm
        )

        # Additional information window appears when button "Add additional information" is clicked
        self.get_main_window_ui().get_button_add_additional_information().clicked.connect(
            self.open_additional_information_window)

        # Additional information comments text area
        self.get_main_window_ui().get_additional_information_window().get_text_additional_information_comments()\
            .textChanged.connect(self.update_the_availability_of_the_additional_information_button_confirm)

        # When the "Cancel" button of the Additional Information window is clicked, the latter closes
        self.get_main_window_ui().get_additional_information_window().get_set_button_additional_information_cancel() \
            .clicked.connect(self.close_additional_information_window)

    def update_open_connections_boxes(self):
        # First, clearing all the boxes
        self.clear_open_connections_boxes()

        # Getting the current line corresponding to the current item
        current_item = self.get_main_window_ui().get_list_open_connections_name().currentItem()
        if current_item is not None:
            current_line = next((x for x in self.get_open_connections_lines()
                                 # Let's remind it that teh item's tooltip corresponds to the Line's Item number
                                 if str(x.get_item()) == current_item.toolTip())
                                , None)
            if current_line:
                # Wire Name
                try:
                    wire_name = current_line.get_name().split("/")[0]
                    self.get_main_window_ui().get_text_wire_name().setPlainText(wire_name)
                except:
                    self.get_main_window_ui().get_text_wire_name().setPlainText("")

                # Cross section
                try:
                    cross_section = current_line.get_name().split("`")[0].split("/")[1]
                    self.get_main_window_ui().get_text_cross_section().setPlainText(cross_section)
                except:
                    self.get_main_window_ui().get_text_cross_section().setPlainText("")

                # Color
                try:
                    color = current_line.get_name().split("`")[1]
                    self.get_main_window_ui().get_text_color().setPlainText(color)
                except:
                    self.get_main_window_ui().get_text_color().setPlainText("")

                # Position 1
                try:
                    position_1 = current_line.get_from_pins().split(".")[0]
                    self.get_main_window_ui().get_text_position_1().setPlainText(position_1)
                except:
                    self.get_main_window_ui().get_text_position_1().setPlainText("")

                # Cavity 1
                try:
                    cavity_1 = current_line.get_from_pins().split(".")[1]
                    self.get_main_window_ui().get_text_cavity_1().setPlainText(cavity_1)
                except:
                    self.get_main_window_ui().get_text_cavity_1().setPlainText("")

                # Position 2
                try:
                    position_2 = current_line.get_to_pins().split(".")[0]
                    self.get_main_window_ui().get_text_position_2().setPlainText(position_2)
                except:
                    self.get_main_window_ui().get_text_position_2().setPlainText("")

                # Cavity 2
                try:
                    cavity_2 = current_line.get_to_pins().split(".")[1]
                    self.get_main_window_ui().get_text_cavity_2().setPlainText(cavity_2)
                except:
                    self.get_main_window_ui().get_text_cavity_2().setPlainText("")
            else:
                LOGGER.error("No valid item is selected")

    def open_additional_information_window(self):
        """
        Opening the Additional information window
        :return: None
        """
        self.get_main_window_ui().get_additional_information_window().get_main_window().show()

    def close_additional_information_window(self):
        """
        Closing the Additional information window
        :return: None
        """
        self.get_main_window_ui().get_additional_information_window().get_main_window().close()

    def clear_open_connections_boxes(self):
        self.get_main_window_ui().get_text_wire_name().clear()
        self.get_main_window_ui().get_text_cross_section().clear()
        self.get_main_window_ui().get_text_color().clear()
        self.get_main_window_ui().get_text_position_1().clear()
        self.get_main_window_ui().get_text_cavity_1().clear()
        self.get_main_window_ui().get_text_position_2().clear()
        self.get_main_window_ui().get_text_cavity_2().clear()

    def clear_main_window(self):
        self.clear_open_connections_boxes()
        self.get_main_window_ui().get_label_file_id().setText("")
        self.get_main_window_ui().get_list_open_connections_name().clear();
        self.clear_open_connections_boxes()
        self.get_main_window_ui().get_text_open_connections_comments().clear()
        self.get_main_window_ui().get_list_shorts_name().clear()
        self.get_main_window_ui().get_text_shorts_comments().clear()

    def disable_permanently_the_top_section_boxes(self):
        """
        All the Boxes located in the Top sections must be set to ReadOnly.
        :return: None
        """
        self.get_main_window_ui().get_text_wire_name().setReadOnly(True)
        self.get_main_window_ui().get_text_cross_section().setReadOnly(True)
        self.get_main_window_ui().get_text_color().setReadOnly(True)
        self.get_main_window_ui().get_text_position_1().setReadOnly(True)
        self.get_main_window_ui().get_text_cavity_1().setReadOnly(True)
        self.get_main_window_ui().get_text_position_2().setReadOnly(True)
        self.get_main_window_ui().get_text_cavity_2().setReadOnly(True)

    def update_the_availability_of_the_open_connections_button_confirm(self):
        """
        Never make the the Open Connections Confirm Button available when No Name in the list is selected and/or
        no text is present within the Comments Text area.
        :return: None
        """
        main_window = self.get_main_window_ui()
        availability = main_window.get_list_open_connections_name().currentItem() is not None \
                       and (len(main_window.get_text_open_connections_comments().toPlainText()) > 0)
        main_window.get_button_open_connections_confirm().setDisabled(not availability)

    def update_the_availability_of_the_shorts_button_confirm(self):
        """
        Never make the the Shorts Confirm Button available when No Name in the list is selected and/or
        no text is present within the Comments Text area.
        :return: None
        """
        main_window = self.get_main_window_ui()
        availability = main_window.get_list_shorts_name().currentItem() is not None \
                       and (len(main_window.get_text_shorts_comments().toPlainText()) > 0)
        main_window.get_button_shorts_confirm().setDisabled(not availability)

    def update_the_availability_of_the_additional_information_button_confirm(self):
        """
        Never make the the Shorts Confirm Button available when No Name in the list is selected and/or
        no text is present within the Comments Text area.
        :return: None
        """
        main_window = self.get_main_window_ui()
        additional_information_window = main_window.get_additional_information_window()
        availability = (len(additional_information_window.get_text_additional_information_comments().toPlainText()) > 0)
        additional_information_window.get_button_additional_information_confirm().setDisabled(not availability)
