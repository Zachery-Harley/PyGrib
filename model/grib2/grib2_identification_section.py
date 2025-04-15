from __future__ import annotations

from model.grib2.code_table import Centre, get_centre


class Grib2IdentificationSection:
    _centre: Centre = None

    def set_centre(self, centre_id: int | Centre) -> Grib2IdentificationSection:
        if isinstance(centre_id, Centre):
            self._centre = centre_id
        else:
            self._centre = get_centre(centre_id)
