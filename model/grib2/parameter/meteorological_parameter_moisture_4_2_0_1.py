from model.grib2.parameter import Parameter, Unit

meteorological_moisture = {
    0: Parameter(
        id=0,
        name='Specific Humidity',
        abbrev='SPFH',
        unit=Unit.KG_PER_KG
    ),
    1: Parameter(
        id=1,
        name='Relative Humidity',
        abbrev='RH',
        unit=Unit.PERCENT
    ),
    2: Parameter(
        id=2,
        name='Humidity Mixing Ratio',
        abbrev='MIXR',
        unit=Unit.KG_PER_KG
    ),
    3: Parameter(
        id=3,
        name='Precipitable Water',
        abbrev='PWAT',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    4: Parameter(
        id=4,
        name='Vapour Pressure',
        abbrev='VAPP',
        unit=Unit.PASCAL
    ),
    5: Parameter(
        id=5,
        name='Saturation Deficit',
        abbrev='SATD',
        unit=Unit.PASCAL
    ),
    6: Parameter(
        id=6,
        name='Evaporation',
        abbrev='EVP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    7: Parameter(
        id=7,
        name='Precipitation Rate (see Note 1)',
        abbrev='PRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    8: Parameter(
        id=8,
        name='Total Precipitation (see Note 3)',
        abbrev='APCP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    9: Parameter(
        id=9,
        name='Large-Scale Precipitation (non-convective) (see Note 3)',
        abbrev='NCPCP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    10: Parameter(
        id=10,
        name='Convective Precipitation (see Note 3)',
        abbrev='ACPCP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    11: Parameter(
        id=11,
        name='Snow Depth',
        abbrev='SNOD',
        unit=Unit.METERS
    ),
    12: Parameter(
        id=12,
        name='Snowfall Rate Water Equivalent (see Note 1)',
        abbrev='SRWEQ',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    13: Parameter(
        id=13,
        name='Water Equivalent of Accumulated Snow Depth (see Note 3)',
        abbrev='WEASD',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    14: Parameter(
        id=14,
        name='Convective Snow (see Note 3)',
        abbrev='SNOC',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    15: Parameter(
        id=15,
        name='Large-Scale Snow (see Note 3)',
        abbrev='SNOL',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    16: Parameter(
        id=16,
        name='Snow Melt (see Note 7)',
        abbrev='SNOM',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    17: Parameter(
        id=17,
        name='Snow Age',
        abbrev='SNOAG',
        unit=Unit.DAY
    ),
    18: Parameter(
        id=18,
        name='Absolute Humidity',
        abbrev='ABSH',
        unit=Unit.KG_PER_METER_CUBED
    ),
    19: Parameter(
        id=19,
        name='Precipitation Type',
        abbrev='PTYPE'
    ),
    20: Parameter(
        id=20,
        name='Integrated Liquid Water',
        abbrev='ILIQW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    21: Parameter(
        id=21,
        name='Condensate',
        abbrev='TCOND',
        unit=Unit.KG_PER_KG
    ),
    22: Parameter(
        id=22,
        name='Cloud Mixing Ratio',
        abbrev='CLMR',
        unit=Unit.KG_PER_KG
    ),
    23: Parameter(
        id=23,
        name='Ice Water Mixing Ratio',
        abbrev='ICMR',
        unit=Unit.KG_PER_KG
    ),
    24: Parameter(
        id=24,
        name='Rain Mixing Ratio',
        abbrev='RWMR',
        unit=Unit.KG_PER_KG
    ),
    25: Parameter(
        id=25,
        name='Snow Mixing Ratio',
        abbrev='SNMR',
        unit=Unit.KG_PER_KG
    ),
    26: Parameter(
        id=26,
        name='Horizontal Moisture Convergence',
        abbrev='MCONV',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    27: Parameter(
        id=27,
        name='Maximum Relative Humidity (see Note 1)',
        abbrev='MAXRH',
        unit=Unit.PERCENT
    ),
    28: Parameter(
        id=28,
        name='Maximum Absolute Humidity (see Note 1)',
        abbrev='MAXAH',
        unit=Unit.KG_PER_METER_CUBED
    ),
    29: Parameter(
        id=29,
        name='Total Snowfall (see Note 3)',
        abbrev='ASNOW',
        unit=Unit.METERS
    ),
    30: Parameter(
        id=30,
        name='Precipitable Water Category',
        abbrev='PWCAT'
    ),
    31: Parameter(
        id=31,
        name='Hail',
        abbrev='HAIL',
        unit=Unit.METERS
    ),
    32: Parameter(
        id=32,
        name='Graupel',
        abbrev='GRLE',
        unit=Unit.KG_PER_KG
    ),
    33: Parameter(
        id=33,
        name='Categorical Rain',
        abbrev='CRAIN'
    ),
    34: Parameter(
        id=34,
        name='Categorical Freezing Rain',
        abbrev='CFRZR'
    ),
    35: Parameter(
        id=35,
        name='Categorical Ice Pellets',
        abbrev='CICEP'
    ),
    36: Parameter(
        id=36,
        name='Categorical Snow',
        abbrev='CSNOW'
    ),
    37: Parameter(
        id=37,
        name='Convective Precipitation Rate',
        abbrev='CPRAT',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    38: Parameter(
        id=38,
        name='Horizontal Moisture Divergence',
        abbrev='MDIVER',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    39: Parameter(
        id=39,
        name='Percent frozen precipitation',
        abbrev='CPOFP',
        unit=Unit.PERCENT
    ),
    40: Parameter(
        id=40,
        name='Potential Evaporation',
        abbrev='PEVAP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    41: Parameter(
        id=41,
        name='Potential Evaporation Rate (see Note 4)',
        abbrev='PEVPR',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    42: Parameter(
        id=42,
        name='Snow Cover',
        abbrev='SNOWC',
        unit=Unit.PERCENT
    ),
    43: Parameter(
        id=43,
        name='Rain Fraction of Total Cloud Water',
        abbrev='FRAIN',
        unit=Unit.PROPORTION
    ),
    44: Parameter(
        id=44,
        name='Rime Factor',
        abbrev='RIME',
        unit=Unit.NUMERIC
    ),
    45: Parameter(
        id=45,
        name='Total Column Integrated Rain',
        abbrev='TCOLR',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    46: Parameter(
        id=46,
        name='Total Column Integrated Snow',
        abbrev='TCOLS',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    47: Parameter(
        id=47,
        name='Large Scale Water Precipitation (Non-Convective) (see Note 3)',
        abbrev='LSWP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    48: Parameter(
        id=48,
        name='Convective Water Precipitation (see Note 3)',
        abbrev='CWP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    49: Parameter(
        id=49,
        name='Total Water Precipitation (see Note 3)',
        abbrev='TWATP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    50: Parameter(
        id=50,
        name='Total Snow Precipitation (see Note 3)',
        abbrev='TSNOWP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    51: Parameter(
        id=51,
        name='Total Column Water(Vertically integrated total water (vapour+cloud water/ice)',
        abbrev='TCWAT',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    52: Parameter(
        id=52,
        name='Total Precipitation Rate (see Note 2)',
        abbrev='TPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    53: Parameter(
        id=53,
        name='Total Snowfall Rate Water Equivalent (see Note 2)',
        abbrev='TSRWE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    54: Parameter(
        id=54,
        name='Large Scale Precipitation Rate',
        abbrev='LSPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    55: Parameter(
        id=55,
        name='Convective Snowfall Rate Water Equivalent',
        abbrev='CSRWE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    56: Parameter(
        id=56,
        name='Large Scale Snowfall Rate Water Equivalent',
        abbrev='LSSRWE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    57: Parameter(
        id=57,
        name='Total Snowfall Rate',
        abbrev='TSRATE',
        unit=Unit.METERS_PER_SECOND
    ),
    58: Parameter(
        id=58,
        name='Convective Snowfall Rate',
        abbrev='CSRATE',
        unit=Unit.METERS_PER_SECOND
    ),
    59: Parameter(
        id=59,
        name='Large Scale Snowfall Rate',
        abbrev='LSSRATE',
        unit=Unit.METERS_PER_SECOND
    ),
    60: Parameter(
        id=60,
        name='Snow Depth Water Equivalent',
        abbrev='SDWE',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    61: Parameter(
        id=61,
        name='Snow Density',
        abbrev='SDEN',
        unit=Unit.KG_PER_METER_CUBED
    ),
    62: Parameter(
        id=62,
        name='Snow Evaporation (see Note 8)',
        abbrev='SEVAP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    64: Parameter(
        id=64,
        name='Total Column Integrated Water Vapour',
        abbrev='TCIWV',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    65: Parameter(
        id=65,
        name='Rain Precipitation Rate',
        abbrev='RPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    66: Parameter(
        id=66,
        name='Snow Precipitation Rate',
        abbrev='SPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    67: Parameter(
        id=67,
        name='Freezing Rain Precipitation Rate',
        abbrev='FPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    68: Parameter(
        id=68,
        name='Ice Pellets Precipitation Rate',
        abbrev='IPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    69: Parameter(
        id=69,
        name='Total Column Integrate Cloud Water',
        abbrev='TCOLW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    70: Parameter(
        id=70,
        name='Total Column Integrate Cloud Ice',
        abbrev='TCOLI',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    71: Parameter(
        id=71,
        name='Hail Mixing Ratio',
        abbrev='HAILMXR',
        unit=Unit.KG_PER_KG
    ),
    72: Parameter(
        id=72,
        name='Total Column Integrate Hail',
        abbrev='TCOLH',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    73: Parameter(
        id=73,
        name='Hail Prepitation Rate',
        abbrev='HAILPR',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    74: Parameter(
        id=74,
        name='Total Column Integrate Graupel',
        abbrev='TCOLG',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    75: Parameter(
        id=75,
        name='Graupel (Snow Pellets) Prepitation Rate',
        abbrev='GPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    76: Parameter(
        id=76,
        name='Convective Rain Rate',
        abbrev='CRRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    77: Parameter(
        id=77,
        name='Large Scale Rain Rate',
        abbrev='LSRRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    78: Parameter(
        id=78,
        name='Total Column Integrate Water (Allcomponents including precipitation)',
        abbrev='TCOLWA',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    79: Parameter(
        id=79,
        name='Evaporation Rate',
        abbrev='EVARATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    80: Parameter(
        id=80,
        name='Total Condensate',
        abbrev='TOTCON',
        unit=Unit.KG_PER_KG
    ),
    81: Parameter(
        id=81,
        name='Total Column-Integrate Condensate',
        abbrev='TCICON',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    82: Parameter(
        id=82,
        name='Cloud Ice Mixing Ratio',
        abbrev='CIMIXR',
        unit=Unit.KG_PER_KG
    ),
    83: Parameter(
        id=83,
        name='Specific Cloud Liquid Water Content',
        abbrev='SCLLWC',
        unit=Unit.KG_PER_KG
    ),
    84: Parameter(
        id=84,
        name='Specific Cloud Ice Water Content',
        abbrev='SCLIWC',
        unit=Unit.KG_PER_KG
    ),
    85: Parameter(
        id=85,
        name='Specific Rain Water Content',
        abbrev='SRAINW',
        unit=Unit.KG_PER_KG
    ),
    86: Parameter(
        id=86,
        name='Specific Snow Water Content',
        abbrev='SSNOWW',
        unit=Unit.KG_PER_KG
    ),
    87: Parameter(
        id=87,
        name='Stratiform Precipitation Rate',
        abbrev='STRPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    88: Parameter(
        id=88,
        name='Categorical Convective Precipitation',
        abbrev='CATCP',
    ),
    90: Parameter(
        id=90,
        name='Total Kinematic Moisture Flux',
        abbrev='TKMFLX',
    ),
    91: Parameter(
        id=91,
        name='U-component (zonal) Kinematic Moisture Flux',
        abbrev='UKMFLX',
        unit=Unit.KG_PER_KG_PER_METER_PER_SECOND
    ),
    92: Parameter(
        id=92,
        name='V-component (meridional) Kinematic Moisture Flux',
        abbrev='VKMFLX',
        unit=Unit.KG_PER_KG_PER_METER_PER_SECOND
    ),
    93: Parameter(
        id=93,
        name='Relative Humidity With Respect to Water',
        abbrev='RHWATER',
        unit=Unit.PERCENT
    ),
    94: Parameter(
        id=94,
        name='Relative Humidity With Respect to Ice',
        abbrev='RHICE',
        unit=Unit.PERCENT
    ),
    95: Parameter(
        id=95,
        name='Freezing or Frozen Precipitation Rate',
        abbrev='FZPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    96: Parameter(
        id=96,
        name='Mass Density of Rain',
        abbrev='MASSDR',
        unit=Unit.KG_PER_METER_CUBED
    ),
    97: Parameter(
        id=97,
        name='Mass Density of Snow',
        abbrev='MASSDS',
        unit=Unit.KG_PER_METER_CUBED
    ),
    98: Parameter(
        id=98,
        name='Mass Density of Graupel',
        abbrev='MASSDG',
        unit=Unit.KG_PER_METER_CUBED
    ),
    99: Parameter(
        id=99,
        name='Mass Density of Hail',
        abbrev='MASSDH',
        unit=Unit.KG_PER_METER_CUBED
    ),
    100: Parameter(
        id=100,
        name='Specific Number Concentration of Rain',
        abbrev='SPNCR',
        unit=Unit.PER_KG
    ),
    101: Parameter(
        id=101,
        name='Specific Number Concentration of Snow',
        abbrev='SPNCS',
        unit=Unit.PER_KG
    ),
    102: Parameter(
        id=102,
        name='Specific Number Concentration of Graupel',
        abbrev='SPNCG',
        unit=Unit.PER_KG
    ),
    103: Parameter(
        id=103,
        name='Specific Number Concentration of Hail',
        abbrev='SPNCH',
        unit=Unit.PER_KG
    ),
    104: Parameter(
        id=104,
        name='Number Density of Rain',
        abbrev='NUMDR',
        unit=Unit.METERS_CUBED
    ),
    105: Parameter(
        id=105,
        name='Number Density of Snow',
        abbrev='NUMDS',
        unit=Unit.METERS_CUBED
    ),
    106: Parameter(
        id=106,
        name='Number Density of Graupel',
        abbrev='NUMDG',
        unit=Unit.METERS_CUBED
    ),
    107: Parameter(
        id=107,
        name='Number Density of Hail',
        abbrev='NUMDH',
        unit=Unit.METERS_CUBED
    ),
    108: Parameter(
        id=108,
        name='Specific Humidity Tendency due to Parameterizations',
        abbrev='SHTPRM',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    109: Parameter(
        id=109,
        name='Mass Density of Liquid Water Coating on Hail Expressed as Mass of Liquid Water per Unit Volume of Air',
        abbrev='MDLWHVA',
        unit=Unit.KG_PER_METER_CUBED
    ),
    110: Parameter(
        id=110,
        name='Specific Mass of Liquid Water Coating on Hail Expressed as Mass of Liquid Water per Unit Mass of Moist Air',
        abbrev='SMLWHMA',
        unit=Unit.KG_PER_KG
    ),
    111: Parameter(
        id=111,
        name='Mass Mixing Ratio of Liquid Water Coating on Hail Expressed as Mass of Liquid Water per Unit Mass of Dry Air',
        abbrev='MMLWHDA',
        unit=Unit.KG_PER_KG
    ),
    112: Parameter(
        id=112,
        name='Mass Density of Liquid Water Coating on Graupel Expressed as Mass of Liquid Water per Unit Volume of Air',
        abbrev='MDLWGVA',
        unit=Unit.KG_PER_METER_CUBED
    ),
    113: Parameter(
        id=113,
        name='Specific Mass of Liquid Water Coating on Graupel Expressed as Mass of Liquid Water per Unit Mass of Moist Air',
        abbrev='SMLWGMA',
        unit=Unit.KG_PER_KG
    ),
    114: Parameter(
        id=114,
        name='Mass Mixing Ratio of Liquid Water Coating on Graupel Expressed as Mass of Liquid Water per Unit Mass of Dry Air',
        abbrev='MMLWGDA',
        unit=Unit.KG_PER_KG
    ),
    115: Parameter(
        id=115,
        name='Mass Density of Liquid Water Coating on Snow Expressed as Mass of Liquid Water per Unit Volume of Air',
        abbrev='MDLWSVA',
        unit=Unit.KG_PER_METER_CUBED
    ),
    116: Parameter(
        id=116,
        name='Specific Mass of Liquid Water Coating on Snow Expressed as Mass of Liquid Water per Unit Mass of Moist Air',
        abbrev='SMLWSMA',
        unit=Unit.KG_PER_KG
    ),
    117: Parameter(
        id=117,
        name='Mass Mixing Ratio of Liquid Water Coating on Snow Expressed as Mass of Liquid Water per Unit Mass of Dry Air',
        abbrev='MMLWSDA',
        unit=Unit.KG_PER_KG
    ),
    118: Parameter(
        id=118,
        name='Unbalanced Component of Specific Humidity',
        abbrev='UNCSH',
        unit=Unit.KG_PER_KG
    ),
    119: Parameter(
        id=119,
        name='Unbalanced Component of Specific Cloud Liquid Water content',
        abbrev='UCSCLW',
        unit=Unit.KG_PER_KG
    ),
    120: Parameter(
        id=120,
        name='Unbalanced Component of Specific Cloud Ice Water content',
        abbrev='UCSCIW',
        unit=Unit.KG_PER_KG
    ),
    121: Parameter(
        id=121,
        name='Fraction of Snow Cover',
        abbrev='FSNOWC',
        unit=Unit.PROPORTION
    ),
    122: Parameter(
        id=122,
        name='Precipitation intensity index',
        abbrev='PIIDX'
    ),
    123: Parameter(
        id=123,
        name='Dominant precipitation type',
        abbrev='DPTYPE'
    ),
    124: Parameter(
        id=124,
        name='Presence of showers',
        abbrev='PSHOW'
    ),
    125: Parameter(
        id=125,
        name='Presence of blowing snow',
        abbrev='PBSNOW'
    ),
    126: Parameter(
        id=126,
        name='Presence of blizzard',
        abbrev='PBLIZZ'
    ),
    127: Parameter(
        id=127,
        name='Ice pellets (non-water equivalent) precipitation rate',
        abbrev='ICEP',
        unit=Unit.METERS_PER_SECOND
    ),
    128: Parameter(
        id=128,
        name='Total solid precipitation rate (see Note 5)',
        abbrev='TSPRATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    129: Parameter(
        id=129,
        name='Effective Radius of Cloud Water',
        abbrev='EFRCWAT',
        unit=Unit.METERS
    ),
    130: Parameter(
        id=130,
        name='Effective Radius of Rain',
        abbrev='EFRRAIN',
        unit=Unit.METERS
    ),
    131: Parameter(
        id=131,
        name='Effective Radius of Cloud Ice',
        abbrev='EFRCICE',
        unit=Unit.METERS
    ),
    132: Parameter(
        id=132,
        name='Effective Radius of Snow',
        abbrev='EFRSNOW',
        unit=Unit.METERS
    ),
    133: Parameter(
        id=133,
        name='Effective Radius of Graupel',
        abbrev='EFRGRL',
        unit=Unit.METERS
    ),
    134: Parameter(
        id=134,
        name='Effective Radius of Hail',
        abbrev='EFRHAIL',
        unit=Unit.METERS
    ),
    135: Parameter(
        id=135,
        name='Effective Radius of Subgrid Liquid Clouds',
        abbrev='EFRSLC',
        unit=Unit.METERS
    ),
    136: Parameter(
        id=136,
        name='Effective Radius of Subgrid Ice Clouds',
        abbrev='EFRSICEC',
        unit=Unit.METERS
    ),
    137: Parameter(
        id=137,
        name='Effective Aspect Ratio of Rain',
        abbrev='EFARRAIN'
    ),
    138: Parameter(
        id=138,
        name='Effective Aspect Ratio of Cloud Ice',
        abbrev='EFARCICE'
    ),
    139: Parameter(
        id=139,
        name='Effective Aspect Ratio of Snow',
        abbrev='EFARSNOW'
    ),
    140: Parameter(
        id=140,
        name='Effective Aspect Ratio of Graupel',
        abbrev='EFARGRL'
    ),
    141: Parameter(
        id=141,
        name='Effective Aspect Ratio of Hail',
        abbrev='EFARHAIL'
    ),
    142: Parameter(
        id=142,
        name='Effective Aspect Ratio of Subgrid Ice Clouds',
        abbrev='EFARSIC'
    ),
    143: Parameter(
        id=143,
        name='Potential evaporation rate',
        abbrev='PERATE',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    144: Parameter(
        id=144,
        name='Specific rain water content (convective)',
        abbrev='SRWATERC',
        unit=Unit.KG_PER_KG
    ),
    145: Parameter(
        id=145,
        name='Specific snow water content (convective)',
        abbrev='SSNOWWC',
        unit=Unit.KG_PER_KG
    ),
    146: Parameter(
        id=146,
        name='Cloud ice precipitation rate (see Note 6)',
        abbrev='CICEPR',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    147: Parameter(
        id=147,
        name='Character of precipitation',
        abbrev='CHPRECIP'
    ),
    148: Parameter(
        id=148,
        name='Snow evaporation rate (see Note 9)',
        abbrev='SNOWERAT',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    149: Parameter(
        id=149,
        name='Cloud water mixing ratio',
        abbrev='CWATERMR',
        unit=Unit.KG_PER_KG
    ),
    150: Parameter(
        id=150,
        name='Column integrated eastward water vapour mass flux',
        abbrev='CEWVMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    151: Parameter(
        id=151,
        name='Column integrated northward water vapour mass flux',
        abbrev='CNWVMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    152: Parameter(
        id=152,
        name='Column integrated eastward cloud liquid water mass flux',
        abbrev='CECLWMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    153: Parameter(
        id=153,
        name='Column integrated northward cloud liquid water mass flux',
        abbrev='CNCLWMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    154: Parameter(
        id=154,
        name='Column integrated eastward cloud ice mass flux',
        abbrev='CECIMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    155: Parameter(
        id=155,
        name='Column integrated northward cloud ice mass flux',
        abbrev='CNCIMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    156: Parameter(
        id=156,
        name='Column integrated eastward rain mass flux',
        abbrev='CERMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    157: Parameter(
        id=157,
        name='Column integrated northward rain mass flux',
        abbrev='CNRMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    158: Parameter(
        id=158,
        name='Column integrated eastward snow mass flux',
        abbrev='CEFMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    159: Parameter(
        id=159,
        name='Column integrated northward snow mass flux',
        abbrev='CNSMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    160: Parameter(
        id=160,
        name='Column integrated divergence of water vapour mass flux',
        abbrev='CDWFMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    161: Parameter(
        id=161,
        name='Column integrated divergence of cloud liquid water mass flux',
        abbrev='CDCLWMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    162: Parameter(
        id=162,
        name='Column integrated divergence of cloud ice mass flux',
        abbrev='CDCIMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    163: Parameter(
        id=163,
        name='Column integrated divergence of rain mass flux',
        abbrev='CDRMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    164: Parameter(
        id=164,
        name='Column integrated divergence of snow mass flux',
        abbrev='CDSMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    165: Parameter(
        id=165,
        name='Column integrated divergence of total water mass flux',
        abbrev='CDTWMF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    166: Parameter(
        id=166,
        name='Column integrated water vapour flux',
        abbrev='CWVF',
        unit=Unit.KG_PER_METER_PER_SECOND
    ),
    167: Parameter(
        id=167,
        name='Total column supercooled liquid water',
        abbrev='TCSLW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    168: Parameter(
        id=168,
        name='Saturation specific humidity with respect to water',
        abbrev='SSPFHW',
        unit=Unit.KG_PER_METER_CUBED
    ),
    169: Parameter(
        id=169,
        name='Total column integrated saturation specific humidity with respect to water',
        abbrev='TCISSPFHW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    192: Parameter(
        id=192,
        name='Categorical Rain',
        abbrev='CRAIN',
    ),
    193: Parameter(
        id=193,
        name='Categorical Freezing Rain',
        abbrev='CFRZR',
    ),
    194: Parameter(
        id=194,
        name='Categorical Ice Pellets',
        abbrev='CICEP',
    ),
    195: Parameter(
        id=195,
        name='Categorical Snow',
        abbrev='CSNOW',
    ),
    196: Parameter(
        id=196,
        name='Convective Precipitation Rate',
        abbrev='CPRAT',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    197: Parameter(
        id=197,
        name='Horizontal Moisture Divergence',
        abbrev='MDIV',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    198: Parameter(
        id=198,
        name='Minimum Relative Humidity',
        abbrev='MINRH',
        unit=Unit.PERCENT
    ),
    199: Parameter(
        id=199,
        name='Potential Evaporation',
        abbrev='PEVAP',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    200: Parameter(
        id=200,
        name='Potential Evaporation Rate',
        abbrev='PEVPR',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    201: Parameter(
        id=201,
        name='Snow Cover',
        abbrev='SNOWC',
        unit=Unit.PERCENT
    ),
    202: Parameter(
        id=202,
        name='Rain Fraction of Total Liquid Water',
        abbrev='FRAIN',
        unit=Unit.NON_DIM
    ),
    203: Parameter(
        id=203,
        name='Rime Factor',
        abbrev='RIME',
        unit=Unit.NON_DIM
    ),
    204: Parameter(
        id=204,
        name='Total Column Integrated Rain',
        abbrev='TCOLR',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    205: Parameter(
        id=205,
        name='Total Column Integrated Snow',
        abbrev='TCOLS',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    206: Parameter(
        id=206,
        name='Total Icing Potential Diagnostic',
        abbrev='TIPD',
        unit=Unit.NON_DIM
    ),
    207: Parameter(
        id=207,
        name='Number concentration for ice particles',
        abbrev='NCIP',
        unit=Unit.NON_DIM
    ),
    208: Parameter(
        id=208,
        name='Snow temperature',
        abbrev='SNOT',
        unit=Unit.KELVIN
    ),
    209: Parameter(
        id=209,
        name='Total column-integrated supercooled liquid water',
        abbrev='TCLSW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    210: Parameter(
        id=210,
        name='Total column-integrated melting ice',
        abbrev='TCOLM',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    211: Parameter(
        id=211,
        name='Evaporation - Precipitation',
        abbrev='EMNP',
        unit=Unit.CM_PER_DAY
    ),
    212: Parameter(
        id=212,
        name='Sublimation (evaporation from snow)',
        abbrev='SBSNO',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    213: Parameter(
        id=213,
        name='Deep Convective Moistening Rate',
        abbrev='CNVMR',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    214: Parameter(
        id=214,
        name='Shallow Convective Moistening Rate',
        abbrev='SHAMR',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    215: Parameter(
        id=215,
        name='Vertical Diffusion Moistening Rate',
        abbrev='VDFMR',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    216: Parameter(
        id=216,
        name='Condensation Pressure of ParcaliLifted From Indicate Surface',
        abbrev='CONDP',
        unit=Unit.PASCAL
    ),
    217: Parameter(
        id=217,
        name='Large scale moistening rate',
        abbrev='LRGMR',
        unit=Unit.KG_PER_KG_PER_SECOND
    ),
    218: Parameter(
        id=218,
        name='Specific humidity at top of viscous sublayer',
        abbrev='QZ0',
        unit=Unit.KG_PER_KG
    ),
    219: Parameter(
        id=219,
        name='Maximum specific humidity at 2m',
        abbrev='QMAX',
        unit=Unit.KG_PER_KG
    ),
    220: Parameter(
        id=220,
        name='Minimum specific humidity at 2m',
        abbrev='QMIN',
        unit=Unit.KG_PER_KG
    ),
    221: Parameter(
        id=221,
        name='Liquid precipitation (Rainfall)',
        abbrev='ARAIN',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    222: Parameter(
        id=222,
        name='Snow temperature, depth-avg',
        abbrev='SNOWT',
        unit=Unit.KELVIN
    ),
    223: Parameter(
        id=223,
        name='Total precipitation (nearest grid point)',
        abbrev='APCPN',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    224: Parameter(
        id=224,
        name='Convective precipitation (nearest grid point)',
        abbrev='ACPCPN',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    225: Parameter(
        id=225,
        name='Freezing Rain',
        abbrev='FRZR',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    226: Parameter(
        id=226,
        name='Pblackominant Weather (see Local Use Note A)',
        abbrev='PWTHER',
        unit=Unit.NUMERIC
    ),
    227: Parameter(
        id=227,
        name='Frozen Rain',
        abbrev='FROZR',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    228: Parameter(
        id=228,
        name='Flat Ice Accumulation (FRAM)',
        abbrev='FICEAC',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    229: Parameter(
        id=229,
        name='Line Ice Accumulation (FRAM)',
        abbrev='LICEAC',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    230: Parameter(
        id=230,
        name='Sleet Accumulation',
        abbrev='SLACC',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    231: Parameter(
        id=231,
        name='Precipitation Potential Index',
        abbrev='PPINDX',
        unit=Unit.PERCENT
    ),
    232: Parameter(
        id=232,
        name='Probability Cloud Ice Present',
        abbrev='PROBCIP',
        unit=Unit.PERCENT
    ),
    233: Parameter(
        id=233,
        name='Snow Liquid ratio',
        abbrev='SNOWLR',
        unit=Unit.KG_PER_KG
    ),
    234: Parameter(
        id=234,
        name='Precipitation Duration',
        abbrev='PCPDUR',
        unit=Unit.HOUR
    ),
    235: Parameter(
        id=235,
        name='Cloud Liquid Mixing Ratio',
        abbrev='CLLMR',
        unit=Unit.KG_PER_KG
    ),
    241: Parameter(
        id=241,
        name='Total Snow',
        abbrev='TSNOW',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    242: Parameter(
        id=242,
        name='Relative Humidity with Respect to Precipitable Water',
        abbrev='RHPW',
        unit=Unit.PERCENT
    ),
    245: Parameter(
        id=245,
        name='Hourly Maximum of Column Vertical Integrated Graupel on Entire Atmosphere',
        abbrev='MAXVIG',
        unit=Unit.KG_PER_SQUARE_METER
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
