# -*- coding: utf-8 -*-

"""
crud_file_dao_impl.py: The python file dedicated to the Implementation Class of the Data Access Object (DAO)
for any need of CRUD to Data Base or Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

# We're using Python Pandas for the CRUD on Excel Files
import pandas as pd

from CONFIGURATIONS.logger import LOGGER
from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from DATA_ACCESS.DAO.INTF.crud_file_dao_intf import CRUDFileDAOIntf


class CRUDFileDAOImpl(CRUDFileDAOIntf):
    def read_file(self, file_path: str) -> FileToReadDTO:
        """

        :param file_path: the file Path of the Test Report Excel File
        :return: The structured content (FileToReadDTO) of the Test Report Excel File represented by its Path
        "file_path"
        """
        try:
            file_to_return = FileToReadDTO()
            file_retrieved = pd.read_excel(file_path)
            # Getting the File's UUT
            file_to_return.set_uut(file_retrieved.loc[2][6])
            # Getting the File's station
            file_to_return.set_station(file_retrieved.loc[2][0])
            # Getting the File's operator
            file_to_return.set_operator(file_retrieved.loc[2][1])
            # Getting the File's time
            file_to_return.set_time(file_retrieved.loc[2][2])
            # Getting the File's date
            file_to_return.set_date(file_retrieved.loc[2][3])
            # Getting the File's test qty
            file_to_return.set_test_qty(file_retrieved.loc[2][4])
            # Getting the File's failure qty
            file_to_return.set_failure_qty(file_retrieved.loc[2][5])

            # Getting the Lines with a Result "Fail"
            lines_to_return = []
            for i in range(4, file_retrieved.shape[0]):
                if file_retrieved.loc[i][6].upper() == "FAIL":
                    line_to_return = LineToRead()
                    # Getting line's item
                    line_to_return.set_item(file_retrieved.loc[i][0])
                    # Getting line's name
                    line_to_return.set_name(file_retrieved.loc[i][1])
                    # Getting line's from pins
                    line_to_return.set_from_pins(file_retrieved.loc[i][2])
                    # Getting line's to pins
                    line_to_return.set_to_pins(file_retrieved.loc[i][3])
                    # Getting line's to measurement
                    line_to_return.set_measurement(file_retrieved.loc[i][4])
                    # Getting line's to type
                    line_to_return.set_type(file_retrieved.loc[i][5])
                    # Getting line's to result
                    line_to_return.set_result(file_retrieved.loc[i][6])
                    lines_to_return.append(line_to_return)
            file_to_return.set_lines_to_read(lines_to_return)

            # The reading process was successfully achieved
            LOGGER.info("File retrieved: " + str(file_to_return))
            return file_to_return
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Reading Process. "
            )
            raise
