from dataclasses import dataclass
from enum import Enum


class Unit(Enum):
    CELSIUS = 'C'
    CM_PER_DAY = 'cm/day'
    DAY = 'day'
    DEGREE = 'deg'
    GEOPOTENTIAL_METERS = 'gpm'
    HECTOPASCAL = 'hPa'
    HOUR = 'hour'
    JULES = 'J'
    JULES_PER_KG = 'Jkg-1'
    JOULES_PER_SQUARE_METER_PER_KELVIN = 'Jm-2K'
    KELVIN = 'K'
    KELVIN_METERS_PER_SECOND = 'Kms-1'
    KELVIN_PER_METER = 'Km-1'
    KELVIN_PER_METER_SQUARED_PER_KG_PER_SECOND = 'Km2kg-1s-1'
    KELVIN_PER_SECOND = 'Ks-1'
    KG_PER_KG = 'kgkg-1'
    KG_PER_KG_PER_METER_PER_SECOND = 'kgkg-1s-1'
    KG_PER_KG_PER_SECOND = 'kgkg-1s-1'
    KG_PER_METER_CUBED = 'kgm-3'
    KG_PER_METER_CUBED_PER_SECOND = 'kgm-3s-1'
    KG_PER_METER_PER_SECOND = 'kgm-1s-1'
    KG_PER_SQUARE_METER = 'kgm-2'
    KG_PER_SQUARE_METER_PER_SECOND = 'kgm-2s-1'
    KNOTS = 'kt'
    LOG_MICROGRAMS_PER_CUBIC_METER = 'log10 (µg m-3)'
    METERS = 'm'
    METERS_CUBED = 'm-3'
    METERS_PER_SECOND = 'ms-1'
    METERS_PER_SECOND_SQUARED = 'ms-2'
    METERS_SQUARED_PER_SECOND = 'm-2s-1'
    KM_SQUARED_PER_DAY = 'km-2day-1'
    MICROGRAMS_PER_CUBIC_METER = 'µg m-3'
    NATURAL_LOG_KILO_PASCAL = 'ln(kPa)'
    NEWTONS_PER_METER_SQUARED = 'Nm-2'
    NEWTONS_PER_METER_SQUARED_PER_SECOND = 'Nm-2s'
    NONE = ''
    NON_DIM = 'non-dim'
    NUMERIC = 'numeric'
    PASCAL = 'Pa'
    PASCAL_PER_SECOND = 'Pas-1'
    PERCENT = '%'
    PER_KG = 'kg-1'
    PER_METER = 'm-1'
    PER_SECOND = 's-1'
    PER_SECOND_PER_METER = '1/s/m'
    PROPORTION = 'proportion'
    RADIANS = 'rad'
    SECOND = 'second'
    SECONDS_SQUARED = 's-2'
    SQUARE_METERS_PER_SECOND = 'm2s-1'
    SQUARE_METERS_PER_SECOND_SQUARED = 'm2s-2'
    WATTS_PER_METER = 'Wm-1'
    WATTS_PER_METER_CUBED_PER_STERADIAN = 'Wm-3sr-1'
    WATTS_PER_METER_PER_STERADIAN = 'Wm-1sr-1'
    WATTS_PER_METER_SQUARED = 'Wm-2'
    DOBSON = 'DU'
    PPBV = 'ppbV'
    PPB = 'ppb'
    DECIBEL = 'dB'
    MM_M6_M3 = 'm m6 m-3'


@dataclass(frozen=True)
class Parameter:
    id: int
    name: str | None
    abbrev: str | None = None
    unit: Unit = Unit.NONE
    deprecated: bool = False
