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
        elif len(args) == 2:
            # Both the View part and the AS to be used by the Controller were provided
            # Preparing each part
            self.set_crud_file_view(args[0])

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

