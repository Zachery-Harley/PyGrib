from __future__ import annotations

from model.grib2 import Grib2IndicatorSection, Grib2IdentificationSection
from parser.grib2.grib2_parser import Grib2Parser


class Grib2Record(Grib2Parser):
    _indicator: Grib2IndicatorSection
    _identification: Grib2IdentificationSection

    def get_indicator(self) -> Grib2IndicatorSection:
        return self._indicator

    def set_indicator(self, indicator: Grib2IndicatorSection) -> Grib2Record:
        self._indicator = indicator
        return self

    def get_identification(self) -> Grib2IdentificationSection:
        return self._identification

    def set_identification(self, identification: Grib2IdentificationSection) -> Grib2Record:
        self._identification = identification
        return self
