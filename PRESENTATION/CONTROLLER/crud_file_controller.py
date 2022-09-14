# -*- coding: utf-8 -*-

"""
crud_file_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import pathlib

from watchdog.observers import Observer

from CONFIGURATIONS.logger import LOGGER

from MAPPER.crud_file_mapper import file_to_read_dto_to_file_to_read

from PRESENTATION.VIEW.crud_file_view import CRUDFileView
from PRESENTATION.CONTROLLER.crud_file_event_handler import CRUDFileEventHandler

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

    def set_test_report_file_event_handler(self, test_report_file_event_handler: CRUDFileEventHandler):
        """

        :param test_report_file_event_handler: The File event Handler related to the test report files.
        :return: None
        """
        self.test_report_file_event_handler = test_report_file_event_handler

    def get_test_report_file_event_handler(self) -> CRUDFileEventHandler:
        """

        :return: The File event Handler related to the test report files.
        """
        return self.test_report_file_event_handler

    def set_crud_file_as(self, crud_file_as: CRUDFileASIntf):
        self.crud_file_as = crud_file_as

    def get_crud_file_as(self) -> CRUDFileASIntf:
        return self.crud_file_as

    def set_current_file(self, current_file: FileToRead):
        self.current_file = current_file

    def get_current_file(self) -> FileToRead:
        return self.current_file

    def __init__(self, *args):
        """

        :param crud_file_view: The View Part to be associated with the current Controller
        :param crud_file_as: The Application Service to be associated with the current Controller
        """
        if len(args) == 0:
            # No specific part to be used by the Controller was provided and have to be "manually" provided be the
            # Developer
            pass
        elif len(args) == 1:
            # The View part was provided

            # Preparing the View Part
            self.set_crud_file_view(args[0])

            # Initializing the Application Service
            self.set_crud_file_as(CRUDFileASImpl())

            # Preparing the Observer and the File Event Handler related to the Test Report folder.
            self.prepare_test_report_folder_observer()

            # If the File Event Handler's Queue already contains files path, let's initialize the Main Window with
            # the first file related to those paths
            file_handler_queue = self.get_test_report_file_event_handler().get_file_queue()
            if len(file_handler_queue) > 0:
                file_retrieved = self \
                    .get_crud_file_as().read_test_report_file(
                        file_handler_queue.pop(0)
                    )
                self.set_current_file(file_to_read_dto_to_file_to_read(file_retrieved))
                LOGGER.info("Test report file loaded : " + str(self.get_current_file()))
                # Before going further, let's first clean the Current File
                self.clean_current_file_lines()
                # Updating the main window with the Current File's contents
                self.get_crud_file_view().update_main_window(self.get_current_file())

            # Feeding the Combo Boxes of the Main Window
            self.feed_main_window_combo_boxes()

            # Managing the events
            self.manage_events()
        elif len(args) == 2:
            # Both the View part and the AS to be used by the Controller were provided
            # Preparing each part
            self.set_crud_file_view(args[0])
            self.set_crud_file_as(args[1])

            # Preparing the Observer and the File Event Handler related to the Test Report folder.
            self.prepare_test_report_folder_observer()
        else:
            # An invalid number of arguments was provided
            msg_error = "Invalid number of arguments given for the instantiation of a Controller"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception

    def prepare_test_report_folder_observer(self):
        """
        Preparing the Observer and the File Event Handler related to the Test Report folder.
        :return: None
        """
        # Initializing the File Event Handler
        self.set_test_report_file_event_handler(CRUDFileEventHandler())

        # Initializing the Folder Observer
        test_report_folder_observer = Observer()

        # Indicating the path of the Test Report Folder
        test_report_folder_path = "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\EXCEL_FILES"

        # At the start, by default, let's add any Excel file found under the Test Report Folder to the File Event
        # Handler's Queue
        test_report_directory = pathlib.Path(test_report_folder_path)
        excel_file_pattern = "*.xlsx"
        for excel_file in test_report_directory.glob(excel_file_pattern):
            self.get_test_report_file_event_handler().get_file_queue().append(excel_file)

        # Scheduling & Orchestration
        test_report_folder_observer.schedule(
            self.get_test_report_file_event_handler()
            , path=test_report_folder_path
            , recursive=False
        )

        # Starting the Folder Observer
        test_report_folder_observer.start()
        LOGGER.info("Test report folder observer has started")

    def manage_events(self):
        # When the "Confirm" button of the GUI Open Connections part is clicked, we write the selected
        # information in a new Excel File
        self.get_crud_file_view().get_main_window_ui().get_button_open_connections_confirm() \
            .clicked.connect(self.write_open_connections_information)

        # When the "Confirm" button of the GUI Shorts part is clicked, we write the selected
        # information in a new Excel File
        self.get_crud_file_view().get_main_window_ui().get_button_shorts_confirm() \
            .clicked.connect(self.write_shorts_information)

        # When the "Confirm" button of the GUI Additional Information Window is clicked, we write the selected
        # information in a new Excel File
        self.get_crud_file_view().get_main_window_ui().get_additional_information_window() \
            .get_button_additional_information_confirm().clicked.connect(self.write_additional_information)

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
            "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\RESOURCE_EXCEL_FILES\\F.XLSX")
        file_w = self.get_crud_file_as().get_file_w(
            "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\RESOURCE_EXCEL_FILES\\W.XLSX")

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
        line_to_write.set_date("current date")
        line_to_write.set_time("current time")
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
            "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\MODIFIED_EXCEL_FILES\\"
            + line_to_write.get_uut() + ".xlsx"
            , line_to_write)

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

    def write_shorts_information(self):
        """
        After clicking the Shorts Confirm button, we write the selected information in
        a new Excel File
        :return: None
        """
        # Getting the main window of the view
        view_window = self.get_crud_file_view().get_main_window_ui()
        line_to_write = LineToWriteDTO()
        line_to_write.set_uut(view_window.get_label_file_id().text())
        line_to_write.set_f(view_window.get_combo_box_F().currentText())
        line_to_write.set_fixed_string(view_window.get_label_for_the_specific_fixed_string().text())
        line_to_write.set_date("current date")
        line_to_write.set_time("current time")
        line_to_write.set_wire_name(None)
        line_to_write.set_cross_section(None)
        line_to_write.set_color(None)
        line_to_write.set_position_1(None)
        line_to_write.set_cavity_1(None)
        line_to_write.set_position_2(None)
        line_to_write.set_cavity_2(None)
        line_to_write.set_w(view_window.get_combo_box_shorts_W().currentText())
        line_to_write.set_comments(view_window.get_text_shorts_comments().toPlainText())

        # Actual writing
        self.get_crud_file_as().write_modified_line(
            "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\MODIFIED_EXCEL_FILES\\"
            + line_to_write.get_uut() + ".xlsx"
            , line_to_write)

        """
        Once the Writing process successfully achieved, we have to remove the modified line from the Current File's
        Line 
        """

        # First, let's identify which Line is the concerned one
        line_to_remove_item = view_window.get_list_shorts_name().currentItem().toolTip()
        line_to_remove = next((x for x in self.get_current_file().get_lines_to_read()
                               # Let's remind it that the item's tooltip corresponds to the Line's Item number
                               if str(x.get_item()) == line_to_remove_item)
                              , None)

        # After the identification, the actual removal process
        self.remove_confirmed_item(line_to_remove)

        """
        Once the Removal process successfully achieved, we need to check the state of the Controller's Current File 
        Lines.
        If there are no more lines (all of them have been modified), we load another file from the File Event Handler's
        Queue.
        """
        self.check_current_file_lines()

    def write_additional_information(self):
        """
        After clicking the Additional Information's Confirm button, we write the selected information in
        a new Excel File
        :return: None
        """
        # Getting the main window of the view
        view_window = self.get_crud_file_view().get_main_window_ui()

        # Getting the additional information window of the view
        additional_information_window = view_window.get_additional_information_window()

        line_to_write = LineToWriteDTO()
        line_to_write.set_uut(view_window.get_label_file_id().text())
        line_to_write.set_f(view_window.get_combo_box_F().currentText())
        line_to_write.set_fixed_string(view_window.get_label_for_the_specific_fixed_string().text())
        line_to_write.set_date("current date")
        line_to_write.set_time("current time")
        line_to_write.set_wire_name(None)
        line_to_write.set_cross_section(None)
        line_to_write.set_color(None)
        line_to_write.set_position_1(None)
        line_to_write.set_cavity_1(None)
        line_to_write.set_position_2(None)
        line_to_write.set_cavity_2(None)
        line_to_write.set_w(additional_information_window.get_combo_box_additional_information_w().currentText())
        line_to_write.set_comments(additional_information_window.get_text_additional_information_comments()
                                   .toPlainText())

        # Actual writing
        self.get_crud_file_as().write_modified_line(
            "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\MODIFIED_EXCEL_FILES\\"
            + line_to_write.get_uut() + ".xlsx"
            , line_to_write)

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
        file_handler_queue = self.get_test_report_file_event_handler().get_file_queue()

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
