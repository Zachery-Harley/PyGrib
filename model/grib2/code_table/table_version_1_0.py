from enum import IntEnum

from parser.exception import Grib2FormatException


def get_table_version(version_id: int):
    try:
        return TableVersion(version_id)
    except ValueError:
        raise Grib2FormatException('Unsupported table version: {}'.format(version_id))


class TableVersion(IntEnum):
    EXPERIMENTAL = 0,
    V07NOV2001 = 1,
    V04NOV2003 = 2,
    V02NOV2005 = 3,
    V07NOV2007 = 4,
    V04NOV2009 = 5,
    V15SEP2010 = 6,
    V04MAY2011 = 7,
    V02NOV2011 = 8,
    V02MAY2012 = 9,
    V07NOV2012 = 10,
    V08MAY2013 = 11,
    V14NOV2013 = 12,
    V07MAY2014 = 13,
    V05NOV2014 = 14,
    V06MAY2015 = 15,
    V11NOV2015 = 16,
    V04MAY2016 = 17,
    V02NOV2016 = 18,
    V03MAY2017 = 19,
    V08NOV2017 = 20,
    V02MAY2018 = 21,
    V07NOV2018 = 22,
    V15MAY2019 = 23,
    V06NOV2019 = 24,
    V06MAY2020 = 25,
    V16NOV2020 = 26,
    V15JUN2021 = 27,
    V15NOV2021 = 28,
    V15MAY2022 = 29,
    V15NOV2022 = 30,
    V15MAY2023 = 31,
    V30NOV2023 = 32,
    V15MAY2024 = 33,
    V18NOV2024 = 34,
    PRE_OPERATIONAL = 35,
    MISSING = 255
