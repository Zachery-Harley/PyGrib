from model.grib2 import LengthAwareGrib2IndicatorSection, Grib2Section
from parser.grib2 import Grib2IndicatorSectionParser, Grib2Record, Grib2SectionScanner


class Grib2Parser:

    def parse(self, record_bytes: bytearray) -> Grib2Record:
        scanner = Grib2SectionScanner(record_bytes)
        current_section = scanner.next_section()

        while current_section is not None:
            current_section = scanner.next_section()

    @staticmethod
    def parse_indicator(is_data: bytearray) -> LengthAwareGrib2IndicatorSection:
        """
        Given the bytes for an indicator section, parse and create the indicator section
        :param is_data: The 16 bytes that make up the indicator section
        :return: An indicator section
        """
        return Grib2IndicatorSectionParser().parse(is_data)

    def _parse_section(self, section: Grib2Section, section_bytes: bytearray) -> Grib2Section:
        
