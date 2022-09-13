# -*- coding: utf-8 -*-

"""
crud_file_mapper.py: The python file dedicated to the implementation of any need of Objects Mappings
throughout the entire Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from mapper.object_mapper import ObjectMapper

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.MODEL.DTO.line_to_read_dto import LineToReadDTO

# The Mapper Object to use throughout the whole implementation
mapper = ObjectMapper()

"""
Creating Mappings for:
"""
# FileToRead to FileToReadDTO
mapper.create_map(FileToRead
                  , FileToReadDTO
                  # Mapping the LinesToRead property
                  , {'lines_to_read': lambda file_to_read: file_to_read.lines_to_read}
                  )

# FileToReadDTO to FileToRead
mapper.create_map(FileToReadDTO
                  , FileToRead
                  # Mapping the LinesToRead property
                  , {'lines_to_read': lambda file_to_read_dto: file_to_read_dto.lines_to_read}
                  )


def file_to_read_to_file_to_read_dto(file_to_read: FileToRead) -> FileToReadDTO:
    """

    :param file_to_read: The FileToRead Object from which all the values of the concerned properties (every properties
    here) of the FileToRead DTO will be retrieved.
    :return: A FileToRead DTO build from the properties of the given FileToRead Object
    """
    file_to_read_dto_to_return = mapper.map(file_to_read, FileToReadDTO)
    return file_to_read_dto_to_return


def file_to_read_dto_to_file_to_read(file_to_read_dto: FileToReadDTO) -> FileToRead:
    """

    :param file_to_read_dto: The FileToRead DTO from which all the values of the concerned properties (every properties
    here) of the FileToRead Object will be retrieved.
    :return: A FileToRead Object build from the properties of the given FileToRead DTO
    """
    file_to_read_to_return = mapper.map(file_to_read_dto, FileToRead)
    return file_to_read_to_return


def line_to_read_to_line_to_read_dto(line_to_read: LineToRead) -> LineToReadDTO:
    """

    :param line_to_read: The LineToRead Object from which all the values of the concerned properties (every properties
    here) of the LineToRead DTO will be retrieved.
    :return: A LineToRead DTO build from the properties of the given LineToRead Object
    """
    try:
        line_to_read_dto_to_return = mapper.map(line_to_read, LineToReadDTO)
        return line_to_read_dto_to_return
    except Exception as exception:
        # At least one error has occurred, therefore, stop the Mapping couldn't go further
        LOGGER.error(
            exception.__class__.__name__ + ": " + str(exception)
            + ". Can't go further with the Mapping. "
        )
        return None


