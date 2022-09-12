# -*- coding: utf-8 -*-

"""
line_to_read_dto.py: The python file dedicated to the "Model:DTO:LineToRead" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DTO.crud_file_dto import CRUDFileDTO


class LineToReadDTO(CRUDFileDTO):

    def set_item(self, item: int):
        self.item = item

    def get_item(self) -> int:
        return self.item

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_from_pins(self, from_pins: str):
        self.from_pins = from_pins

    def get_from_pins(self) -> str:
        return self.from_pins

    def set_to_pins(self, to_pins: str):
        self.to_pins = to_pins

    def get_to_pins(self) -> str:
        return self.to_pins

    def set_measurement(self, measurement: str):
        self.measurement = measurement

    def get_measurement(self) -> str:
        return self.measurement

    def set_type(self, type: str):
        self.type = type

    def get_type(self) -> str:
        return self.type

    def set_result(self, result: str):
        self.result = result

    def get_result(self) -> str:
        return self.result

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
        # All the properties initialized to a default value
        self.set_item(None)
        self.set_name(None)
        self.set_from_pins(None)
        self.set_to_pins(None)
        self.set_measurement(None)
        self.set_type(None)
        self.set_result(None)
        self.set_wire_name(None)
        self.set_cross_section(None)
        self.set_color(None)
        self.set_position_1(None)
        self.set_cavity_1(None)
        self.set_position_2(None)
        self.set_cavity_2(None)

