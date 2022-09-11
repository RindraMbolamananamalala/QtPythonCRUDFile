# -*- coding: utf-8 -*-

"""
line_to_read.py: The python file dedicated to the "Model:LineToRead" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.crud_file_do import CRUDFileDO


class LineToRead(CRUDFileDO):

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
