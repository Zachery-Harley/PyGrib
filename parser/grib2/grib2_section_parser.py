from model.grib2 import Grib2Section
from parser import ByteParser
from parser.exception import Grib2FormatException


class Grib2SectionParser:

    @staticmethod
    def __validate_section_header(section_parser: bytearray, parser: ByteParser, expected_section: Grib2Section):
        section_length = parser.next_uint_32()
        section_number = parser.next_uint_8()

        if len(section_parser) < section_length:
            raise Grib2FormatException(
                "Invalid {} Section length: Expected {}, got {}".format(
                    expected_section, section_length, len(section_parser))
            )

        if section_number != expected_section.value:
            raise Grib2FormatException(
                "Invalid section number for {} Section: Expected {}, got {}".format(
                    expected_section, expected_section.value, section_number)
            )
