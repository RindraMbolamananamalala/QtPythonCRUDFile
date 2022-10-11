# -*- coding: utf-8 -*-

"""
crud_file_as_intf.py: The python file dedicated to the Abstract Base Class of the CRUD file Application
Service part dedicated to any need of CRUD service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from abc import ABC, abstractmethod

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.MODEL.DTO.line_to_write_dto import LineToWriteDTO
from BUSINESS.MODEL.DTO.file_f_dto import FileFDTO
from BUSINESS.MODEL.DTO.file_w_dto import FileWDTO


class CRUDFileASIntf(ABC):
    @abstractmethod
    def get_file_f(self, file_path: str) -> FileFDTO:
        """

        :param file_path: The path where the excel File F is located
        :return: The structured File F
        """
        return

    @abstractmethod
    def get_file_w(self, file_path: str) -> FileWDTO:
        """

        :param file_path: The path where the excel File W is located
        :return: The structured File W
        """
        return

    @abstractmethod
    def get_defect_codes(self, file_path: str) -> list:
        """
        Returns in the format of a list the lines that correspond respectively to the Defect Codes in
        function of the type of Treatment.
            L[0] : Cross Pinning
            L[1] : Open wires
            L[2] : Extra Wires - Shorts
            L[3] : Additional Information

            :param file_path: The path of the Excel File in which the Defect Codes will be retrieved
            :return The list of the various Defect Codes' Lines.
        """
        return


    @abstractmethod
    def read_test_report_file(self, test_report_file_path: str) -> FileToReadDTO:
        """

        :param test_report_file_path: The file path of the Test Report excel file to be read.
        :return: The structured content of the Test Report excel file represented by its file path.
        """
        return

    @abstractmethod
    def write_modified_line(self, test_modified_report_file_path: str, line_to_write: LineToWriteDTO):
        """

        :param test_modified_report_file_path: The file path of the modified Test Report excel file
        where the modified line will be added.
        :param line_to_write: The modified line to be added.
        :return: None
        """
        return
