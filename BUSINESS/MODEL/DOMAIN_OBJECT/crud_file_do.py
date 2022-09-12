# -*- coding: utf-8 -*-

"""
crud_file.py: The python file dedicated to the super class of all the Project's Domain Objects (DOs)
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


class CRUDFileDO:

    def __str__(self) -> str:
        """

        :return:  a structure in which all DTO's attributes are presented besides their respective value(s)
        """
        return super.__str__(self) + " :" + str(vars(self))
