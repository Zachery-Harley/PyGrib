from enum import IntEnum

from parser.exception import Grib2FormatException


def get_earth_shape(earth_shape: int):
    try:
        return EarthShape(earth_shape)
    except ValueError:
        raise Grib2FormatException('Unsupported Earth Shape: {}'.format(earth_shape))


class EarthShape(IntEnum):
    SPHERICAL_6367470 = 0,
    SPHERICAL_DEFINED = 1,
    OBLATE_SPHEROID = 2,
    OBLATE_SPHEROID_DEFINED_KM = 3,
    IAG_GRS80 = 4,
    WGS84 = 5,
    SPHERICAL_6371229 = 6,
    OBLATE_SPHEROID_DEFINED_M = 7,
    SPHERICAL_6371200_WGS84 = 8,
    ORDNANCE_SURVEY_1936 = 9,
    WGS84_CORRECTED_GEOMAGNETIC_COORDINATES = 10,
    SUN_695990000 = 11,
    MISSING = 255
