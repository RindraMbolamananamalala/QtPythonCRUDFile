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

    def set_wire_name(self, wire_name: str):
        self.wire_name = wire_name

    def get_wire_name(self) -> str:
        return self.wire_name

    def set_cross_section(self, cross_section: str):
        self.cross_section = cross_section

    def get_cross_section(self) -> str:
        return self.cross_section

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    def set_position_1(self, position_1: str):
        self.position_1 = position_1

    def get_position_1(self) -> str:
        return self.position_1

    def set_cavity_1(self, cavity_1: str):
        self.cavity_1 = cavity_1

    def get_cavity_1(self) -> str:
        return self.cavity_1

    def set_position_2(self, position_2: str):
        self.position_2 = position_2

    def get_position_2(self) -> str:
        return self.position_2

    def set_cavity_2(self, cavity_2: str):
        self.cavity_2 = cavity_2

    def get_cavity_2(self) -> str:
        return self.cavity_2

    def __init__(self):
        self.set_uut(None)
        self.set_station(None)
        self.set_operator(None)
        self.set_time(None)
        self.set_date(None)
        self.set_test_qty(None)
        self.set_failure_qty(None)
        self.set_lines_to_read([])
        self.set_wire_name(None)
        self.set_cross_section(None)
        self.set_color(None)
        self.set_position_1(None)
        self.set_cavity_1(None)
        self.set_position_2(None)
        self.set_cavity_2(None)

