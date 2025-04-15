from __future__ import annotations


class ScanningMode:
    _parallel_scans_negative: bool = False
    _meridian_scans_positive: bool = False
    _row_scans_meridian: bool = False
    _row_alternates_direction: bool = False

    def is_parallel_scans_negative(self) -> bool:
        return self._parallel_scans_negative

    def is_meridian_scans_positive(self) -> bool:
        return self._meridian_scans_positive

    def is_row_scans_meridian(self) -> bool:
        return self._row_scans_meridian

    def is_row_alternates_direction(self) -> bool:
        return self._row_alternates_direction

    def set_parallel_scans_negative(self, value: bool) -> ScanningMode:
        self._parallel_scans_negative = value
        return self

    def set_meridian_scans_positive(self, value: bool) -> ScanningMode:
        self._meridian_scans_positive = value
        return self

    def set_row_scans_meridian(self, value: bool) -> ScanningMode:
        self._row_scans_meridian = value
        return self

    def set_row_alternates_direction(self, value: bool) -> ScanningMode:
        self._row_alternates_direction = value
        return self
