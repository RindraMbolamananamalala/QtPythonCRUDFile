# -*- coding: utf-8 -*-

"""
line_to_save.py: The python file dedicated to the "Model:Entity:LineToSave"  implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's Entity
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import Column, Integer, String, DateTime, DECIMAL

from CONFIGURATIONS.application_properties import get_application_property

from DATA_ACCESS.data_access_base import Data_Access_Base

from BUSINESS.MODEL.ENTITY.qt_python_crud_file_entity import QTPythonCRUDFileEntity


class LineToSave(Data_Access_Base, QTPythonCRUDFileEntity):
    __tablename__ = get_application_property("db_line_to_save_table_name")
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(String)
    zone = Column(String)
    equipment_name = Column(String)
    date_time = Column(DateTime)
    wire_name = Column(String)
    cross_section = Column(DECIMAL(10, 2))
    color = Column(String)
    pos_1 = Column(String)
    cav_1 = Column(String)
    pos_2 = Column(String)
    cav_2 = Column(String)
    defect_code = Column(String)
    comment = Column(String)

