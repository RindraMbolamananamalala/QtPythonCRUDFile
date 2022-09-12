# -*- coding: utf-8 -*-

"""
crud_file_event_handler.py: The python file dedicated to the "File Event Handler" to be used by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from watchdog.events import FileSystemEventHandler

from CONFIGURATIONS.logger import LOGGER


class CRUDFileEventHandler(FileSystemEventHandler):

    def set_file_queue(self, file_queue: list):
        """

        :param file_queue: The Queue of Files which related events are handled by the current handler
        :return: None
        """
        self.file_queue = file_queue

    def get_file_queue(self) -> list:
        """

        :return: The Queue of Files which related events are handled by the current handler
        """
        return self.file_queue

    def on_created(self, event):
        """
        Storing the path of a newly created file inside the Queue of Files of the Handler.
        :param event: The event related to the creation of a new File
        :return: None
        """
        LOGGER.info(event.src_path + " created and added to the queue of file");
        self.get_file_queue().append(event.src_path)

    def __init__(self):
        # Initializing the Queue of Files
        self.set_file_queue([])
