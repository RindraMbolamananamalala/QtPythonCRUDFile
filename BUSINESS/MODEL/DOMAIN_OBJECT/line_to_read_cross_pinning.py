# -*- coding: utf-8 -*-

"""
line_to_read_cross_pinning.py: The python file dedicated to the "Model:LineToReadCrossPinning" part of the MVC pattern
implemented within the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs.
This DO is a child class of the Model:LineToRead DO, but instead of just one object dedicated each of the 2 Pins ("From"
and "To"), it stores those information within a List Data Structure (because several information rlated to those Pins
are to be managed, and then stored).
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead


class LineToReadCrossPinning(LineToRead):

    def set_from_pins(self, from_pins: list):
        self.from_pins = from_pins

    def get_from_pins(self) -> list:
        return self.from_pins

    def set_from_pins_comment(self, from_pins_comment: list):
        self.from_pins_comment = from_pins_comment

    def get_from_pins_comment(self) -> list:
        return self.from_pins_comment

    def set_to_pins(self, to_pins: list):
        self.to_pins = to_pins

    def get_to_pins(self) -> list:
        return self.to_pins

    def set_to_pins_comment(self, to_pins_comment: list):
        self.to_pins_comment = to_pins_comment

    def get_to_pins_comment(self) -> list:
        return self.to_pins_comment

    def __init__(self):
        # First, let's initialize the Object according to the default behaviors and Data of its Superclass
        super(LineToReadCrossPinning, self).__init__()

        # Then, we initialize all the pins (this time managed by list data structures) with default values
        self.set_from_pins([])
        self.set_from_pins_comment([])
        self.set_to_pins([])
        self.set_to_pins_comment([])
