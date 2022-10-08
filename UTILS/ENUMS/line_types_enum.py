# -*- coding: utf-8 -*-

"""
line_types_enum.py: The python file dedicated to the ENUM class managing the different types of a line
that a Report line could have.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from enum import Enum


class LineTypesEnum(Enum):
    """

    The Enum dedicated to the type of line that a Report Line can have
    """
    CROSS_PINNING = 1
    OPEN_WIRES = 2
    EXTRA_WIRES_SHORTS = 3
