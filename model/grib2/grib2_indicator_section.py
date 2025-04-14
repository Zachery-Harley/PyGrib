from __future__ import annotations

IDENTIFIER_LENGTH: int = 4
RESERVED_LENGTH: int = 2
INDICATOR_SECTION_LENGTH: int = 16


class Grib2IndicatorSection:
    discipline: int

    def set_discipline(self, discipline: int) -> Grib2IndicatorSection:
        self.discipline = discipline
        return self

    def validate(self):
        pass


class LengthAwareGrib2IndicatorSection(Grib2IndicatorSection):
    recordLength: int

    def set_record_length(self, record_length: int) -> Grib2IndicatorSection:
        self.recordLength = record_length
        return self
