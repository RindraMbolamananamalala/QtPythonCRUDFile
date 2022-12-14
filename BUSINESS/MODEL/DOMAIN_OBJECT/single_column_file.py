# -*- coding: utf-8 -*-

"""
single_column_file.py: The python file dedicated to the "Model:SingleColumnFile" part of the MVC pattern implemented
within the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.crud_file_do import CRUDFileDO


class SingleColumnFile(CRUDFileDO):

    def set_lines(self, lines: list):
        self.lines = lines

    def get_lines(self) -> list:
        return self.lines

    def __init__(self):
        self.set_lines([])
