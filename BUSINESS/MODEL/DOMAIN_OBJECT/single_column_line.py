from BUSINESS.MODEL.DOMAIN_OBJECT.crud_file_do import CRUDFileDO

"""
single_column_line.py: The python file dedicated to the "Model:SingleColumnLine" part of the MVC pattern implemented
within the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


class SingleColumnLine(CRUDFileDO):

    def set_content(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content

    def __init__(self, content: str):
        self.set_content(content)
