# -*- coding: utf-8 -*-

"""
crud_file_dto.py: The python file dedicated to the super class of all the Project's Data Transfer Objects (DTOs)
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


class CRUDFileDTO:

    def __str__(self) -> str:
        """

        :return:  a structure in which all DTO's attributes are presented besides their respective value(s)
        """
        return super.__str__(self) + " :" + str(vars(self))

    def __eq__(self, other):
        """

        :param other: The other object to be compared to the current one
        :return: True if the two objects are "equal", False otherwise
        """
        if isinstance(other, CRUDFileDTO):
            return vars(self) == vars(other)
        return False
