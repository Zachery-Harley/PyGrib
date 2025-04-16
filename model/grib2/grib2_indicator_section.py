from __future__ import annotations

from model.grib2.code_table import Discipline, get_discipline

IDENTIFIER_LENGTH: int = 4
RESERVED_LENGTH: int = 2
INDICATOR_SECTION_LENGTH: int = 16


class Grib2IndicatorSection:
    _discipline: Discipline

    def get_discipline(self) -> int:
        return self._discipline

    def set_discipline(self, discipline: Discipline | int) -> Grib2IndicatorSection:
        if isinstance(discipline, Discipline):
            self._discipline = discipline
        else:
            self._discipline = get_discipline(discipline)
        return self


class LengthAwareGrib2IndicatorSection(Grib2IndicatorSection):
    _recordLength: int

    def get_record_length(self) -> int:
        return self._recordLength

    def set_record_length(self, record_length: int) -> LengthAwareGrib2IndicatorSection:
        self._recordLength = record_length
        return self
