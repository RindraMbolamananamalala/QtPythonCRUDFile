# -*- coding: utf-8 -*-

"""
crud_file_dao_impl.py: The python file dedicated to the Implementation Class of the Data Access Object (DAO)
for any need of CRUD to Data Base or Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

# We're using Python Pandas for the CRUD on Excel Files
import os.path

import pandas as pd

from openpyxl import load_workbook

from BUSINESS.MODEL.DTO.file_f_dto import FileFDTO
from BUSINESS.MODEL.DTO.file_w_dto import FileWDTO
from BUSINESS.MODEL.DTO.line_to_write_dto import LineToWriteDTO
from CONFIGURATIONS.logger import LOGGER
from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from DATA_ACCESS.DAO.INTF.crud_file_dao_intf import CRUDFileDAOIntf


class CRUDFileDAOImpl(CRUDFileDAOIntf):

    def get_file_f(self, file_path: str) -> FileFDTO:
        """

        :param file_path: The path where the excel File F is located
        :return: The structured File F
        """
        file_to_return = FileFDTO()
        file_retrieved = pd.read_excel(file_path, header=None)
        lines_to_return = []
        for i in range(0, file_retrieved.shape[0]):
            line_to_return = file_retrieved.loc[i][0]
            lines_to_return.append(line_to_return)
        file_to_return.set_lines(lines_to_return)
        return file_to_return

    def get_file_w(self, file_path: str) -> FileWDTO:
        """

        :param file_path: The path where the excel File W is located
        :return: The structured File W
        """
        file_to_return = FileWDTO()
        file_retrieved = pd.read_excel(file_path, header=None)
        lines_to_return = []
        for i in range(0, file_retrieved.shape[0]):
            line_to_return = file_retrieved.loc[i][0]
            lines_to_return.append(line_to_return)
        file_to_return.set_lines(lines_to_return)
        return file_to_return

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

            # Getting ONLY the Lines with a Result "Fail"
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

    def write_line(self, file_path: str, line_to_add: LineToWriteDTO):
        """

        :param file_path: the file Path of Excel file where the line_to_add will be written
        :param line_to_add: The Line to be written
        :return: None
        """
        # Preparing the line
        line_to_write = pd.DataFrame([
            line_to_add.get_uut()
            , line_to_add.get_fixed_string()
            , line_to_add.get_f()
            , line_to_add.get_date()
            , line_to_add.get_time()
            , line_to_add.get_wire_name()
            , line_to_add.get_cross_section()
            , line_to_add.get_color()
            , line_to_add.get_position_1()
            , line_to_add.get_cavity_1()
            , line_to_add.get_position_2()
            , line_to_add.get_cavity_2()
            , line_to_add.get_w()
            , line_to_add.get_comments()
        ])

        # The writing will happen in a the x-axis
        line_to_write = line_to_write.transpose()

        if os.path.isfile(file_path):
            # The File where we will write already exists
            wb = load_workbook(file_path)
            ws = wb["Sheet1"]
            list_line_to_write = line_to_write.values.tolist()
            for i in range(len(list_line_to_write)):
                ws.append(list_line_to_write[i])
            wb.save(file_path)
        else:
            # The File where where we will write doesn't exist yet, so we need to create it first
            writer = pd.ExcelWriter(file_path, mode="w", engine='xlsxwriter')
            line_to_write.to_excel(writer, index=False, header=["Order number", "Equipment name", "Production team"
                                                                , "Date", "Time", "Wire name", "Cross section"
                                                                , "Color", "Pos1", "Cav1"
                                                                , "Pos2", "Cav2", "Defect code"
                                                                , "Comment"])
            writer.save()