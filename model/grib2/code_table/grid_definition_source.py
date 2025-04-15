from enum import IntEnum

from parser.exception import Grib2FormatException


def get_grid_definition_source(grid_def_src: int):
    try:
        return GridDefinitionSource(grid_def_src)
    except ValueError:
        raise Grib2FormatException('Unsupported Grid Definition Source: {}'.format(grid_def_src))


class GridDefinitionSource(IntEnum):
    SPECIFIED = 0,
    PREDETERMINED = 1,
    DOES_NOT_APPLY = 255
