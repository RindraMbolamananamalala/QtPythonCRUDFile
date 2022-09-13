# -*- coding: utf-8 -*-

"""
file_to_read_dto.py: The python file dedicated to the "Model:DTO:FileToRead" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import pandas as pd

from BUSINESS.MODEL.DTO.crud_file_dto import CRUDFileDTO


class FileToReadDTO(CRUDFileDTO):

    def set_uut(self, uut: str):
        if uut:
            self.uut = uut
        else:
            self.uut = None

    def get_uut(self) -> str:
        return self.uut

    def set_station(self, station: str):
        if not pd.isna(station):
            self.station = station
        else:
            self.station = None

    def get_station(self) -> str:
        return self.station

    def set_operator(self, operator: str):
        if not pd.isna(operator):
            self.operator = operator
        else:
            self.operator = None

    def get_operator(self) -> str:
        return self.operator

    def set_time(self, time: str):
        if not pd.isna(time):
            self.time = time
        else:
            self.time = None

    def get_time(self) -> str:
        return self.time

    def set_date(self, date: str):
        if not pd.isna(date):
            self.date = date
        else:
            self.date = None

    def get_date(self) -> str:
        return self.date

    def set_test_qty(self, test_qty: int):
        if not pd.isna(test_qty):
            self.test_qty = test_qty
        else:
            self.test_qty = None

    def get_test_qty(self) -> int:
        return self.test_qty

    def set_failure_qty(self, failure_qty: int):
        if not pd.isna(failure_qty):
            self.failure_qty = failure_qty
        else:
            self.failure_qty = None

    def get_failure_qty(self) -> int:
        return self.failure_qty

    def set_lines_to_read(self, lines_to_read: list):
        if lines_to_read:
            self.lines_to_read = lines_to_read
        else:
            self.lines_to_read = []

    def get_lines_to_read(self):
        return self.lines_to_read

    def __init__(self):
        self.set_uut(None)
        self.set_station(None)
        self.set_operator(None)
        self.set_time(None)
        self.set_date(None)
        self.set_test_qty(None)
        self.set_failure_qty(None)
        self.set_lines_to_read([])

