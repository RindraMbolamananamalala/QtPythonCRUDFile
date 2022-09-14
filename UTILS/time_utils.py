# -*- coding: utf-8 -*-

"""
time_utils.py: The python file dedicated to the implementation of any need of Time information anywhere in the
Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from datetime import date, datetime


def get_current_date(date_format: str):
    """

    :param date_format: The format in which the date is wanted to be written
    :return: the current date
    """
    current_date = date.today().strftime(date_format)
    return current_date


def get_current_time(time_format: str):
    """

    :param time_format: The format in which the time is wanted to be written
    :return: the current time
    """
    current_time = datetime.now().strftime(time_format)
    return current_time



