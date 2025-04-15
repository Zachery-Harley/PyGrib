from enum import IntEnum

from parser.exception import Grib2FormatException


def get_reference_time_significance(ref_time_sig: int):
    try:
        return ReferenceTimeSignificance(ref_time_sig)
    except ValueError:
        raise Grib2FormatException('Unsupported Significance of Reference Time: {}'.format(ref_time_sig))


class ReferenceTimeSignificance(IntEnum):
    ANALYSIS = 0,
    START_OF_FORCAST = 1,
    VERIFYING_TIME_OF_FORCAST = 2,
    OBSERVATION_TIME = 3,
    LOCAL_TIME = 4,
    SIMULATION_START = 5,
    MISSING = 255
