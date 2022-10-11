# -*- coding: utf-8 -*-

"""
crud_file_as_impl.py: The python file dedicated to the Ipplementation Class of the CRUD file Application
Service part dedicated to any need of CRUD service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DTO.file_f_dto import FileFDTO
from BUSINESS.MODEL.DTO.file_w_dto import FileWDTO
from BUSINESS.MODEL.DTO.line_to_write_dto import LineToWriteDTO
from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.crud_file_as_intf import CRUDFileASIntf

from DATA_ACCESS.DAO.INTF.crud_file_dao_intf import CRUDFileDAOIntf
from DATA_ACCESS.DAO.IMPL.crud_html_file_dao_impl import CRUDHTMLFileDAOImpl
from DATA_ACCESS.DAO.IMPL.crud_file_dao_impl import CRUDFileDAOImpl


class CRUDFileASImpl(CRUDFileASIntf):

    def get_file_f(self, file_path: str) -> FileFDTO:
        """

        :param file_path: The path where the excel File F is located
        :return: The structured File F
        """
        file_retrieved = self.get_crud_file_dao().get_file_f(file_path)
        return file_retrieved

    def get_file_w(self, file_path: str) -> FileWDTO:
        """

        :param file_path: The path where the excel File W is located
        :return: The structured File W
        """
        file_retrieved = self.get_crud_file_dao().get_file_w(file_path)
        return file_retrieved

    def set_crud_file_dao(self, crud_file_dao: CRUDFileDAOIntf):
        """

        :param crud_file_dao: The CRUDFileDAO to be used by the Application Service.
        :return: None
        """
        self.crud_filed_dao = crud_file_dao

    def get_crud_file_dao(self) -> CRUDFileDAOIntf:
        """

        :return: The CRUDFileDAO used by the Application Service.
        """
        return self.crud_filed_dao

    def set_crud_excel_file_dao(self, crud_excel_file_dao: CRUDFileDAOIntf):
        """

        :param crud_excel_file_dao: The CRUD file DAO dedicated to Excel Files only to be used by the current AS
        :return: None
        """
        self.crud_excel_file_dao = crud_excel_file_dao

    def get_crud_excel_file_dao(self) -> CRUDFileDAOIntf:
        """

        :return: The CRUD file DAO dedicated to Excel Files only used by the current AS
        """
        return self.crud_excel_file_dao

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
        try:
            codes_retrieved = self.get_crud_excel_file_dao().get_defect_codes(file_path)
            return codes_retrieved
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Retrieval of Defect Codes Process. "
            )
            raise



    def read_test_report_file(self, test_report_file_path: str) -> FileToReadDTO:
        """

        :param test_report_file_path: The file path of the Test Report excel file to be read.
        :return: The structured content of the Test Report excel file represented by its file path.
        """
        try:
            test_report_file = self.get_crud_file_dao().read_file(test_report_file_path)
            # The reading process related to the report file was successfully achieved
            LOGGER.info("File retrieved: " + str(test_report_file))
            return test_report_file
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Reading Process. "
            )
            raise

    def write_modified_line(self, test_modified_report_file_path: str, line_to_write: LineToWriteDTO):
        """

        :param test_modified_report_file_path: The file path of the modified Test Report excel file
        where the modified line will be added.
        :param line_to_write: The modified line to be added.
        :return: None
        """
        self.get_crud_file_dao().write_line(test_modified_report_file_path, line_to_write)

    def __init__(self):
        # Initializing the DAOs
        self.set_crud_file_dao(CRUDHTMLFileDAOImpl())
        self.set_crud_excel_file_dao(CRUDFileDAOImpl())
