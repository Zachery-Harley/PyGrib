from model.grib2 import LengthAwareGrib2IndicatorSection
from model.grib2.grib2_indicator_section import IDENTIFIER_LENGTH, RESERVED_LENGTH, INDICATOR_SECTION_LENGTH
from parser import ByteParser
from parser.exception import Grib2FormatException


class Grib2IndicatorSectionParser:

    def parse(self, is_bytes: bytearray) -> LengthAwareGrib2IndicatorSection:
        self.__validate_bytes(is_bytes)
        parser: ByteParser = ByteParser(is_bytes).skip(IDENTIFIER_LENGTH + RESERVED_LENGTH)
        indicator_section: LengthAwareGrib2IndicatorSection = LengthAwareGrib2IndicatorSection()

        indicator_section.set_discipline(parser.next_uint_8())
        self.__validate_edition_number(parser.next_uint_8())
        indicator_section.set_record_length(parser.next_uint_8())

        return indicator_section

    @staticmethod
    def __validate_bytes(is_bytes: bytearray):
        if len(is_bytes) != INDICATOR_SECTION_LENGTH:
            raise Grib2FormatException(
                'Indicator Section expected {} bytes, got {}'.format(INDICATOR_SECTION_LENGTH, len(is_bytes)))

        if is_bytes[0:4] != 'GRIB':
            raise Grib2FormatException(
                'Indicator Section expected `identifier` to be GRIB, got {}'.format(len(is_bytes[0:4])))

    @staticmethod
    def __validate_edition_number(edition_number: int):
        if edition_number != 2:
            raise Grib2FormatException('Edition Number expected 2, got {}'.format(edition_number))
