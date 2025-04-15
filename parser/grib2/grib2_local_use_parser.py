from model.grib2 import Grib2Section, Grib2LocalUseSection
from parser import ByteParser
from parser.grib2 import Grib2SectionParser


class Grib2LocalUseParser(Grib2SectionParser):

    def parse(self, loc_bytes: bytearray):
        parser: ByteParser = ByteParser(loc_bytes)
        self.__validate_section_header(loc_bytes, parser, Grib2Section.LOCAL_USE)

        section: Grib2LocalUseSection = Grib2LocalUseSection()
        section.set_local_use(parser.get_remaining_bytes())
        return section
