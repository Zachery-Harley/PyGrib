from __future__ import annotations

IDENTIFIER_LENGTH: int = 4
RESERVED_LENGTH: int = 2
INDICATOR_SECTION_LENGTH: int = 16


class Grib2IndicatorSection:
    _discipline: int

    def get_discipline(self) -> int:
        return self._discipline

    def set_discipline(self, discipline: int) -> Grib2IndicatorSection:
        self._discipline = discipline
        return self


class LengthAwareGrib2IndicatorSection(Grib2IndicatorSection):
    _recordLength: int

    def get_record_length(self) -> int:
        return self._recordLength

    def set_record_length(self, record_length: int) -> LengthAwareGrib2IndicatorSection:
        self._recordLength = record_length
        return self
