from model.grib2.parameter import Parameter, Unit

meteorological_long_wave = {
    0: Parameter(
        id=0,
        name='Net Long-Wave Radiation Flux (Surface)',
        abbrev='NLWRS',
        unit=Unit.WATTS_PER_METER_SQUARED,
        deprecated=True
    ),
    1: Parameter(
        id=1,
        name='Net Long-Wave Radiation Flux (Top of Atmosphere)',
        abbrev='NLWRT',
        unit=Unit.WATTS_PER_METER_SQUARED,
        deprecated=True
    ),
    2: Parameter(
        id=2,
        name='Long-Wave Radiation Flux',
        abbrev='LWAVR',
        unit=Unit.WATTS_PER_METER_SQUARED,
        deprecated=True
    ),
    3: Parameter(
        id=3,
        name='Downward Long-Wave Rad. Flux',
        abbrev='DLWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    4: Parameter(
        id=4,
        name='Upward Long-Wave Rad. Flux',
        abbrev='ULWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    5: Parameter(
        id=5,
        name='Net Long-Wave Radiation Flux',
        abbrev='NLWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    6: Parameter(
        id=6,
        name='Net Long-Wave Radiation Flux, Clear Sky',
        abbrev='NLWRCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    7: Parameter(
        id=7,
        name='Brightness Temperature',
        abbrev='BRTEMP',
        unit=Unit.KELVIN
    ),
    8: Parameter(
        id=8,
        name='Downward Long-Wave Radiation Flux, Clear Sky',
        abbrev='DLWRFCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    9: Parameter(
        id=9,
        name='Near IR albedo for diffuse radiation',
        abbrev='NIRALBDIF',
        unit=Unit.PERCENT
    ),
    10: Parameter(
        id=10,
        name='Near IR albedo for direct radiation',
        abbrev='NIRALBDIR',
        unit=Unit.PERCENT
    ),
    11: Parameter(
        id=11,
        name='Near IR albedo for direct radiation, geometric component',
        abbrev='NIRALBDIRG',
        unit=Unit.PERCENT
    ),
    12: Parameter(
        id=12,
        name='Near IR albedo for direct radiation, isotropic component',
        abbrev='NIRALBDIRI',
        unit=Unit.PERCENT
    ),
    13: Parameter(
        id=13,
        name='Near IR albedo for direct radiation, volumetric component',
        abbrev='NIRALBDIRV',
        unit=Unit.PERCENT
    ),

    192: Parameter(
        id=192,
        name='Downward Long-Wave Rad. Flux',
        abbrev='DLWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    193: Parameter(
        id=193,
        name='Upward Long-Wave Rad. Flux',
        abbrev='ULWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    194: Parameter(
        id=194,
        name='Long-Wave Radiative Heating Rate',
        abbrev='LWHR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    195: Parameter(
        id=195,
        name='Clear Sky Upward Long Wave Flux',
        abbrev='CSULF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    196: Parameter(
        id=196,
        name='Clear Sky Downward Long Wave Flux',
        abbrev='CSDLF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    197: Parameter(
        id=197,
        name='Cloud Forcing Net Long Wave Flux',
        abbrev='CFNLF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
