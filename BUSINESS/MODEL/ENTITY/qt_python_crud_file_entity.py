# -*- coding: utf-8 -*-

"""
qt_python_crud_file_entity.py: The python file dedicated to the super class of all the Project's Entities
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


class QTPythonCRUDFileEntity:

    def __str__(self) -> str:
        """

        :return:  a structure in which all Entity's attributes are presented besides their respective value(s)
        """
        return super.__str__(self) + " :" + str(vars(self))
