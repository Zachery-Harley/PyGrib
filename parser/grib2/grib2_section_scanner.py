from typing import Tuple

from model.grib2 import Grib2Section
from model.grib2.grib2_end_section import END_SECTION_LENGTH
from model.grib2.grib2_indicator_section import INDICATOR_SECTION_LENGTH
from parser import ByteParser

_SECTION_HEADER_LENGTH = 4


class Grib2SectionScanner:
    _bytes_: bytearray
    _position: int
    _indicator_read: bool

    def __init__(self, record_bytes: bytearray):
        self._bytes_ = record_bytes
        self._indicator_read = False
        self._position = 0

    def next_section(self) -> Tuple[Grib2Section, bytearray] | None:
        if self._remaining_length() == 0:
            return None

        if not self._indicator_read:
            self._indicator_read = True
            return Grib2Section.INDICATOR, self._read_next(INDICATOR_SECTION_LENGTH)
        else:
            return self._read_next_section()

    def _read_next_section(self) -> Tuple[Grib2Section, bytearray]:
        if self._remaining_length() == END_SECTION_LENGTH:
            return Grib2Section.END, self._read_next(END_SECTION_LENGTH)
        else:
            parser = ByteParser(self._read_next(_SECTION_HEADER_LENGTH))
            section_length = parser.next_uint_32()
            section_number = parser.next_uint_8()
            self._rewind(_SECTION_HEADER_LENGTH)
            return Grib2Section(section_number), self._read_next(section_length)

    def _remaining_length(self):
        return len(self._bytes_) - self._position

    def _read_next(self, length: int) -> bytearray:
        return self._bytes_[self._position: self._position + length]

    def _rewind(self, offset: int):
        self._position -= offset
