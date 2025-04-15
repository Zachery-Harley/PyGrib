from enum import IntEnum

from parser.exception import Grib2FormatException


def get_data_type(data_type: int):
    try:
        return DataType(data_type)
    except ValueError:
        raise Grib2FormatException('Unsupported Data Type: {}'.format(data_type))


class DataType(IntEnum):
    ANALYSIS = 0,
    FORCAST = 1,
    ANALYSIS_AND_FORCAST = 2,
    CONTROL_FORCAST = 3,
    PERTURBED_FORCAST = 4,
    CONTROL_AND_PERTURBED_FORCAST = 5,
    PROCESSED_SATELLITE_OBSERVATIONS = 6,
    PROCESSED_RADAR_OBSERVATIONS = 7,
    EVENT_PROBABILITY = 8,
    EXPERIMENTAL_DATA = 9,
    ML_BASED_FORECAST = 10,
    MISSING = 255
