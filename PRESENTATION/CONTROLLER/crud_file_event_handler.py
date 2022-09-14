# -*- coding: utf-8 -*-

"""
crud_file_event_handler.py: The python file dedicated to the "File Event Handler" to be used by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import pathlib
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from PRESENTATION.CONTROLLER.crud_file_controller import CRUDFileController


class CRUDFileEventHandler(FileSystemEventHandler):

    def set_crud_file_controller(self, crud_file_controller: CRUDFileController):
        self.crud_file_controller = crud_file_controller

    def get_crud_file_controller(self) -> CRUDFileController:
        return self.crud_file_controller

    def on_created(self, event):
        """
        Storing the path of a newly created file inside the Queue of Files of the Controller.
        :param event: The event related to the creation of a new File
        :return: None
        """
        LOGGER.info(event.src_path + " created and added to the queue of file")
        self.get_crud_file_controller().get_file_queue().append(event.src_path)

        # Let's wait 5 seconds after the add of the new file before trying to treat it
        time.sleep(5)
        # Check if the Application is already ready to treat the new file
        self.get_crud_file_controller().check_current_file_lines()

    def prepare_test_report_folder_observer(self):
        """
        Preparing the Observer and the File Event Handler related to the Test Report folder.
        :return: None
        """

        # Initializing the Folder Observer
        test_report_folder_observer = Observer()

        # Indicating the path of the Test Report Folder
        test_report_folder_path = get_application_property("test_report_folder_path")

        # At the start, by default, let's add any Excel file found under the Test Report Folder to the File Event
        # Handler's Queue
        test_report_directory = pathlib.Path(test_report_folder_path)
        excel_file_pattern = "*.xlsx"
        for excel_file in test_report_directory.glob(excel_file_pattern):
            self.get_crud_file_controller().get_file_queue().append(excel_file)

        # Scheduling & Orchestration
        test_report_folder_observer.schedule(
            self
            , path=test_report_folder_path
            , recursive=False
        )

        # Starting the Folder Observer
        test_report_folder_observer.start()
        LOGGER.info("Test report folder observer has started")

    def __init__(self, crud_file_controller: CRUDFileController):
        """

        :param crud_file_controller: The controller to be associated with the File Event Handler
        """
        self.set_crud_file_controller(crud_file_controller)

        # Preparing the Observer related to the Test Report folder.
        self.prepare_test_report_folder_observer()

        self.get_crud_file_controller().load_another_file()
