# -*- coding: utf-8 -*-

"""
data_access_base.py: The python file dedicated to the preparations of the Base and Session for any need
of access (CRUD) to the dedicated MySQL Database.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from CONFIGURATIONS.application_properties import get_application_property

"""
Creating the engine corresponding to the DB
"""
db_user_name = get_application_property('db_user_name')
db_user_password = get_application_property('db_user_password')
db_host = get_application_property('db_host')
db_port = get_application_property('db_port')
db_name = get_application_property('db_name')
engine = create_engine('mysql://'
                       + db_user_name
                       + ':'
                       + db_user_password
                       + '@'
                       + db_host
                       + ':'
                       + db_port
                       + '/'
                       + db_name)

"""
Preparing a session from the engine previously created
"""
Session = sessionmaker(bind=engine)

Data_Access_Base = declarative_base()
