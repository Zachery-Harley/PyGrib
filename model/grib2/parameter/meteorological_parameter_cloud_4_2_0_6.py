from model.grib2.parameter import Parameter, Unit

meteorological_cloud = {
    0: Parameter(
        id=0,
        name='Cloud Ice',
        abbrev='CICE',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    1: Parameter(
        id=1,
        name='Total Cloud Cover',
        abbrev='TCDC',
        unit=Unit.PERCENT
    ),
    2: Parameter(
        id=2,
        name='Convective Cloud Cover',
        abbrev='CDCON',
        unit=Unit.PERCENT
    ),
    3: Parameter(
        id=3,
        name='Low Cloud Cover',
        abbrev='LCDC',
        unit=Unit.PERCENT
    ),
    4: Parameter(
        id=4,
        name='Medium Cloud Cover',
        abbrev='MCDC',
        unit=Unit.PERCENT
    ),
    5: Parameter(
        id=5,
        name='High Cloud Cover',
        abbrev='HCDC',
        unit=Unit.PERCENT
    ),
    6: Parameter(
        id=6,
        name='Cloud Water',
        abbrev='CWAT',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    7: Parameter(
        id=7,
        name='Cloud Amount',
        abbrev='CDCA',
        unit=Unit.PERCENT
    ),
    8: Parameter(
        id=8,
        name='Cloud Type',
        abbrev='CDCT'
    ),
    9: Parameter(
        id=9,
        name='Thunderstorm Maximum Tops',
        abbrev='TMAXT',
        unit=Unit.METERS
    ),
    10: Parameter(
        id=10,
        name='Thunderstorm Coverage',
        abbrev='THUNC'
    ),
    11: Parameter(
        id=11,
        name='Cloud Base',
        abbrev='CDCB',
        unit=Unit.METERS
    ),
    12: Parameter(
        id=12,
        name='Cloud Top',
        abbrev='CDCTOP',
        unit=Unit.METERS
    ),
    13: Parameter(
        id=13,
        name='Ceiling',
        abbrev='CEIL',
        unit=Unit.METERS
    ),
    14: Parameter(
        id=14,
        name='Non-Convective Cloud Cover',
        abbrev='CDLYR',
        unit=Unit.PERCENT
    ),
    15: Parameter(
        id=15,
        name='Cloud Work Function',
        abbrev='CWORK',
        unit=Unit.JULES_PER_KG
    ),
    16: Parameter(
        id=16,
        name='Convective Cloud Efficiency',
        abbrev='CUEFI',
        unit=Unit.PROPORTION
    ),
    17: Parameter(
        id=17,
        name='Total Condensate * - Parameter deprecated',
        abbrev='TCONDO',
        unit=Unit.KG_PER_KG
    ),
    18: Parameter(
        id=18,
        name='Total Column-Integrated Cloud Water * - Parameter deprecated',
        abbrev='TCOLWO',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    19: Parameter(
        id=19,
        name='Total Column-Integrated Cloud Ice * - Parameter deprecated',
        abbrev='TCOLIO',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    20: Parameter(
        id=20,
        name='Total Column-Integrated Condensate * - Parameter deprecated',
        abbrev='TCOLC',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    21: Parameter(
        id=21,
        name='Ice fraction of total condensate',
        abbrev='FICE',
        unit=Unit.PROPORTION
    ),
    22: Parameter(
        id=22,
        name='Cloud Cover',
        abbrev='CDCC',
        unit=Unit.PERCENT
    ),
    23: Parameter(
        id=23,
        name='Cloud Ice Mixing Ratio * - Parameter deprecated',
        abbrev='CDCIMR',
        unit=Unit.KG_PER_KG
    ),
    24: Parameter(
        id=24,
        name='Sunshine',
        abbrev='SUNS',
        unit=Unit.NUMERIC
    ),
    25: Parameter(
        id=25,
        name='Horizontal Extent of Cumulonimbus (CB)',
        abbrev='CBHE',
        unit=Unit.PERCENT
    ),
    26: Parameter(
        id=26,
        name='Height of Convective Cloud Base',
        abbrev='HCONCB',
        unit=Unit.METERS
    ),
    27: Parameter(
        id=27,
        name='Height of Convective Cloud Top',
        abbrev='HCONCT',
        unit=Unit.METERS
    ),
    28: Parameter(
        id=28,
        name='Number Concentration of Cloud Droplets',
        abbrev='NCONCD',
        unit=Unit.PER_KG
    ),
    29: Parameter(
        id=29,
        name='Number Concentration of Cloud Ice',
        abbrev='NCCICE',
        unit=Unit.PER_KG
    ),
    30: Parameter(
        id=30,
        name='Number Density of Cloud Droplets',
        abbrev='NDENCD',
        unit=Unit.METERS_CUBED
    ),
    31: Parameter(
        id=31,
        name='Number Density of Cloud Ice',
        abbrev='NDCICE',
        unit=Unit.METERS_CUBED
    ),
    32: Parameter(
        id=32,
        name='Fraction of Cloud Cover',
        abbrev='FRACCC',
        unit=Unit.NUMERIC
    ),
    33: Parameter(
        id=33,
        name='Sunshine Duration',
        abbrev='SUNSD',
        unit=Unit.SECOND
    ),
    34: Parameter(
        id=34,
        name='Surface Long Wave Effective Total Cloudiness',
        abbrev='SLWTC',
        unit=Unit.NUMERIC
    ),
    35: Parameter(
        id=35,
        name='Surface Short Wave Effective Total Cloudiness',
        abbrev='SSWTC',
        unit=Unit.NUMERIC
    ),
    36: Parameter(
        id=36,
        name='Fraction of Stratiform Precipitation Cover',
        abbrev='FSTRPC',
        unit=Unit.PROPORTION
    ),
    37: Parameter(
        id=37,
        name='Fraction of Convective Precipitation Cover',
        abbrev='FCONPC',
        unit=Unit.PROPORTION
    ),
    38: Parameter(
        id=38,
        name='Mass Density of Cloud Droplets',
        abbrev='MASSDCD',
        unit=Unit.KG_PER_METER_CUBED
    ),
    39: Parameter(
        id=39,
        name='Mass Density of Cloud Ice',
        abbrev='MASSDCI',
        unit=Unit.KG_PER_METER_CUBED
    ),
    40: Parameter(
        id=40,
        name='Mass Density of Convective Cloud Water Droplets',
        abbrev='MDCCWD',
        unit=Unit.KG_PER_METER_CUBED
    ),
    47: Parameter(
        id=47,
        name='Volume Fraction of Cloud Water Droplets (see Note 2)',
        abbrev='VFRCWD',
        unit=Unit.NUMERIC
    ),
    48: Parameter(
        id=48,
        name='Volume Fraction of Cloud Ice Particles (see Note 2)',
        abbrev='VFRCICE',
        unit=Unit.NUMERIC
    ),
    49: Parameter(
        id=49,
        name='Volume Fraction of Cloud (Ice and/or Water) (see Note 2)',
        abbrev='VFRCIW',
        unit=Unit.NUMERIC
    ),
    50: Parameter(
        id=50,
        name='Fog (see Note 3)',
        abbrev='FOG',
        unit=Unit.PERCENT
    ),
    51: Parameter(
        id=51,
        name='Sunshine Duration Fraction (see Note 4)',
        abbrev='SUNFRAC',
        unit=Unit.PROPORTION
    ),

    192: Parameter(
        id=192,
        name='Non-Convective Cloud Cover',
        abbrev='CDLYR',
        unit=Unit.PERCENT
    ),
    193: Parameter(
        id=193,
        name='Cloud Work Function',
        abbrev='CWORK',
        unit=Unit.JULES_PER_KG
    ),
    194: Parameter(
        id=194,
        name='Convective Cloud Efficiency',
        abbrev='CUEFI',
        unit=Unit.NON_DIM
    ),
    195: Parameter(
        id=195,
        name='Total Condensate',
        abbrev='TCOND',
        unit=Unit.KG_PER_KG
    ),
    196: Parameter(
        id=196,
        name='Total Column-Integrated Cloud Water',
        abbrev='TCOLW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    197: Parameter(
        id=197,
        name='Total Column-Integrated Cloud Ice',
        abbrev='TCOLI',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    198: Parameter(
        id=198,
        name='Total Column-Integrated Condensate',
        abbrev='TCOLC',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    199: Parameter(
        id=199,
        name='Ice fraction of total condensate',
        abbrev='FICE',
        unit=Unit.NON_DIM
    ),
    200: Parameter(
        id=200,
        name='Convective Cloud Mass Flux',
        abbrev='MFLUX',
        unit=Unit.PASCAL_PER_SECOND
    ),
    201: Parameter(
        id=201,
        name='Sunshine Duration',
        abbrev='SUNSD',
        unit=Unit.SECOND
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
