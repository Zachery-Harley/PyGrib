from model.grib2 import Grib2Section, Grib2GDS
from parser import ByteParser
from parser.grib2 import Grib2SectionParser
from parser.grib2.template import parse_gds_template


class Grib2GridDefinitionParser(Grib2SectionParser):

    def parse(self, gds_data: bytearray) -> Grib2GDS:
        parser: ByteParser = ByteParser(gds_data)
        self.__validate_section_header(gds_data, parser, Grib2Section.GRID_DEFINITION)

        section: Grib2GDS = Grib2GDS()
        (section
         .set_source_of_grid_definition(parser.next_uint_8())
         .set_number_of_data_points(parser.next_uint_32())
         .set_quasi_regular_octets_per_value(parser.next_uint_8())
         .set_quasi_regular_grid_interpretation(parser.next_uint_8())
         .set_grid_definition_template_number(parser.next_uint_8()))

        section = parse_gds_template(section.get_grid_definition_template(), section, parser)
        quasi_list = self.parse_quasi_regular_list(parser, section)
        section.set_quasi_regular_list = quasi_list
        return section

    @staticmethod
    def parse_quasi_regular_list(parser, section):
        quasi_list = []
        while parser.get_remaining_bytes() > 0:
            quasi_list.append(parser.next_uint(section.get_quasi_regular_octets_per_value()))
        return quasi_list
