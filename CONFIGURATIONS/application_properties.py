# -*- coding: utf-8 -*-

"""
application_properties.py: The python file dedicated to the particular process of retrieving
the current Profile & current Profile's properties of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os
import configparser

application_ini_file_path = os.getcwd().split("QTPythonCRUDFile")[0] \
                                     + "QTPythonCRUDFile" \
                                     + "\\application.ini"

config = configparser.RawConfigParser()
config.read(application_ini_file_path)
# retrieving the chosen Profile
profile = config["PROFILE"]["value"]


def get_application_property(property_key) -> str:
    """
    Getting an application's property from the latter's "property_key".

    :param property_key: The property key of the wanted property
    :return: The value of the wanted property
    """
    return config[profile][property_key]



