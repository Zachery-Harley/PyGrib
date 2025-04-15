from enum import IntEnum

from parser.exception import Grib2FormatException


def get_grid_definition_template(grid_def_template: int):
    try:
        return GridDefinitionTemplate(grid_def_template)
    except ValueError:
        raise Grib2FormatException('Unsupported Grid Definition Template: {}'.format(grid_def_template))


class GridDefinitionTemplate(IntEnum):
    LAT_LON = 0,
    MISSING = 65535
