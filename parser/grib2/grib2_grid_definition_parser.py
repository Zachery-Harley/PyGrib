from model.grib2 import Grib2Section, Grib2GridDefinitionSection
from parser import ByteParser
from parser.grib2 import Grib2SectionParser


class Grib2GridDefinitionParser(Grib2SectionParser):

    def parse(self, gds_data: bytearray):
        parser: ByteParser = ByteParser(gds_data)
        self.__validate_section_header(gds_data, parser, Grib2Section.GRID_DEFINITION)

        section: Grib2GridDefinitionSection = Grib2GridDefinitionSection()
        (section
         .set_source_of_grid_definition(parser.next_uint_8())
         .set_number_of_data_points(parser.next_uint_32())
         .set_quasi_regular_octets_per_value(parser.next_uint_8())
         .set_quasi_regular_grid_interpretation(parser.next_uint_8())
         .set_grid_definition_template_number(parser.next_uint_8()))


       # Need to add a parser.get_flag_byte