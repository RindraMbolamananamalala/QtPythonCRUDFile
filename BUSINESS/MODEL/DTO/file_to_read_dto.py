# -*- coding: utf-8 -*-

"""
file_to_read_dto.py: The python file dedicated to the "Model:DTO:FileToRead" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DTO.crud_file_dto import CRUDFileDTO


class FileToReadDTO(CRUDFileDTO):

    def set_uut(self, uut: str):
        self.uut = uut

    def get_uut(self) -> str:
        return self.uut

    def set_station(self, station: str):
        self.station = station

    def get_station(self) -> str:
        return self.station

    def set_operator(self, operator: str):
        self.operator = operator

    def get_operator(self) -> str:
        return self.operator

    def set_time(self, time: str):
        self.time = time

    def get_time(self) -> str:
        return self.time

    def set_date(self, date: str):
        self.date = date

    def get_date(self) -> str:
        return self.date

    def set_test_qty(self, test_qty: int):
        self.test_qty = test_qty

    def get_test_qty(self) -> int:
        return self.test_qty

    def set_failure_qty(self, failure_qty: int):
        self.failure_qty = failure_qty

    def get_failure_qty(self) -> int:
        return self.failure_qty

    def set_lines_to_read(self, lines_to_read: list):
        self.lines_to_read = lines_to_read

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

