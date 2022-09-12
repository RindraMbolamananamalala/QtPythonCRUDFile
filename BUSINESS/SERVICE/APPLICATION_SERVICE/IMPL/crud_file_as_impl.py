# -*- coding: utf-8 -*-

"""
crud_file_as_impl.py: The python file dedicated to the Ipplementation Class of the CRUD file Application
Service part dedicated to any need of CRUD service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.crud_file_as_intf import CRUDFileASIntf

from DATA_ACCESS.DAO.INTF.crud_file_dao_intf import CRUDFileDAOIntf

from DATA_ACCESS.DAO.IMPL.crud_file_dao_impl import CRUDFileDAOImpl


class CRUDFileASImpl(CRUDFileASIntf):
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

    def __init__(self):
        # Initializing the DAO
        self.set_crud_file_dao(CRUDFileDAOImpl())
