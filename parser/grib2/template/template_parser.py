from abc import ABC, abstractmethod

from model.grib2 import Grib2GDS
from parser import ByteParser


class GDSTemplateParser(ABC):

    @abstractmethod
    def parse(self, gds: Grib2GDS, template_data: bytearray | ByteParser):
        pass
