# -*- coding: utf-8 -*-

"""
crud_file_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import time

from watchdog.observers import Observer

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.VIEW.crud_file_view import CRUDFileView
from PRESENTATION.CONTROLLER.crud_file_event_handler import CRUDFileEventHandler

from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead
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

            # TEMPORARY
            # file = FileToRead()
            # file.set_uut("B0008713583")
            #
            # line_1 = LineToRead()
            # line_1.set_name("8759/0.13`YE/VT")
            # line_1.set_type("TestConnection")
            # line_1.set_from_pins("A2/183*C1-B_V1.S")
            # line_1.set_to_pins("A26/17*13-B_V1.S2")
            # line_2 = LineToRead()
            # line_2.set_name("3211/0.35`RD/WH")
            # line_2.set_type("TestBusConnectorGroupDetection")
            # line_2.set_from_pins("A2/182*C2-B_V1.S")
            # line_2.set_to_pins("A26/17*13-B_V1.S3")
            # line_3 = LineToRead()
            # line_3.set_type("IsolationTest")
            # line_3.set_from_pins("A2/182*C2-B_V1.S")
            # line_3.set_to_pins("A26/17*13-B_V1.S3")
            #
            # file.get_lines_to_read().append(line_1)
            # file.get_lines_to_read().append(line_2)
            # file.get_lines_to_read().append(line_3)

            file_retrieved = self \
                .get_crud_file_as().read_test_report_file(
                "E:\\Upwork\\MdToriqul\\Project\\QTPythonCRUDFile\\EXCEL_FILES\\B0008706912_2022-09-08_09-02-43.xlsx"
            )

            self.get_crud_file_view().update_main_window(file_retrieved)
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

        # Scheduling & Orchestration
        test_report_folder_observer.schedule(
            self.get_test_report_file_event_handler()
            , path=test_report_folder_path
            , recursive=False
        )

        # Starting the Folder Observer
        test_report_folder_observer.start()
        LOGGER.info("Test report folder observer has started")
