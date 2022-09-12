# -*- coding: utf-8 -*-

"""
crud_file_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access Object (DAO)
for any need of CRUD to Data Base or Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from abc import ABC, abstractmethod

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO


class CRUDFileDAOIntf(ABC):
    @abstractmethod
    def read_file(self, file_path: str) -> FileToReadDTO:
        """

        :param file_path: the file Path of the Test Report Excel File
        :return: The structured content (FileToReadDTO) of the Test Report Excel File represented by its Path
        "file_path"
        """
        return
