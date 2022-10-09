# -*- coding: utf-8 -*-

"""
line_to_write_dto.py: The python file dedicated to the "Model:DTO:LineToWrite" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DTO.crud_file_dto import CRUDFileDTO


class LineToWriteDTO(CRUDFileDTO):

    def set_uut(self, uut: str):
        self.uut = uut

    def get_uut(self) -> str:
        return self.uut

    def set_f(self, f: str):
        self.f = f

    def get_f(self) -> str:
        return self.f

    def set_equipment_name(self, equipment_name: str):
        self.equipment_name = equipment_name

    def get_equipment_name(self) -> str:
        return self.equipment_name

    def set_fixed_string_part_1(self, fixed_string_part_1: str):
        self.fixed_string_part_1 = fixed_string_part_1

    def get_fixed_string_part_1(self) -> str:
        return self.fixed_string_part_1

    def set_date(self, date: str):
        self.date = date

    def get_date(self) -> str:
        return self.date

    def set_time(self, time: str):
        self.time = time

    def get_time(self) -> str:
        return self.time

    def set_wire_name(self, wire_name: str):
        self.wire_name = wire_name

    def get_wire_name(self) -> str:
        return self.wire_name

    def set_cross_section(self, cross_section: str):
        self.cross_section = cross_section

    def get_cross_section(self) -> str:
        return self.cross_section

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

    def set_w(self, w: str):
        self.w = w

    def get_w(self) -> str:
        return self.w

    def set_comments(self, comments: str):
        self.comments = comments

    def get_comments(self) -> str:
        return self.comments

    def __init__(self):
        # Initializing all properties with default values
        self.set_uut(None)
        self.set_f(None)
        self.set_equipment_name(None)
        self.set_date(None)
        self.set_time(None)
        self.set_wire_name(None)
        self.set_cross_section(None)
        self.set_color(None)
        self.set_position_1(None)
        self.set_cavity_1(None)
        self.set_position_2(None)
        self.set_cavity_2(None)
        self.set_w(None)
        self.set_comments(None)
