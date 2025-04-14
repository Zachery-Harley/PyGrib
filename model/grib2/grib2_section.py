from enum import IntEnum


class Grib2Section(IntEnum):
    INDICATOR = 0,
    IDENTIFICATION = 1,
    LOCAL_USE = 2,
    GRID_DEFINITION = 3,
    PRODUCT_DEFINITION = 4,
    DATA_REPRESENTATION = 5,
    BIT_MAP = 6,
    DATA = 7,
    END = 8
