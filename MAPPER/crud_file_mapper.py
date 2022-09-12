# -*- coding: utf-8 -*-

"""
crud_file_mapper.py: The python file dedicated to the implementation of any need of Objects Mappings
throughout the entire Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from mapper.object_mapper import ObjectMapper

from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO

# The Mapper Object to use throughout the whole implementation
mapper = ObjectMapper()

"""
Creating Mappings for:
"""
# FileToRead to FileToReadDTO
mapper.create_map(FileToRead, FileToReadDTO, {'lines_to_read': lambda file_to_read: file_to_read.lines_to_read})


def file_to_read_to_file_to_read_dto(file_to_read: FileToRead) -> FileToReadDTO:
    """

    :param file_to_read: The FileToRead Object from which all the values of the concerned properties (every properties
    here) of the FileToRead DTO will be retrieved.
    :return: An FileToRead DTO build from the properties of the given Image Object
    """
    file_to_read_dto_to_return = mapper.map(file_to_read, FileToReadDTO)
    return file_to_read_dto_to_return
