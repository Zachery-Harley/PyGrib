from model.grib2 import LengthAwareGrib2IndicatorSection, Grib2Section, Grib2IndicatorSection, \
    Grib2IdentificationSection
from parser.exception import Grib2FormatException
from parser.grib2 import Grib2IndicatorSectionParser, Grib2Record, Grib2SectionScanner


class Grib2Parser:

    def parse(self, record_bytes: bytearray) -> Grib2Record:
        scanner = Grib2SectionScanner(record_bytes)
        current_section = scanner.next_section()

        while current_section is not None:
            current_section = scanner.next_section()

    def _parse_section(self, record: Grib2Record, section: Grib2Section, section_bytes: bytearray) -> Grib2Record:
        match section:
            case Grib2Section.INDICATOR:
                if record.indicator is not None:
                    raise Grib2FormatException('An Indicator Section has already been parsed')
                return record.set_indicator(self.parse_indicator(section_bytes))
            case Grib2Section.IDENTIFICATION:
                if record.identification is not None:
                    raise Grib2FormatException('An Identification Section has already been parsed')
                return record.set_identification(self.parse_identification (section_bytes))

    @staticmethod
    def parse_identification(ids_data: bytearray) -> Grib2IdentificationSection:
        return Grib2IdentificationSectionParser().parse(ids_data)

    @staticmethod
    def parse_indicator(is_data: bytearray) -> LengthAwareGrib2IndicatorSection:
        """
        Given the bytes for an indicator section, parse and create the indicator section
        :param is_data: The 16 bytes that make up the indicator section
        :return: An indicator section
        """
        return Grib2IndicatorSectionParser().parse(is_data)

