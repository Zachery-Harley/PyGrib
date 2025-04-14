from model.grib2 import Grib2EndSection
from parser.exception import Grib2FormatException


class Grib2EndSectionParser:

    def parse(self, end_data: bytearray) -> Grib2EndSection:
        if end_data != '7777':
            raise Grib2FormatException('Expected End Section to have value `7777` but got {}'.format(end_data))
        return Grib2EndSection()
