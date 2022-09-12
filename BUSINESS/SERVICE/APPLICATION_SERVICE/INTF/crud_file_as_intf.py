# -*- coding: utf-8 -*-

"""
crud_file_as_intf.py: The python file dedicated to the Abstract Base Class of the CRUD file Application
Service part dedicated to any need of CRUD service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from abc import ABC, abstractmethod

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO


class CRUDFileASIntf(ABC):
    @abstractmethod
    def read_test_report_file(self, test_report_file_path: str) -> FileToReadDTO:
        """

        :param test_report_file_path: The file path of the Test Report excel file to be read.
        :return: The structured content of the Test Report excel file represented by its file path.
        """
        return
