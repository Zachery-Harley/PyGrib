from enum import IntEnum

from parser.exception import Grib2FormatException


def get_production_status(production_status: int):
    try:
        return ProductionStatus(production_status)
    except ValueError:
        raise Grib2FormatException('Unsupported Production Status: {}'.format(production_status))


class ProductionStatus(IntEnum):
    OPERATIONAL = 0,
    OPERATIONAL_TEST = 1,
    RESEARCH = 2,
    RE_ANALYSIS = 3,
    TIGGE = 4,
    TIGGE_TEST = 5,
    S2S = 6,
    S2S_TEST = 7,
    UERRAN = 8,
    UERRAN_TEST = 9,
    CARRA = 10,
    CARRA_TEST = 11,
    DESTINATION_EARTH = 12,
    DESTINATION_EARTH_TEST = 13,
    MISSING = 255
