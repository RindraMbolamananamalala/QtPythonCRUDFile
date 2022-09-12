from BUSINESS.MODEL.DOMAIN_OBJECT.file_to_read import FileToRead
from BUSINESS.MODEL.DTO.file_to_read_dto import FileToReadDTO
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read import LineToRead

from MAPPER.crud_file_mapper import file_to_read_to_file_to_read_dto, line_to_read_to_line_to_read_dto

if __name__ == "__main__":
    # file = FileToRead()
    # file.set_uut("UUT_test")
    # file.set_station("station_test")
    # file.set_operator("operator_test")
    # file.set_time("time_test")
    # file.set_date("date_test")
    # file.set_test_qty(1000)
    # file.set_failure_qty(100)
    # line_to_read_1 = LineToRead()
    # line_to_read_1.set_name("Name_test_1")
    # line_to_read_2 = LineToRead()
    # line_to_read_2.set_name("Name_test_2")
    # line_to_read_3 = LineToRead()
    # line_to_read_3.set_name("Name_test_3")
    # file.get_lines_to_read().append(line_to_read_1)
    # file.get_lines_to_read().append(line_to_read_2)
    # file.get_lines_to_read().append(line_to_read_3)
    #
    # file_dto = file_to_read_to_file_to_read_dto(file)
    #
    # for line in file_dto.get_lines_to_read():
    #     print(line)

    line_to_read = LineToRead()
    line_to_read.set_item("Item_test")
    line_to_read.set_name("2384/0.35`GN/BK")
    line_to_read.set_from_pins("E17/47*1-S_V1.2")
    line_to_read.set_to_pins("N10/6*RB1-B_V1.57")
    line_to_read.set_measurement("measurement_test")
    line_to_read.set_type("Type_test")
    line_to_read.set_result("Result_test")

    line_to_read_dto = line_to_read_to_line_to_read_dto(line_to_read)

    print(line_to_read_dto)