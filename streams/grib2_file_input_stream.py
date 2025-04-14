import os
from typing import BinaryIO

from model.grib2.grib2_indicator_section import INDICATOR_SECTION_LENGTH
from parser.grib2 import Grib2Record
from parser.grib2.grib2_parser import Grib2Parser
from streams.grib2_input_stream import Grib2InputStream


class Grib2FileInputStream(Grib2InputStream):
    _file: BinaryIO
    _file_size: int
    _record: bytearray

    def __init__(self, file_path: str):
        self._file = open(file_path, 'rb')
        self._file_size = os.path.getsize(file_path)

    def end_of_file(self) -> bool:
        return self._file_size == self._file.tell()

    def close(self):
        self._file.close()

    def next_record(self) -> Grib2Record | None:
        if self.bytes_remaining() > INDICATOR_SECTION_LENGTH:
            self._record = bytearray()
            self._record.extend(self._file.read(INDICATOR_SECTION_LENGTH))
            self._read_remaining_record()
            return Grib2Parser.parse(self._record)
        else:
            return None

    def _read_remaining_record(self):
        record_length = Grib2Parser.parse_indicator(self._record).recordLength
        self._record.extend(self._file.read(record_length - INDICATOR_SECTION_LENGTH))

    def bytes_remaining(self):
        return self._file_size - self._file.tell()
