from enum import IntEnum

from parser.exception import Grib2FormatException


def get_discipline(discipline: int):
    try:
        return Discipline(discipline)
    except ValueError:
        raise Grib2FormatException('Unsupported Discipline: {}'.format(discipline))


class Discipline(IntEnum):
    METEOROLOGICAL = 0,
    HYDROLOGICAL = 1,
    LAND_SURFACE = 2,
    SATELLITE = 3,
    SPACE = 4,
    OCEANOGRAPHIC = 10,
    HEALTH = 20,
    MISSING = 255
