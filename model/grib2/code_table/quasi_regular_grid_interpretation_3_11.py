from enum import IntEnum

from parser.exception import Grib2FormatException


def get_quasi_regular_grid_interpretation(qrgi: int):
    try:
        return QuasiRegularGridInterpretation(qrgi)
    except ValueError:
        raise Grib2FormatException('Unsupported Quasi Regular Grid Interpretation: {}'.format(qrgi))

class QuasiRegularGridInterpretation(IntEnum):
    NO_LIST = 0,
    FULL_CIRCLES = 1,
    BETWEEN_EXTREMES = 2,
    SPECIFIED_LATITUDES = 3,
