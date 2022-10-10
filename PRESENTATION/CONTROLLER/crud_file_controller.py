# -*- coding: utf-8 -*-

"""
crud_file_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *


from CONFIGURATIONS.application_properties import get_application_property

from CONFIGURATIONS.logger import LOGGER

from UTILS.ENUMS.line_types_enum import LineTypesEnum
from UTILS.time_utils import get_current_time, get_current_date

from MAPPER.crud_file_mapper import file_to_read_dto_to_file_to_read

from PRESENTATION.HMI.ui_Cross_Pinning import UI_CrossPinning
from PRESENTATION.HMI.ui_Open_Wires import UI_OpenWires
from PRESENTATION.HMI.ui_Shorts import UI_Shorts
from PRESENTATION.HMI.ui_Additional_Information_Window import UI_AdditionalInformationWindow

from PRESENTATION.VIEW.crud_file_view import CRUDFileView
from PRESENTATION.VIEW.cross_pinning_view import CrossPinningView
from PRESENTATION.VIEW.open_wires_view import OpenWiresView
from PRESENTATION.VIEW.shorts_view import ShortsView
from PRESENTATION.VIEW.additional_information_view import AdditionalInformationView

from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead
from BUSINESS.MODEL.DTO.line_to_write_dto import LineToWriteDTO
from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.crud_file_as_intf import CRUDFileASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.crud_file_as_impl import CRUDFileASImpl


class CRUDFileController:

    def set_crud_file_view(self, crud_file_view: CRUDFileView):
        """

        :param crud_file_view: The View part to be associated with the Controller part within the MVC
        Implementation at the level of the Presentation Layer of the Project.
        :return: None
        """
        self.crud_file_view = crud_file_view

    def get_crud_file_view(self) -> CRUDFileView:
        """

        :return: The View part associated with the Controller part within the MVC Implementation at the level of
        the Presentation Layer of the Project.
        :return: None
        """
        return self.crud_file_view

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
        self.current_file = current_file

    def get_current_file(self) -> FileToRead:
        return self.current_file

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

            # Preparing the View Parts (TEMPORARY, the Loading Window View should be the first VIEW to be managed by
            # the Controller)

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

            # Initializing all the lists of lines, acknowledging that each of them corresponds to a specific type of
            # lines
            self.set_list_lines_cross_pinning([])
            self.set_list_lines_open_wires([])
            self.set_list_lines_shorts([])

            # Retrieving all the lines from the current MHTML file and then dispatch them to the adequate list
            # VERY TEMPORARY; will be managed with a dynamic way once it is possible
            current_mhtml_path = "E:\\Upwork\\MdToriqul\\Project\\Actual HTML files for the tests\\B0008721651_2022-09-20_22-48-40.html"
            for line in self.get_crud_file_as().read_test_report_file(current_mhtml_path).get_lines_to_read():
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

            # Initializing the Views  by feeding them with the first line of the adequate Lines list
            # TEMPORARY, should be called mor dynamically once it is possible
            # (The same process should be applied to the others View Part, with the adequate list of lines)
            if self.get_list_lines_cross_pinning():
                self.get_cross_pinning_view().update_content(self.get_list_lines_cross_pinning().pop())
            if self.get_list_lines_open_wires():
                self.get_open_wires_view().update_content(self.get_list_lines_open_wires().pop())
            if self.get_list_lines_shorts():
                self.get_shorts_view().update_content(self.get_list_lines_shorts().pop())


            # Initializing the File_Queue
            # self.set_file_queue([])

            # Feeding the Combo Boxes of the Main Window
            # self.feed_main_window_combo_boxes()

            # Managing the events
            self.manage_events()
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

    def feed_main_window_combo_boxes(self):
        """
        Feeding the combo boxes on the main windows, including that of the internal Add Additional information window,
        from their corresponding Excel File
        :return: None
        """
        # Getting the View's Main window
        main_window = self.get_crud_file_view().get_main_window_ui()

        # Getting the F's values
        file_f = self.get_crud_file_as().get_file_f(
            get_application_property("file_f_path"))
        # Getting the W's values
        file_w = self.get_crud_file_as().get_file_w(
            get_application_property("file_w_path"))

        # Feeding the combo boxes
        # F_combo_box
        for value in file_f.get_lines():
            main_window.get_combo_box_F().addItem(value)
        # W combo_boxes
        for value in file_w.get_lines():
            main_window.get_combo_box_open_connections_W().addItem(value)
            main_window.get_combo_box_shorts_W().addItem(value)
            main_window.get_additional_information_window().get_combo_box_additional_information_w().addItem(value)

    def write_open_connections_information(self):
        """
        After clicking the Open Connections Confirm button, we write the selected information in
        a new Excel File
        :return: None
        """
        # Getting the main window of the view
        view_window = self.get_crud_file_view().get_main_window_ui()

        # Preparing the line to write
        line_to_write = LineToWriteDTO()
        line_to_write.set_uut(view_window.get_label_file_id().text())
        line_to_write.set_f(view_window.get_combo_box_F().currentText())
        line_to_write.set_fixed_string(view_window.get_label_for_the_specific_fixed_string().text())
        line_to_write.set_date(get_current_date("%d.%m.%Y"))
        line_to_write.set_time(get_current_time("%I:%M:%S %p"))
        line_to_write.set_wire_name(view_window.get_text_wire_name().toPlainText())
        line_to_write.set_cross_section(view_window.get_text_cross_section().toPlainText())
        line_to_write.set_color(view_window.get_text_color().toPlainText())
        line_to_write.set_position_1(view_window.get_text_position_1().toPlainText())
        line_to_write.set_cavity_1(view_window.get_text_cavity_1().toPlainText())
        line_to_write.set_position_2(view_window.get_text_position_2().toPlainText())
        line_to_write.set_cavity_2(view_window.get_text_cavity_2().toPlainText())
        line_to_write.set_w(view_window.get_combo_box_open_connections_W().currentText())
        line_to_write.set_comments(view_window.get_text_open_connections_comments().toPlainText())

        # Actual writing
        self.get_crud_file_as().write_modified_line(
            get_application_property("folder_modified_lines_path")
            , line_to_write
        )

        """
        Once the Writing process successfully achieved, we have to remove the modified line from the Current File's
        Line 
        """

        # First, let's identify which Line is the concerned one
        line_to_remove_item = view_window.get_list_open_connections_name().currentItem().toolTip()
        line_to_remove = next((x for x in self.get_current_file().get_lines_to_read()
                               # Let's remind it that the item's tooltip corresponds to the Line's Item number
                               if str(x.get_item()) == line_to_remove_item)
                              , None)

        # After the identification, the actual removal process
        self.remove_confirmed_item(line_to_remove)
        LOGGER.info(
            "The following line has been successfully removed from the Current File's list: "
            + str(line_to_remove)
        )

        """
        Once the Removal process successfully achieved, we need to check the state of the Controller's Current File 
        Lines.
        If there are no more lines (all of them have been modified), we load another file from the File Event Handler's
        Queue.
        """
        self.check_current_file_lines()

    def write_open_wires_information(self):
        try:
            """
            After clicking the Open Wires window Confirm button, we write the selected information in
            a new Excel File.
            
            :return: None
            """
            # Getting the Open Wires window of the view
            open_wires_view_window_ui = self.get_open_wires_view().get_window_ui()

            # Preparing the data that still needs pre-processing
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

            # TEMPORARY COMMENTED, will be seriously reviewed once it is possible
            """
            Once the Writing process successfully achieved, we have to remove the modified line from the Current File's
            Line
            """

            # First, let's identify which Line is the concerned one
            # line_to_remove_item = view_window.get_list_open_connections_name().currentItem().toolTip()
            # line_to_remove = next((x for x in self.get_current_file().get_lines_to_read()
            #                        # Let's remind it that the item's tooltip corresponds to the Line's Item number
            #                        if str(x.get_item()) == line_to_remove_item)
            #                       , None)
            #
            # # After the identification, the actual removal process
            # self.remove_confirmed_item(line_to_remove)
            # LOGGER.info(
            #     "The following line has been successfully removed from the Current File's list: "
            #     + str(line_to_remove)
            # )

            """
            Once the Removal process successfully achieved, we need to check the state of the Controller's Current File
            Lines.
            If there are no more lines (all of them have been modified), we load another file from the File Event 
            Handler's Queue.
            """
            # self.check_current_file_lines()
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

            # And then, go back to the Loading Window
            # TEMPORARY, we'lle work on it SERIOUSLY once the Cross Pinning managed
            print("ADDITIONAL INFORMATION DONE")
        except Exception as exception:
            # At least one error has occurred, therefore, stop the writing process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def remove_confirmed_item(self, line_to_remove: LineToRead):
        """
        Removing the modified line from the Current File's Line
        :line_to_remove: The modified line to be removed
        :return: None
        """
        # Removal process
        self.get_current_file().get_lines_to_read().remove(line_to_remove)

        # Let's update the Main Window with the new state of the Current File
        self.get_crud_file_view().update_main_window(self.get_current_file())

    def check_current_file_lines(self):
        """
        Checking if the Current File lines property is Empty|Not Empty.
        If (Empty), then, it is time to load another one.
        :return: None
        """
        if len(self.get_current_file().get_lines_to_read()) < 1:
            # If the Current File's line are Empty, we load another one
            self.load_another_file()

    def load_another_file(self):
        """
        Loading another Test Report Excel file to be treated by the Application through the latter's specific GUI.
        :return: None
        """
        # The file to be loaded is the the First one in the File Handler's queue of file
        file_handler_queue = self.get_file_queue()

        if len(file_handler_queue) > 0:
            # Loading a new file is only possible when the File Handler's queue still contains File
            file_retrieved = self \
                .get_crud_file_as().read_test_report_file(
                file_handler_queue.pop(0)
            )

            self.set_current_file(file_to_read_dto_to_file_to_read(file_retrieved))

            # Before going further, let's first clean the Current File
            self.clean_current_file_lines()
            LOGGER.info("Test report file loaded : " + str(self.get_current_file()))
            # Updating the main window with the Current File's contents
            self.get_crud_file_view().update_main_window(self.get_current_file())
        else:
            # Just Clear the main window until a new file is added within the Folder
            self.get_crud_file_view().clear_main_window()

    def clean_current_file_lines(self):
        """
        Removing from the Current File the lines, even though with a Result set to "Fail",
        but with a Type that should be ignored by the Application.
        :return: None
        """
        line_to_be_removed = []
        for line in self.get_current_file().get_lines_to_read():
            if line.get_type().upper() not in ["TESTSWITCH", "TESTCONNECTION"
                , "TESTBUSCONNECTORGROUP", "TESTBUSCONNECTORGROUPOPEN"
                , "TESTBUSCONNECTORGROUPDETECTION", "ISOLATIONTEST"]:
                # Just list the lines that are supposed to be ignored
                line_to_be_removed.append(line)

        # Proceed to the actual removal process, based on the previous pre-filled list of lines
        for line in line_to_be_removed:
            self.get_current_file().get_lines_to_read().remove(line)
