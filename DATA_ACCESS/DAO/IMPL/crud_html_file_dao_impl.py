# -*- coding: utf-8 -*-

"""
crud_html_file_dao_impl.py: The python file dedicated to the Implementation Class of the Data Access Object (DAO)
for any need of CRUD related to (M)HTML Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import re

# Throughout the entire class, we are using BeautifulSoup for any need of Scraping
from bs4 import BeautifulSoup

from CONFIGURATIONS.logger import LOGGER

from UTILS.ENUMS.line_types_enum import LineTypesEnum

from BUSINESS.MODEL.DTO.file_f_dto import FileFDTO
from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.MODEL.DTO.file_w_dto import FileWDTO
from BUSINESS.MODEL.DTO.line_to_write_dto import LineToWriteDTO
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read_cross_pinning import LineToReadCrossPinning
from DATA_ACCESS.DAO.INTF.crud_file_dao_intf import CRUDFileDAOIntf
from DATA_ACCESS.DAO.IMPL.crud_file_dao_impl import CRUDFileDAOImpl


class CRUDHTMLFileDAOImpl(CRUDFileDAOIntf):

    def set_crud_file_dao(self, crud_file_dao: CRUDFileDAOImpl) -> None:
        """

        :param crud_file_dao: The CRUD File DAO to be used by the Current DAO when the time of writing within an
        Excel File will come.
        :return: None
        """
        self.crud_file_dao = crud_file_dao

    def get_crud_file_dao(self) -> CRUDFileDAOImpl:
        """

        :return: The CRUD File DAO used by the Current DAO when the time of writing within an Excel File will come.
        """
        return self.crud_file_dao

    def __init__(self):
        # Initializing the CRUD File DAO to be used by the Current DAO when the time of writing within an Excel File
        # will come.
        self.set_crud_file_dao(CRUDFileDAOImpl())

    def get_file_f(self, file_path: str) -> FileFDTO:
        """
        (We're still going to use that of the DATA_ACCESS.DAO.INTF.crud_file_dao_impl.CRUDFileDAOImpl when this
        Function is needed), so, just "pass" here.

        :param file_path: The path where the excel File F is located
        :return: The structured File F
        """
        pass

    def get_file_w(self, file_path: str) -> FileWDTO:
        """
        (We're still going to use that of the DATA_ACCESS.DAO.INTF.crud_file_dao_impl.CRUDFileDAOImpl when this
        Function is needed), so, just "pass" here.

        :param file_path: The path where the excel File W is located
        :return: The structured File W
        """
        pass

    def read_file(self, file_path: str) -> FileToReadDTO:
        """

        :param file_path: the file Path of the Test Report HTML File
        :return: The structured content (FileToReadDTO) of the Test Report HTML File represented by its Path
        "file_path"
        """
        try:
            # Initializing the File to be returned later
            file_to_return = FileToReadDTO()

            # First of all, let's access to the HTML file
            with open(file_path) as file_to_read:
                soup = BeautifulSoup(file_to_read, "html.parser")

            # Getting the File's UUT (we're going to retrieve the UUT now, but if needed, all the others properties
            # could be easily retrieved)
            table_header = soup.find("table", class_="header")
            table_header_content = table_header.get_text()
            uut = table_header_content.split("UUT\n")[1].split("\n")[0]
            file_to_return.set_uut(uut)

            # Now, it's time to manage the Lines to return
            lines_to_return = []
            for content_raw in soup.findAll("table", class_=["teststepfail", "teststepfailGeneratedCommand"]):
                # Only the Tables of the Classes "teststepfail" or "teststepfailGeneratedCommand"  within the HTML file
                # are concerned by the selection made by the Application

                # So, first, let's get the content of those tables and process them
                content = content_raw.get_text()
                content = "\n".join([s for s in content.split("\n") if s])
                content_split = content.split("\n")

                # Now, let's get all the information (Data) that we need inside those Tables
                if re.search("^Open\n", content) and not re.search("\nMiswire\n", content):
                    """
                    The current Table's Data are related to Open Wires
                    """
                    name = content_split[1]
                    from_pins = content_split[2]
                    from_pins_comment = content_split[3]
                    to_pins = content_split[4]
                    to_pins_comment = content_split[5]

                    line_to_add = LineToRead()
                    line_to_add.set_name(name)
                    # Let's remind it, it's an Open Wires' line
                    line_to_add.set_type(LineTypesEnum.OPEN_WIRES)
                    line_to_add.set_from_pins(from_pins)
                    line_to_add.set_from_pins_comment(from_pins_comment)
                    line_to_add.set_to_pins(to_pins)
                    line_to_add.set_to_pins_comment(to_pins_comment)

                    lines_to_return.append(line_to_add)

                elif re.search("^Open\n", content) and re.search("\nMiswire\n", content):
                    """
                    The current Table's Data are related to Cross Pinning
                    """
                    cross_pinning_line_to_add = LineToReadCrossPinning()
                    name = content_split[1]
                    cross_pinning_line_to_add.set_name(name)
                    # Let's remind it, it's an Cross Pinning' line
                    cross_pinning_line_to_add.set_type(LineTypesEnum.CROSS_PINNING)

                    """
                    Managing the Miswire sub-lines
                    """
                    #  The 1-st Miswire sub-line
                    from_pins_1 = content_split[2]
                    from_pins_comment_1 = content_split[3]
                    to_pins_1 = content_split[4]
                    to_pins_comment_1 = content_split[5]
                    if re.search(":Z", content_split[6]):
                        # The current sub-line contains information on Splices, therefore, let's take them into account
                        cross_pinning_line_to_add.set_splices_list(content_split[6].split(", "))

                    cross_pinning_line_to_add.get_from_pins().append(from_pins_1)
                    cross_pinning_line_to_add.get_from_pins_comment().append(from_pins_comment_1)
                    cross_pinning_line_to_add.get_to_pins().append(to_pins_1)
                    cross_pinning_line_to_add.get_to_pins_comment().append(to_pins_comment_1)

                    #  The i in [2..N]-th Miswire sub-lines
                    not_miswire_part = content.split("\nMiswire\n")[0]
                    miswire_part = content.replace(not_miswire_part, "")
                    for miswire_line in miswire_part.split("\nMiswire\n"):
                        if len(miswire_line):
                            miswire_line_split = miswire_line.split("\n")
                            from_pins_i = miswire_line_split[0]
                            from_pins_comment_i = miswire_line_split[1]
                            to_pins_i = miswire_line_split[2]
                            to_pins_comment_i = miswire_line_split[3]

                            cross_pinning_line_to_add.get_from_pins().append(from_pins_i)
                            cross_pinning_line_to_add.get_from_pins_comment().append(from_pins_comment_i)
                            cross_pinning_line_to_add.get_to_pins().append(to_pins_i)
                            cross_pinning_line_to_add.get_to_pins_comment().append(to_pins_comment_i)

                    lines_to_return.append(cross_pinning_line_to_add)

                elif re.search("^Short\n", content) and re.search("\nIsolationTest\n", content):
                    """
                    The current Table's Data are related to Extra Wires - Shorts
                    """
                    from_pins = content_split[2]
                    from_pins_comment = content_split[3]
                    to_pins = content_split[4]
                    to_pins_comment = content_split[5]

                    line_to_add = LineToRead()
                    line_to_add.set_name(name)
                    # Let's remind it, it's an Extra Wires - Shorts' line
                    line_to_add.set_type(LineTypesEnum.EXTRA_WIRES_SHORTS)
                    line_to_add.set_from_pins(from_pins)
                    line_to_add.set_from_pins_comment(from_pins_comment)
                    line_to_add.set_to_pins(to_pins)
                    line_to_add.set_to_pins_comment(to_pins_comment)

                    lines_to_return.append(line_to_add)

            file_to_return.set_lines_to_read(lines_to_return)

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
        Since we still have to write the lines inside an Excel File, we are going to use that of the
        DATA_ACCESS.DAO.INTF.crud_file_dao_impl.CRUDFileDAOImpl.
        Therefore, we're going to just call this ready-to-use "write_line" function here.

        :param file_path: the file Path of Excel file where the line_to_add will be written
        :param line_to_add: The Line to be written
        :return: None
        """
        try:
            self.crud_file_dao.write_line(file_path, line_to_add)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise