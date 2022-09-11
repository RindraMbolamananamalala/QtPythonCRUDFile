# -*- coding: utf-8 -*-

"""
logger.py: The python file dedicated to the configurations related to the python LOGGER to be used throughout
the Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


import coloredlogs
import logging

LOGGER = logging.getLogger(__name__)
coloredlogs.install(level='INFO'
                    , logger=LOGGER
                    , fmt='%(asctime)s,%(msecs)03d  '
                          '%(hostname)s %(levelname)s  %(process)d --- '
                          '[ %(processName)s] %(pathname)s : %(message)s')


