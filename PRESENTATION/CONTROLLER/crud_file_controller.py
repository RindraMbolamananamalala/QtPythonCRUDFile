# -*- coding: utf-8 -*-

"""
crud_file_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import time
import os

from PySide2.QtWidgets import *

from CONFIGURATIONS.application_properties import get_application_property

from CONFIGURATIONS.logger import LOGGER

from UTILS.ENUMS.line_types_enum import LineTypesEnum
from UTILS.time_utils import get_current_time, get_current_date

from MAPPER.crud_file_mapper import file_to_read_dto_to_file_to_read

from PRESENTATION.HMI.ui_Loading_Window import Ui_window_loading
from PRESENTATION.HMI.ui_Cross_Pinning import UI_CrossPinning
from PRESENTATION.HMI.ui_Open_Wires import UI_OpenWires
from PRESENTATION.HMI.ui_Shorts import UI_Shorts
from PRESENTATION.HMI.ui_Additional_Information_Window import UI_AdditionalInformationWindow

from PRESENTATION.VIEW.loading_window_view import LoadingWindowView
from PRESENTATION.VIEW.cross_pinning_view import CrossPinningView
from PRESENTATION.VIEW.open_wires_view import OpenWiresView
from PRESENTATION.VIEW.shorts_view import ShortsView
from PRESENTATION.VIEW.additional_information_view import AdditionalInformationView

from BUSINESS.CONSTRAINTS.CONVERTER.text_converter import html_content_to_simple_text
from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead
from BUSINESS.MODEL.DTO.line_to_write_dto import LineToWriteDTO
from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.crud_file_as_intf import CRUDFileASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.crud_file_as_impl import CRUDFileASImpl


class CRUDFileController:

    def set_current_view(self, current_view):
        """

        :param current_view:  The current View to be managed by the Controller
        :return:
        """
        self.current_view = current_view

    def get_current_view(self):
        """

        :return: The current View managed by the controller
        """
        return self.current_view

    def set_loading_window_view(self, loading_window_view: LoadingWindowView):
        """

        :param loading_window_view: The View associated with the Loading Window
        :return:
        """
        self.loading_window_view = loading_window_view

    def get_loading_window_view(self) -> LoadingWindowView:
        """

        :return: The View associated with the Loading Window
        """
        return self.loading_window_view

    def set_cross_pinning_view(self, cross_pinning_view: CrossPinningView):
        """

        :param cross_pinning_view: The Cross Pinning View part to be associated with the Controller part within the MVC
        Implementation at the level of the Presentation Layer of the Project.
        :return: None
        """
        self.cross_pinning_view = cross_pinning_view

    def get_cross_pinning_view(self) -> CrossPinningView:
        """

        :return: The Cross Pinning View part associated with the Controller part within the MVC Implementation at the
        level of the Presentation Layer of the Project.
        """
        return self.cross_pinning_view

    def set_open_wires_view(self, open_wires_view: OpenWiresView):
        """

        :param open_wires_view: The Open Wires View part to be associated with the Controller part within the MVC
        Implementation at the level of the Presentation Layer of the Project.
        :return: None
        """
        self.open_wires_view = open_wires_view

    def get_open_wires_view(self) -> OpenWiresView:
        """

        :return: The Open Wires View part associated with the Controller part within the MVC Implementation at the
        level of the Presentation Layer of the Project.
        """
        return self.open_wires_view

    def set_shorts_view(self, shorts_view: ShortsView):
        """

        :param open_wires_view: The Open Wires View part to be associated with the Controller part within the MVC
        Implementation at the level of the Presentation Layer of the Project.
        :return: None
        """
        self.shorts_view = shorts_view

    def get_shorts_view(self) -> ShortsView:
        """

        :return: The Shorts View part associated with the Controller part within the MVC Implementation at the
        level of the Presentation Layer of the Project.
        """
        return self.shorts_view

    def set_additional_information_view(self, additional_information_view: AdditionalInformationView):
        """

        :param additional_information_view: The Additional Information View part to be associated with the Controller
        part within the MVC Implementation at the level of the Presentation Layer of the Project.
        :return: None
        """
        self.additional_information_view = additional_information_view

    def get_additional_information_view(self) -> AdditionalInformationView:
        """

        :return: The Shorts View part associated with the Controller part within the MVC Implementation at the
        level of the Presentation Layer of the Project.
        """
        return self.additional_information_view

    def set_crud_file_as(self, crud_file_as: CRUDFileASIntf):
        """

        :param crud_file_as: The CRUD File Application Service to be used by the current Controller
        :return:
        """
        self.crud_file_as = crud_file_as

    def get_crud_file_as(self) -> CRUDFileASIntf:
        """

        :return: The CRUD File Application Service used by the current Controller
        """
        return self.crud_file_as

    def set_file_queue(self, file_queue: list):
        """

        :param file_queue: The Queue of Files which related events are handled by the CRUD File handler
        :return: None
        """
        self.file_queue = file_queue

    def get_file_queue(self) -> list:
        """

        :return: The Queue of Files which related events are handled by the CRUD File handler
        """
        return self.file_queue

    def set_current_file(self, current_file: FileToRead):
        """

        :param current_file: The current File To Read Object for the treatments
        :return: None
        """
        self.current_file = current_file

    def get_current_file(self) -> FileToRead:
        """

        :return: The current File To Read Object for the treatments
        """
        return self.current_file

    def set_file_to_delete_path(self, file_to_delete_path: str):
        """

        :param file_to_delete_path: The path of the file to be deleted at the end of the current treatment
        :return: None
        """
        self.file_to_delete_path = file_to_delete_path

    def get_file_to_delete_path(self) -> str:
        """

        :return: The path of the file to be deleted at the end of the current treatment
        """
        return self.file_to_delete_path

    def set_list_lines_cross_pinning(self, list_lines_cross_pinning: list):
        self.list_lines_cross_pinning = list_lines_cross_pinning

    def get_list_lines_cross_pinning(self) -> list:
        return self.list_lines_cross_pinning

    def set_list_lines_open_wires(self, list_lines_open_wires: list):
        self.list_lines_open_wires = list_lines_open_wires

    def get_list_lines_open_wires(self) -> list:
        return self.list_lines_open_wires

    def set_list_lines_shorts(self, list_lines_shorts: list):
        self.list_lines_shorts = list_lines_shorts

    def get_list_lines_shorts(self) -> list:
        return self.list_lines_shorts

    def __init__(self, *args):
        """

        :param crud_file_view: The View Part to be associated with the current Controller
        :param crud_file_as: The Application Service to be associated with the current Controller
        """
        if len(args) == 0:
            """
            Preparing the View Parts
            """
            # Loading Window View
            loading_window_ui = Ui_window_loading(QMainWindow())
            self.set_loading_window_view(LoadingWindowView(loading_window_ui))
            # Cross Pinning View
            cross_pinning_ui = UI_CrossPinning(QMainWindow())
            self.set_cross_pinning_view(CrossPinningView(cross_pinning_ui))
            # Open Wires View
            open_wires_ui = UI_OpenWires(QMainWindow())
            self.set_open_wires_view(OpenWiresView(open_wires_ui))
            # Shorts View
            shorts_ui = UI_Shorts(QMainWindow())
            self.set_shorts_view(ShortsView(shorts_ui))
            # Additional Information View
            additional_information_view = UI_AdditionalInformationWindow(QMainWindow())
            self.set_additional_information_view(AdditionalInformationView(additional_information_view))

            # Initializing the Application Service
            self.set_crud_file_as(CRUDFileASImpl())

            # Feeding the Combo Boxes of the all the Windows
            self.feed_windows_combo_boxes()

            # Initializing the File_Queue
            self.set_file_queue([])

            # Managing the events
            self.manage_events()

            # At the beginning, the first viw is that of Loading Window
            self.set_current_view(self.get_loading_window_view())

            # Starting the treatments
            self.check_current_window()
        elif len(args) == 2:
            # Both the View part and the AS to be used by the Controller were provided
            # Preparing each part
            self.set_crud_file_view(args[0])
            self.set_crud_file_as(args[1])
        else:
            # An invalid number of arguments was provided
            msg_error = "Invalid number of arguments given for the instantiation of a Controller"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception

    def manage_events(self):
        """
        Associating actions with Event(s) at the level of different Components

        :return: None
        """

        # Writing in the Excel File the current content of the Cross Pinning window and then pass to the Open Wires
        # window when the "Done" button is clicked.
        self.get_cross_pinning_view().get_window_ui().get_button_done().clicked.connect(
            self.write_cross_pinning_information_after_done
        )

        # Writing in the Excel File the current content of the Cross Pinning UI when the "Confirm" button is clicked.
        self.get_cross_pinning_view().get_window_ui().get_button_confirm().clicked.connect(
            self.write_cross_pinning_information
        )

        # Writing in the Excel File the current content of the Open Wires UI when the "Confirm" button is clicked.
        self.get_open_wires_view().get_window_ui().get_button_confirm().clicked.connect(
            self.write_open_wires_information
        )

        # Writing in the Excel File the current content of the Extra Wires - Short UI when the "Confirm" button
        # is clicked.
        self.get_shorts_view().get_window_ui().get_button_confirm().clicked.connect(
            self.write_shorts_information
        )

        # Writing in the Excel File the current content of the Additional Information and then just stay there
        # when the "Confirm" button is clicked.
        self.get_additional_information_view().get_window_ui().get_button_confirm().clicked.connect(
            self.write_additional_information
        )

        # Writing in the Excel File the current content of the Additional Information and then go back to the loading
        # Window when the "Done" button is clicked.
        self.get_additional_information_view().get_window_ui().get_button_done().clicked.connect(
            self.write_additional_information_after_done
        )

    def feed_windows_combo_boxes(self):
        """
        Feeding the combo boxes on the main windows, including that of the internal Add Additional information window,
        from their corresponding Excel File
        :return: None
        """
        # Getting the View's Main window
        cross_pinning_window = self.get_cross_pinning_view().get_window_ui()
        open_wires_window = self.get_open_wires_view().get_window_ui()
        shorts_window = self.get_shorts_view().get_window_ui()
        additional_information_window = self.get_additional_information_view().get_window_ui()

        # Getting the respective values
        defects_codes = self.get_crud_file_as().get_defect_codes(
            get_application_property("defect_codes_path")
        )

        """ 
        Actual feeding processes 
        """
        # CROSS PINNING
        for value in defects_codes[0].get_lines():
            cross_pinning_window.get_combobox_fed_by_excel_sheet().addItem\
                (value)

        # OPEN WIRES
        for value in defects_codes[1].get_lines():
            open_wires_window.get_combobox_fed_by_excel_sheet().addItem(value)

        # SHORTS
        for value in defects_codes[2].get_lines():
            shorts_window.get_combobox_fed_by_excel_sheet().addItem(value)

        # ADDITIONAL INFORMATION
        for value in defects_codes[3].get_lines():
            additional_information_window.get_combobox_fed_by_excel_sheet().addItem(value)

    def write_cross_pinning_information(self):
        """
        After clicking the Cross Pinning window's Confirm button, we write the selected information in
        a new Excel File.

        :return: None
        """
        try:
            # Getting the Cross Pinning window of the view
            cross_pinning_view_window_ui = self.get_cross_pinning_view().get_window_ui()

            # Preparing the data that still need pre-processing
            fixed_string_part_1 = cross_pinning_view_window_ui.get_label_fixed_strings().text().split(" - ")[0]
            equipment_name = cross_pinning_view_window_ui.get_label_fixed_strings().text().split(" - ")[1]
            wire_name = cross_pinning_view_window_ui.get_label_name().text().split(" ")[0]
            cross_section = cross_pinning_view_window_ui.get_label_name().text().split(" ")[1]
            color = cross_pinning_view_window_ui.get_label_name().text().split(" ")[2]
            from_pins_info = html_content_to_simple_text(
                self.get_cross_pinning_view().get_selected_from_item_label().text()
            )
            from_pins = from_pins_info.split("[")[0]
            pos_1 = from_pins.split(".")[0]
            cav_1 = from_pins.split(".")[1]
            try:
                from_pins_comment = from_pins_info.split("[")[1].replace("]", "")
            except:
                from_pins_comment = ""
            to_pins_info = html_content_to_simple_text(
                self.get_cross_pinning_view().get_selected_to_item_label().text()
            )
            to_pins = to_pins_info.split("[")[0]
            pos_2 = to_pins.split(".")[0]
            cav_2 = to_pins.split(".")[1]
            try:
                to_pins_comment = to_pins_info.split("[")[1].replace("]", "")
            except:
                to_pins_comment = ""
            defect_code = cross_pinning_view_window_ui.get_combobox_fed_by_excel_sheet().currentText()

            # Now, let's prepare the line to write
            line_to_write = LineToWriteDTO()
            line_to_write.set_uut(cross_pinning_view_window_ui.get_label_uut().text())
            line_to_write.set_fixed_string_part_1(fixed_string_part_1)
            line_to_write.set_equipment_name(equipment_name)
            line_to_write.set_date(get_current_date("%d.%m.%Y"))
            line_to_write.set_time(get_current_time("%I:%M:%S %p"))
            line_to_write.set_wire_name(wire_name)
            line_to_write.set_cross_section(cross_section)
            line_to_write.set_color(color)
            line_to_write.set_position_1(pos_1)
            line_to_write.set_cavity_1(cav_1)
            line_to_write.set_position_2(pos_2)
            line_to_write.set_cavity_2(cav_2)
            line_to_write.set_w(defect_code)
            line_to_write.set_comments(cross_pinning_view_window_ui.get_text_comments().toPlainText())

            # Actual writing
            self.get_crud_file_as().write_modified_line(
                get_application_property("folder_modified_lines_path")
                , line_to_write
            )
            self.get_cross_pinning_view().clear_data()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def write_cross_pinning_information_after_done(self):
        """
        After clicking the Cross Pinning Information Window's Done button, we write the selected information in
        a new Excel File and pass to the next Window (Open Wires Window).

        :return: None
        """
        try:
            # First, just write
            self.write_cross_pinning_information()

            # Now, it's time to :
            # 1- Load another line (If there is still any)
            # OR
            # 2 - Pass to the the Next Step: OPEN WIRES
            if len(self.get_list_lines_cross_pinning()) > 0:
                # There is still any...
                self.get_cross_pinning_view().update_content(self.get_list_lines_cross_pinning().pop())
            else:
                # No more line, let's pass to the Next Step: OPEN WIRES
                self.get_current_view().get_window_ui().get_main_window().close()
                self.set_current_view(self.get_open_wires_view())
                self.get_current_view().get_window_ui().get_main_window().showMaximized()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def write_open_wires_information(self):
        try:
            """
            After clicking the Open Wires window Confirm button, we write the selected information in
            a new Excel File.
            
            :return: None
            """
            # Getting the Open Wires window of the view
            open_wires_view_window_ui = self.get_open_wires_view().get_window_ui()

            # Preparing the data that still need pre-processing
            fixed_string_part_1 = open_wires_view_window_ui.get_label_fixed_strings().text().split(" - ")[0]
            equipment_name = open_wires_view_window_ui.get_label_fixed_strings().text().split(" - ")[1]
            wire_name = open_wires_view_window_ui.get_label_right_part().text().split("/")[0]
            cross_section = open_wires_view_window_ui.get_label_right_part().text().split("/")[1]
            color = open_wires_view_window_ui.get_label_middle_part().text()
            from_pins_info = open_wires_view_window_ui.get_label_left_part().toolTip().split("->")[0]
            from_pins = from_pins_info.split("[")[0]
            pos_1 = from_pins.split(".")[0]
            cav_1 = from_pins.split(".")[1]
            from_pins_comment = from_pins_info.split("[")[1].replace("]", "")
            to_pins_info = open_wires_view_window_ui.get_label_left_part().toolTip().split("->")[1]
            to_pins = to_pins_info.split("[")[0]
            pos_2 = to_pins.split(".")[0]
            cav_2 = to_pins.split(".")[1]
            to_pins_comment = to_pins_info.split("[")[1].replace("]", "")
            defect_code = open_wires_view_window_ui.get_combobox_fed_by_excel_sheet().currentText()

            # Now, let's prepare the line to write
            line_to_write = LineToWriteDTO()
            line_to_write.set_uut(open_wires_view_window_ui.get_label_uut().text())
            line_to_write.set_fixed_string_part_1(fixed_string_part_1)
            line_to_write.set_equipment_name(equipment_name)
            line_to_write.set_date(get_current_date("%d.%m.%Y"))
            line_to_write.set_time(get_current_time("%I:%M:%S %p"))
            line_to_write.set_wire_name(wire_name)
            line_to_write.set_cross_section(cross_section)
            line_to_write.set_color(color)
            line_to_write.set_position_1(pos_1)
            line_to_write.set_cavity_1(cav_1)
            line_to_write.set_position_2(pos_2)
            line_to_write.set_cavity_2(cav_2)
            line_to_write.set_w(defect_code)
            line_to_write.set_comments(open_wires_view_window_ui.get_text_comments().toPlainText())

            # Actual writing
            self.get_crud_file_as().write_modified_line(
                get_application_property("folder_modified_lines_path")
                , line_to_write
            )

            # Now, it's time to :
            # 1- Load another line (If there is still any)
            # OR
            # 2 - Pass to the the Next Step: SHORTS
            if len(self.get_list_lines_open_wires()) > 0:
                # There is still any...
                self.get_open_wires_view().update_content(self.get_list_lines_open_wires().pop())
            else:
                # No more line, let's pass to the Next Step: SHORTS
                self.get_current_view().get_window_ui().get_main_window().close()
                self.set_current_view(self.get_shorts_view())
                self.get_current_view().get_window_ui().get_main_window().showMaximized()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def write_shorts_information(self):
        try:
            """
            After clicking the Extra Wires - Shorts Confirm button, we write the selected information in
            a new Excel File.
            
            :return: None
            """
            # Getting the Shorts window of the view
            shorts_view_window_ui = self.get_shorts_view().get_window_ui()

            # Preparing the data that still needs pre-processing
            fixed_string_part_1 = shorts_view_window_ui.get_label_fixed_strings().text().split(" - ")[0]
            equipment_name = shorts_view_window_ui.get_label_fixed_strings().text().split(" - ")[1]
            from_pins_info = shorts_view_window_ui.get_label_left_part().toolTip().split("->")[0]
            from_pins = from_pins_info.split("[")[0]
            pos_1 = from_pins.split(".")[0]
            cav_1 = from_pins.split(".")[1]
            from_pins_comment = from_pins_info.split("[")[1].replace("]", "")
            to_pins_info = shorts_view_window_ui.get_label_left_part().toolTip().split("->")[1]
            to_pins = to_pins_info.split("[")[0]
            pos_2 = to_pins.split(".")[0]
            cav_2 = to_pins.split(".")[1]
            to_pins_comment = to_pins_info.split("[")[1].replace("]", "")
            defect_code = shorts_view_window_ui.get_combobox_fed_by_excel_sheet().currentText()

            # Now, let's prepare the line to write
            line_to_write = LineToWriteDTO()
            line_to_write.set_uut(shorts_view_window_ui.get_label_uut().text())
            line_to_write.set_fixed_string_part_1(fixed_string_part_1)
            line_to_write.set_equipment_name(equipment_name)
            line_to_write.set_date(get_current_date("%d.%m.%Y"))
            line_to_write.set_time(get_current_time("%I:%M:%S %p"))
            line_to_write.set_wire_name(None)
            line_to_write.set_cross_section(None)
            line_to_write.set_color(None)
            line_to_write.set_position_1(pos_1)
            line_to_write.set_cavity_1(cav_1)
            line_to_write.set_position_2(pos_2)
            line_to_write.set_cavity_2(cav_2)
            line_to_write.set_w(defect_code)
            line_to_write.set_comments(shorts_view_window_ui.get_text_comments().toPlainText())

            # Actual writing
            self.get_crud_file_as().write_modified_line(
                get_application_property("folder_modified_lines_path")
                , line_to_write
            )

            # Now, it's time to :
            # 1- Load another line (If there is still any)
            # OR
            # 2 - Pass to the the Next Step: SHORTS
            if len(self.get_list_lines_shorts()) > 0:
                self.get_shorts_view().update_content(self.get_list_lines_shorts().pop())
            else:
                self.get_current_view().get_window_ui().get_main_window().close()
                self.set_current_view(self.get_additional_information_view())
                self.get_current_view().get_window_ui().get_main_window().showMaximized()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def write_additional_information(self):
        try:
            """
            After clicking the Additional Information Window's Confirm button, we write the selected information in
            a new Excel File.

            :return: None
            """
            # Getting the Shorts window of the view
            additional_information_view_window_ui = self.get_additional_information_view().get_window_ui()

            # Preparing the data that still needs pre-processing
            fixed_string_part_1 = additional_information_view_window_ui.get_label_fixed_strings().text().split(" - ")[0]
            equipment_name = additional_information_view_window_ui.get_label_fixed_strings().text().split(" - ")[1]
            defect_code = additional_information_view_window_ui.get_combobox_fed_by_excel_sheet().currentText()

            # Now, let's prepare the line to write
            line_to_write = LineToWriteDTO()
            line_to_write.set_uut(additional_information_view_window_ui.get_label_uut().text())
            line_to_write.set_fixed_string_part_1(fixed_string_part_1)
            line_to_write.set_equipment_name(equipment_name)
            line_to_write.set_date(get_current_date("%d.%m.%Y"))
            line_to_write.set_time(get_current_time("%I:%M:%S %p"))
            line_to_write.set_wire_name(None)
            line_to_write.set_cross_section(None)
            line_to_write.set_color(None)
            line_to_write.set_position_1(None)
            line_to_write.set_cavity_1(None)
            line_to_write.set_position_2(None)
            line_to_write.set_cavity_2(None)
            line_to_write.set_w(defect_code)
            line_to_write.set_comments(additional_information_view_window_ui.get_text_comments().toPlainText())

            # Actual writing
            self.get_crud_file_as().write_modified_line(
                get_application_property("folder_modified_lines_path")
                , line_to_write
            )
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def write_additional_information_after_done(self):
        """
        After clicking the Additional Information Window's Done button, we write the selected information in
        a new Excel File and leave the Window (redirection to the Loading Window).

        :return: None
        """
        try:
            # First, just write
            self.write_additional_information()

            # Then, we have to remove the recently treated file
            os.remove(self.get_file_to_delete_path())

            # And finally, we are going to request the Treatment of a next HTML file
            self.get_current_view().get_window_ui().get_main_window().close()
            self.set_current_view(self.get_loading_window_view())
            self.get_current_view().get_window_ui().get_main_window().showMaximized()
            self.check_current_window()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def check_current_window(self):
        """
        Checking if the Current File lines property is Empty|Not Empty.
        If (Empty), then, it is time to load another one.
        :return: None
        """
        if self.get_current_view() == self.get_loading_window_view():
            # We have to load an HTML file
            self.load_html_file()

    def load_html_file(self):
        # The html file to be loaded is the the First one in the File queue
        file_queue = self.get_file_queue()
        if len(file_queue) > 0:
            # Loading a new HTML file is only possible when the File Queue still contains File
            html_file = file_queue.pop(0)
            file_retrieved = self.get_crud_file_as().read_test_report_file(html_file)
            self.set_current_file(file_to_read_dto_to_file_to_read(file_retrieved))
            self.set_file_to_delete_path(html_file)
            LOGGER.info("Test report HTML file loaded : " + str(self.get_current_file()))

            # (Re-)Initializing all the lists of lines, acknowledging that each of them corresponds to a specific type
            # of lines
            self.set_list_lines_cross_pinning([])
            self.set_list_lines_open_wires([])
            self.set_list_lines_shorts([])
            QApplication.processEvents()

            # Retrieving all the general information about the file that is read and display them on the Windows
            fixed_string_part_1 = get_application_property("specific_fixed_string_part_1")
            equipment_name = get_application_property("equipment_name")
            uut = self.get_current_file().get_uut()
            QApplication.processEvents()

            # Retrieving all the lines from the current HTML file and then dispatch them to the adequate list
            for line in self.get_current_file().get_lines_to_read():
                if line.get_type() == LineTypesEnum.CROSS_PINNING:
                    # Case of a Cross Pinning-related Line
                    self.get_list_lines_cross_pinning().append(line)
                elif line.get_type() == LineTypesEnum.OPEN_WIRES:
                    # Case of a Open Wires-related Line
                    self.get_list_lines_open_wires().append(line)
                elif line.get_type() == LineTypesEnum.EXTRA_WIRES_SHORTS:
                    # Case of a Extra Wires - Shorts-related Line
                    self.get_list_lines_shorts().append(line)
                else:
                    # Unknown type of line
                    msg_error = "An unknown type of line was detected while treating : " + "\"" + str(line) + "\""
                    LOGGER.error(msg_error)
                    raise TypeError(msg_error)

            """
            (Re-)Initializing the Views by feeding them with the first line of the adequate Lines list
            """
            # CROSS PINNING
            self.get_cross_pinning_view().get_window_ui().get_label_fixed_strings().setText(
                fixed_string_part_1 + " - " + equipment_name
            )
            self.get_cross_pinning_view().get_window_ui().get_label_uut().setText(uut)
            if self.get_list_lines_cross_pinning():
                self.get_cross_pinning_view().update_content(self.get_list_lines_cross_pinning().pop())
            self.get_cross_pinning_view().get_window_ui().get_main_window().showMaximized()
            # OPEN WIRES
            self.get_open_wires_view().get_window_ui().get_label_fixed_strings().setText(
                fixed_string_part_1 + " - " + equipment_name
            )
            self.get_open_wires_view().get_window_ui().get_label_uut().setText(uut)
            if self.get_list_lines_open_wires():
                self.get_open_wires_view().update_content(self.get_list_lines_open_wires().pop())
            # SHORTS
            self.get_shorts_view().get_window_ui().get_label_fixed_strings().setText(
                fixed_string_part_1 + " - " + equipment_name
            )
            self.get_shorts_view().get_window_ui().get_label_uut().setText(uut)
            if self.get_list_lines_shorts():
                self.get_shorts_view().update_content(self.get_list_lines_shorts().pop())
            # ADDITIONAL INFORMATION
            self.get_additional_information_view().get_window_ui().get_label_uut().setText(uut)
            self.get_additional_information_view().get_window_ui().get_label_fixed_strings().setText(
                fixed_string_part_1 + " - " + equipment_name
            )
            QApplication.processEvents()

            # And, The Cross Pinning window is the first of the Treatment Windows to be displayed
            # and the others will follow once the treatments on this Window will be achieved
            if self.get_current_view().get_window_ui().get_main_window().isVisible():
                self.get_current_view().get_window_ui().get_main_window().close()
            self.set_current_view(self.get_cross_pinning_view())
            self.get_current_view().get_window_ui().get_main_window().showMaximized()
        else:
            # We have to load all the HTML files present within dedicated folder to our File Queue
            file_path = get_application_property("test_report_folder_path")

            if not os.listdir(file_path):
                # If no file is available within the HTML folder, we have to wait...
                # ...so, let's display the Loading Window.
                self.get_current_view().get_window_ui().get_main_window().showMaximized()
                while not os.listdir(file_path):
                    # In order to keep the Loading Window open
                    QApplication.processEvents()
                # Once the files are there:
                # 1 - Let's wait for about 5 s in to make sure that the recently added file(s) are(is) ready
                time.sleep(5)
            # 2 -... and load all those files within our File Queue
            for file_name in os.listdir(file_path):
                self.get_file_queue().append(file_path + "\\" + file_name)
            # 3 - Now, let's launch a new Load of HTML file, but this time, with the File(s)
            self.load_html_file()

