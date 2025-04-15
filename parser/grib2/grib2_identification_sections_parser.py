from model.grib2 import Grib2IdentificationSection, Grib2Section
from parser import ByteParser
from parser.grib2 import Grib2SectionParser


class Grib2IdentificationSectionParser(Grib2SectionParser):

    def parse(self, ids_bytes: bytearray) -> Grib2IdentificationSection:
        parser: ByteParser = ByteParser(ids_bytes[:21])
        self.__validate_section_header(ids_bytes, parser, Grib2Section.IDENTIFICATION)

        section = Grib2IdentificationSection()
        section.set_centre(parser.next_uint_8())
        section.set_sub_centre(parser.next_uint_8())
        section.set_table_version(parser.next_uint_8())
        section.set_local_table_version(parser.next_uint_8())

        section.set_year(parser.next_uint_16())
        section.set_month(parser.next_uint_8())
        section.set_day(parser.next_uint_8())
        section.set_hour(parser.next_uint_8())
        section.set_minute(parser.next_uint_8())
        section.set_second(parser.next_uint_8())
        section.set_production_status(parser.next_uint_8())
        section.set_data_type(parser.next_uint_8())

        return section