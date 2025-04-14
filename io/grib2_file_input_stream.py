import os
from typing import BinaryIO

from io.grib2_input_stream import Grib2InputStream


class Grib2FileInputStream(Grib2InputStream):
    __file__: BinaryIO
    __file_size__: int
    __record__: bytearray

    def __init__(self, file_path: str):
        self.__file__ = open(file_path, 'rb')
        self.__file_size__ = os.path.getsize(file_path)

    def end_of_file(self) -> bool:
        return self.__file_size__ == self.__file__.tell()

    def close(self):
        self.__file__.close()

    def next_record(self):
        if self.bytes_remaining() > 16:
            self.__record__ = bytearray()
            self.__record__.extend(self.__file__.read(16))
        else:
            return None

    def bytes_remaining(self):
        return self.__file_size__ - self.__file__.tell()
