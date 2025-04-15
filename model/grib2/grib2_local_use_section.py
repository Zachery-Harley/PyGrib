from __future__ import annotations


class Grib2LocalUseSection:
    _local_use: bytearray = None

    def get_local_use(self) -> bytearray:
        return self._local_use

    def set_local_use(self, local_use: bytearray) -> Grib2LocalUseSection:
        self._local_use = local_use
        return self
