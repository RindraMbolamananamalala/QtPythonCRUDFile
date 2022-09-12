# -*- coding: utf-8 -*-

"""
single_column_line_dto.py: The python file dedicated to the "Model:DTO:SingleColumnLine" part of the MVC pattern
implemented within the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DTO.crud_file_dto import CRUDFileDTO


class SingleColumnLineDTO(CRUDFileDTO):

    def set_content(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content

    def __init__(self, *args):
        if len(args) == 0:
            # No argument was given, therefore, all the properties set to None at the start
            self.set_content(None)
        elif len(args) == 1:
            # The content was provided
            self.set_content(args[0])
        else:
            # Invalid numbers of arguments
            msg_error = "Invalid numbers of arguments given for the instantiation of a SingleColumnLineDTO"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception
