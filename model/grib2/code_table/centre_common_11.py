from enum import Enum

from parser.exception import Grib2FormatException


class Centre(Enum):
    MET_OFFICE_74 = 74,
    MET_OFFICE_75 = 75


def get_centre(centre_id: int) -> Centre:
    try:
        return Centre(centre_id)
    except KeyError:
        raise Grib2FormatException('Unsupported centre ID: {}'.format(centre_id))
