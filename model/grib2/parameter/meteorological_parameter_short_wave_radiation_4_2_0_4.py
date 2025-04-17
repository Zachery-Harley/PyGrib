from model.grib2.parameter import Parameter, Unit

meteorological_short_wave = {
    0: Parameter(
        id=0,
        name='Net Short-Wave Radiation Flux (Surface)',
        abbrev='NSWRS',
        unit=Unit.WATTS_PER_METER_SQUARED,
        deprecated=True
    ),
    1: Parameter(
        id=1,
        name='Net Short-Wave Radiation Flux (Top of Atmosphere)',
        abbrev='NSWRT',
        unit=Unit.WATTS_PER_METER_SQUARED,
        deprecated=True
    ),
    2: Parameter(
        id=2,
        name='Short-Wave Radiation Flux',
        abbrev='SWAVR',
        unit=Unit.WATTS_PER_METER_SQUARED,
        deprecated=True
    ),
    3: Parameter(
        id=3,
        name='Global Radiation Flux',
        abbrev='GRAD',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    4: Parameter(
        id=4,
        name='Brightness Temperature',
        abbrev='BRTMP',
        unit=Unit.KELVIN
    ),
    5: Parameter(
        id=5,
        name='Radiance (with respect to wave number)',
        abbrev='LWRAD',
        unit=Unit.WATTS_PER_METER_PER_STERADIAN
    ),
    6: Parameter(
        id=6,
        name='Radiance (with respect to wavelength)',
        abbrev='SWRAD',
        unit=Unit.WATTS_PER_METER_CUBED_PER_STERADIAN
    ),
    7: Parameter(
        id=7,
        name='Downward Short-Wave Radiation Flux',
        abbrev='DSWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    8: Parameter(
        id=8,
        name='Upward Short-Wave Radiation Flux',
        abbrev='USWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    9: Parameter(
        id=9,
        name='Net Short Wave Radiation Flux',
        abbrev='NSWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    10: Parameter(
        id=10,
        name='Photosynthetically Active Radiation',
        abbrev='PHOTAR',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    11: Parameter(
        id=11,
        name='Net Short-Wave Radiation Flux, Clear Sky',
        abbrev='NSWRFCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    12: Parameter(
        id=12,
        name='Downward UV Radiation',
        abbrev='DWUVR',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    13: Parameter(
        id=13,
        name='Direct Short Wave Radiation Flux',
        abbrev='DSWRFLX',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    14: Parameter(
        id=14,
        name='Diffuse Short Wave Radiation Flux',
        abbrev='DIFSWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    15: Parameter(
        id=15,
        name='Upward UV radiation emitted/reflected from the Earths surface',
        abbrev='UVVEARTH',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),

    50: Parameter(
        id=50,
        name='UV Index (Under Clear Sky)',
        abbrev='UVIUCS',
        unit=Unit.NUMERIC
    ),
    51: Parameter(
        id=51,
        name='UV Index',
        abbrev='UVI',
        unit=Unit.NUMERIC
    ),
    52: Parameter(
        id=52,
        name='Downward Short-Wave Radiation Flux, Clear Sky',
        abbrev='DSWRFCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    53: Parameter(
        id=53,
        name='Upward Short-Wave Radiation Flux, Clear Sky',
        abbrev='USWRFCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    54: Parameter(
        id=54,
        name='Direct normal short-wave radiation flux',
        abbrev='DNSWRFLX',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    55: Parameter(
        id=55,
        name='UV visible albedo for diffuse radiation',
        abbrev='UVALBDIF',
        unit=Unit.PERCENT
    ),
    56: Parameter(
        id=56,
        name='UV visible albedo for direct radiation',
        abbrev='UVALBDIR',
        unit=Unit.PERCENT
    ),
    57: Parameter(
        id=57,
        name='UV visible albedo for direct radiation, geometric component',
        abbrev='UBALBDIRG',
        unit=Unit.PERCENT
    ),
    58: Parameter(
        id=58,
        name='UV visible albedo for direct radiation, isotropic component',
        abbrev='UVALBDIRI',
        unit=Unit.PERCENT
    ),
    59: Parameter(
        id=59,
        name='UV visible albedo for direct radiation, volumetric component',
        abbrev='UVBDIRV',
        unit=Unit.PERCENT
    ),
    60: Parameter(
        id=60,
        name='Photosynthetically active radiation flux, clear sky',
        abbrev='PHOARFCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    61: Parameter(
        id=61,
        name='Direct short-wave radiation flux, clear sky',
        abbrev='DSWRFLXCS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),

    192: Parameter(
        id=192,
        name='Downward Short-Wave Radiation Flux',
        abbrev='DSWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    193: Parameter(
        id=193,
        name='Upward Short-Wave Radiation Flux',
        abbrev='USWRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    194: Parameter(
        id=194,
        name='UV-B Downward Solar Flux',
        abbrev='DUVB',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    195: Parameter(
        id=195,
        name='Clear sky UV-B Downward Solar Flux',
        abbrev='CDUVB',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    196: Parameter(
        id=196,
        name='Clear Sky Downward Solar Flux',
        abbrev='CSDSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    197: Parameter(
        id=197,
        name='Solar Radiative Heating Rate',
        abbrev='SWHR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    198: Parameter(
        id=198,
        name='Clear Sky Upward Solar Flux',
        abbrev='CSUSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    199: Parameter(
        id=199,
        name='Cloud Forcing Net Solar Flux',
        abbrev='CFNSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    200: Parameter(
        id=200,
        name='Visible Beam Downward Solar Flux',
        abbrev='VBDSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    201: Parameter(
        id=201,
        name='Visible Diffuse Downward Solar Flux',
        abbrev='VDDSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    202: Parameter(
        id=202,
        name='Near IR Beam Downward Solar Flux',
        abbrev='NBDSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    203: Parameter(
        id=203,
        name='Near IR Diffuse Downward Solar Flux',
        abbrev='NDDSF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    204: Parameter(
        id=204,
        name='Downward Total Radiation Flux',
        abbrev='DTRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    205: Parameter(
        id=205,
        name='Upward Total Radiation Flux',
        abbrev='UTRF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
