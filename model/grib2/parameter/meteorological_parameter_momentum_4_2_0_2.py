from model.grib2.parameter import Parameter, Unit

meteorological_momentum = {
    0: Parameter(
        id=0,
        name='Wind Direction (from which blowing)',
        abbrev='WDIR',
        unit=Unit.DEGREE
    ),
    1: Parameter(
        id=1,
        name='Wind Speed',
        abbrev='WIND',
        unit=Unit.METERS_PER_SECOND
    ),
    2: Parameter(
        id=2,
        name='U-Component of Wind',
        abbrev='UGRD',
        unit=Unit.METERS_PER_SECOND
    ),
    3: Parameter(
        id=3,
        name='V-Component of Wind',
        abbrev='VGRD',
        unit=Unit.METERS_PER_SECOND
    ),
    4: Parameter(
        id=4,
        name='Stream Function',
        abbrev='STRM',
        unit=Unit.SQUARE_METERS_PER_SECOND
    ),
    5: Parameter(
        id=5,
        name='Velocity Potential',
        abbrev='VPOT',
        unit=Unit.SQUARE_METERS_PER_SECOND
    ),
    6: Parameter(
        id=6,
        name='Montgomery Stream Function',
        abbrev='MNTSF',
        unit=Unit.SQUARE_METERS_PER_SECOND_SQUARED
    ),
    7: Parameter(
        id=7,
        name='Sigma Coordinate Vertical Velocity',
        abbrev='SGCVV',
        unit=Unit.PER_SECOND
    ),
    8: Parameter(
        id=8,
        name='Vertical Velocity (Pressure)',
        abbrev='VVEL',
        unit=Unit.PASCAL_PER_SECOND
    ),
    9: Parameter(
        id=9,
        name='Vertical Velocity (Geometric)',
        abbrev='DZDT',
        unit=Unit.METERS_PER_SECOND
    ),
    10: Parameter(
        id=10,
        name='Absolute Vorticity',
        abbrev='ABSV',
        unit=Unit.PER_SECOND
    ),
    11: Parameter(
        id=11,
        name='Absolute Divergence',
        abbrev='ABSD',
        unit=Unit.PER_SECOND
    ),
    12: Parameter(
        id=12,
        name='Relative Vorticity',
        abbrev='RELV',
        unit=Unit.PER_SECOND
    ),
    13: Parameter(
        id=13,
        name='Relative Divergence',
        abbrev='RELD',
        unit=Unit.PER_SECOND
    ),
    14: Parameter(
        id=14,
        name='Potential Vorticity',
        abbrev='PVORT',
        unit=Unit.KELVIN_PER_METER_SQUARED_PER_KG_PER_SECOND
    ),
    15: Parameter(
        id=15,
        name='Vertical U-Component Shear',
        abbrev='VUCSH',
        unit=Unit.PER_SECOND
    ),
    16: Parameter(
        id=16,
        name='Vertical V-Component Shear',
        abbrev='VVCSH',
        unit=Unit.PER_SECOND
    ),
    17: Parameter(
        id=17,
        name='Momentum Flux, U-Component',
        abbrev='UFLX',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    18: Parameter(
        id=18,
        name='Momentum Flux, V-Component',
        abbrev='VFLX',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    19: Parameter(
        id=19,
        name='Wind Mixing Energy',
        abbrev='WMIXE',
        unit=Unit.JULES
    ),
    20: Parameter(
        id=20,
        name='Boundary Layer Dissipation',
        abbrev='BLYDP',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    21: Parameter(
        id=21,
        name='Maximum Wind Speed',
        abbrev='MAXGUST',
        unit=Unit.METERS_PER_SECOND,
        deprecated=True
    ),
    22: Parameter(
        id=22,
        name='Wind Speed (Gust)',
        abbrev='GUST',
        unit=Unit.METERS_PER_SECOND
    ),
    23: Parameter(
        id=23,
        name='U-Component of Wind (Gust)',
        abbrev='UGUST',
        unit=Unit.METERS_PER_SECOND
    ),
    24: Parameter(
        id=24,
        name='V-Component of Wind (Gust)',
        abbrev='VGUST',
        unit=Unit.METERS_PER_SECOND
    ),
    25: Parameter(
        id=25,
        name='Vertical Speed Shear',
        abbrev='VWSH',
        unit=Unit.PER_SECOND
    ),
    26: Parameter(
        id=26,
        name='Horizontal Momentum Flux',
        abbrev='MFLX',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    27: Parameter(
        id=27,
        name='U-Component Storm Motion',
        abbrev='USTM',
        unit=Unit.METERS_PER_SECOND
    ),
    28: Parameter(
        id=28,
        name='V-Component Storm Motion',
        abbrev='VSTM',
        unit=Unit.METERS_PER_SECOND
    ),
    29: Parameter(
        id=29,
        name='Drag Coefficient',
        abbrev='CD',
        unit=Unit.NUMERIC
    ),
    30: Parameter(
        id=30,
        name='Frictional Velocity',
        abbrev='FRICV',
        unit=Unit.METERS_PER_SECOND
    ),
    31: Parameter(
        id=31,
        name='Turbulent Diffusion Coefficient for Momentum',
        abbrev='TDCMOM',
        unit=Unit.SQUARE_METERS_PER_SECOND
    ),
    32: Parameter(
        id=32,
        name='Eta Coordinate Vertical Velocity',
        abbrev='ETACVV',
        unit=Unit.PER_SECOND
    ),
    33: Parameter(
        id=33,
        name='Wind Fetch',
        abbrev='WINDF',
        unit=Unit.METERS
    ),
    34: Parameter(
        id=34,
        name='Normal Wind Component',
        abbrev='NWIND',
        unit=Unit.METERS_PER_SECOND
    ),
    35: Parameter(
        id=35,
        name='Tangential Wind Component',
        abbrev='TWIND',
        unit=Unit.METERS_PER_SECOND
    ),
    36: Parameter(
        id=36,
        name='Amplitude Function for Rossby Wave Envelope for Meridional Wind',
        abbrev='AFRWE',
        unit=Unit.METERS_PER_SECOND
    ),
    37: Parameter(
        id=37,
        name='Northward Turbulent Surface Stress',
        abbrev='NTSS',
        unit=Unit.NEWTONS_PER_METER_SQUARED_PER_SECOND
    ),
    38: Parameter(
        id=38,
        name='Eastward Turbulent Surface Stress',
        abbrev='ETSS',
        unit=Unit.NEWTONS_PER_METER_SQUARED_PER_SECOND
    ),
    39: Parameter(
        id=39,
        name='Eastward Wind Tendency Due to Parameterizations',
        abbrev='EWTPARM',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    40: Parameter(
        id=40,
        name='Northward Wind Tendency Due to Parameterizations',
        abbrev='NWTPARM',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    41: Parameter(
        id=41,
        name='U-Component of Geostrophic Wind',
        abbrev='UGWIND',
        unit=Unit.METERS_PER_SECOND
    ),
    42: Parameter(
        id=42,
        name='V-Component of Geostrophic Wind',
        abbrev='VGWIND',
        unit=Unit.METERS_PER_SECOND
    ),
    43: Parameter(
        id=43,
        name='Geostrophic Wind Direction',
        abbrev='GEOWD',
        unit=Unit.DEGREE
    ),
    44: Parameter(
        id=44,
        name='Geostrophic Wind Speed',
        abbrev='GEOWS',
        unit=Unit.METERS_PER_SECOND
    ),
    45: Parameter(
        id=45,
        name='Unbalanced Component of Divergence',
        abbrev='UNDIV',
        unit=Unit.PER_SECOND
    ),
    46: Parameter(
        id=46,
        name='Vorticity Advection',
        abbrev='VORTADV',
        unit=Unit.SECONDS_SQUARED
    ),
    47: Parameter(
        id=47,
        name='Surface roughness for heat',
        abbrev='SFRHEAT',
        unit=Unit.METERS
    ),
    48: Parameter(
        id=48,
        name='Surface roughness for moisture',
        abbrev='SFRMOIST',
        unit=Unit.METERS
    ),
    49: Parameter(
        id=49,
        name='Wind stress',
        abbrev='WINDSTR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    50: Parameter(
        id=50,
        name='Eastward wind stress',
        abbrev='EWINDSTR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    51: Parameter(
        id=51,
        name='Northward wind stress',
        abbrev='NWINDSTR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    52: Parameter(
        id=52,
        name='u-component of wind stress',
        abbrev='UWINDSTR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    53: Parameter(
        id=53,
        name='v-component of wind stress',
        abbrev='VWINDSTR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    54: Parameter(
        id=54,
        name='Natural logarithm of surface roughness length for heat',
        abbrev='NLSRLH',
        unit=Unit.METERS
    ),
    55: Parameter(
        id=55,
        name='Natural logarithm of surface roughness length for moisture',
        abbrev='NLSRLM',
        unit=Unit.METERS
    ),
    56: Parameter(
        id=56,
        name='u-component of neutral wind',
        abbrev='UNWIND',
        unit=Unit.METERS_PER_SECOND
    ),
    57: Parameter(
        id=57,
        name='v-component of neutral wind',
        abbrev='VNWIND',
        unit=Unit.METERS_PER_SECOND
    ),
    58: Parameter(
        id=58,
        name='Magnitude of turbulent surface stress',
        abbrev='TSFCSTR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    59: Parameter(
        id=59,
        name='Vertical divergence',
        abbrev='VDIV',
        unit=Unit.PER_SECOND
    ),
    60: Parameter(
        id=60,
        name='Drag thermal coefficient',
        abbrev='DTC',
        unit=Unit.NUMERIC
    ),
    61: Parameter(
        id=61,
        name='Drag evaporation coefficient',
        abbrev='DEC',
        unit=Unit.NUMERIC
    ),
    62: Parameter(
        id=62,
        name='Eastward turbulent surface stress',
        abbrev='EASTTSS',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    63: Parameter(
        id=63,
        name='Northward turbulent surface stress',
        abbrev='NRTHTSS',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    64: Parameter(
        id=64,
        name='Eastward turbulent surface stress due to orographic form drag',
        abbrev='EASTTSSOD',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    65: Parameter(
        id=65,
        name='Northward turbulent surface stress due to orographic form drag',
        abbrev='NRTHTSSOD',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    66: Parameter(
        id=66,
        name='Eastward turbulent surface stress due to surface roughness',
        abbrev='EASTTSSSR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    67: Parameter(
        id=67,
        name='Northward turbulent surface stress due to surface roughness',
        abbrev='NRTHTSSSR',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    192: Parameter(
        id=192,
        name='Vertical Speed Shear',
        abbrev='VWSH',
        unit=Unit.PER_SECOND
    ),
    193: Parameter(
        id=193,
        name='Horizontal Momentum Flux',
        abbrev='MFLX',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    194: Parameter(
        id=194,
        name='U-Component Storm Motion',
        abbrev='USTM',
        unit=Unit.METERS_PER_SECOND
    ),
    195: Parameter(
        id=195,
        name='V-Component Storm Motion',
        abbrev='VSTM',
        unit=Unit.METERS_PER_SECOND
    ),
    196: Parameter(
        id=196,
        name='Drag Coefficient',
        abbrev='CD',
        unit=Unit.NON_DIM
    ),
    197: Parameter(
        id=197,
        name='Frictional Velocity',
        abbrev='FRICV',
        unit=Unit.METERS_PER_SECOND
    ),
    198: Parameter(
        id=198,
        name='Latitude of U Wind Component of Velocity',
        abbrev='LAUV',
        unit=Unit.DEGREE
    ),
    199: Parameter(
        id=199,
        name='Longitude of U Wind Component of Velocity',
        abbrev='LOUV',
        unit=Unit.DEGREE
    ),
    200: Parameter(
        id=200,
        name='Latitude of V Wind Component of Velocity',
        abbrev='LAVV',
        unit=Unit.DEGREE
    ),
    201: Parameter(
        id=201,
        name='Longitude of V Wind Component of Velocity',
        abbrev='LOVV',
        unit=Unit.DEGREE
    ),
    202: Parameter(
        id=202,
        name='Latitude of Presure Point',
        abbrev='LAPP',
        unit=Unit.DEGREE
    ),
    203: Parameter(
        id=203,
        name='Longitude of Presure Point',
        abbrev='LOPP',
        unit=Unit.DEGREE
    ),
    204: Parameter(
        id=204,
        name='Vertical Eddy Diffusivity Heat exchange',
        abbrev='VEDH',
        unit=Unit.SQUARE_METERS_PER_SECOND
    ),
    205: Parameter(
        id=205,
        name='Covariance between Meridional and Zonal, Components of the wind.',
        abbrev='COVMZ',
        unit=Unit.SQUARE_METERS_PER_SECOND_SQUARED
    ),
    206: Parameter(
        id=206,
        name='Covariance between Temperature and Zonal, Components of the wind.',
        abbrev='COVTZ',
        unit=Unit.KELVIN_METERS_PER_SECOND
    ),
    207: Parameter(
        id=207,
        name='Covariance between Temperature and Meridional, Components of the wind.',
        abbrev='COVTM',
        unit=Unit.KELVIN_METERS_PER_SECOND
    ),
    208: Parameter(
        id=208,
        name='Vertical Diffusion Zonal Acceleration',
        abbrev='VDFUA',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    209: Parameter(
        id=209,
        name='Vertical Diffusion Meridional Acceleration',
        abbrev='VDFVA',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    210: Parameter(
        id=210,
        name='Gravity wave drag zonal acceleration',
        abbrev='GWDU',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    211: Parameter(
        id=211,
        name='Gravity wave drag meridional acceleration',
        abbrev='GWDV',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    212: Parameter(
        id=212,
        name='Convective zonal momentum mixing acceleration',
        abbrev='CNVU',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    213: Parameter(
        id=213,
        name='Convective meridional momentum mixing acceleration',
        abbrev='CNVV',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    214: Parameter(
        id=214,
        name='Tendency of vertical velocity',
        abbrev='WTEND',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    215: Parameter(
        id=215,
        name='Omega (Dp/Dt) divide by density',
        abbrev='OMGALF',
        unit=Unit.KELVIN
    ),
    216: Parameter(
        id=216,
        name='Convective Gravity wave drag zonal acceleration',
        abbrev='CNGWDU',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    217: Parameter(
        id=217,
        name='Convective Gravity wave drag meridional acceleration',
        abbrev='CNGWDV',
        unit=Unit.METERS_PER_SECOND_SQUARED
    ),
    218: Parameter(
        id=218,
        name='Velocity Point Model Surface',
        abbrev='LMV'
    ),
    219: Parameter(
        id=219,
        name='Potential Vorticity (Mass-Weighted)',
        abbrev='PVMWW',
        unit=Unit.PER_SECOND_PER_METER
    ),
    220: Parameter(
        id=220,
        name='Hourly Maximum of Upward Vertical Velocity',
        abbrev='MAXUVV',
        unit=Unit.METERS_PER_SECOND
    ),
    221: Parameter(
        id=221,
        name='Hourly Maximum of Downward Vertical Velocity',
        abbrev='MAXDVV',
        unit=Unit.METERS_PER_SECOND
    ),
    222: Parameter(
        id=222,
        name='U Component of Hourly Maximum 10m Wind Speed',
        abbrev='MAXUW',
        unit=Unit.METERS_PER_SECOND
    ),
    223: Parameter(
        id=223,
        name='V Component of Hourly Maximum 10m Wind Speed',
        abbrev='MAXVW',
        unit=Unit.METERS_PER_SECOND
    ),
    224: Parameter(
        id=224,
        name='Ventilation Rate',
        abbrev='VRATE',
        unit=Unit.SQUARE_METERS_PER_SECOND
    ),
    225: Parameter(
        id=225,
        name='Transport Wind Speed',
        abbrev='TRWSPD',
        unit=Unit.METERS_PER_SECOND
    ),
    226: Parameter(
        id=226,
        name='Transport Wind Direction',
        abbrev='TRWDIR',
        unit=Unit.DEGREE
    ),
    227: Parameter(
        id=227,
        name='Earliest Reasonable Arrival Time (10% exceedance)',
        abbrev='TOA10',
        unit=Unit.SECOND
    ),
    228: Parameter(
        id=228,
        name='Most Likely Arrival Time (50% exceedance)',
        abbrev='TOA50',
        unit=Unit.SECOND
    ),
    229: Parameter(
        id=229,
        name='Most Likely Departure Time (50% exceedance)',
        abbrev='TOD50',
        unit=Unit.SECOND
    ),
    230: Parameter(
        id=230,
        name='Latest Reasonable Departure Time (90% exceedance)',
        abbrev='TOD90',
        unit=Unit.SECOND
    ),
    231: Parameter(
        id=231,
        name='Tropical Wind Direction',
        abbrev='TPWDIR',
        unit=Unit.DEGREE
    ),
    232: Parameter(
        id=232,
        name='Tropical Wind Speed',
        abbrev='TPWSPD',
        unit=Unit.METERS_PER_SECOND
    ),
    233: Parameter(
        id=233,
        name='Inflow Based (ESFC) to 50% EL Shear Magnitude',
        abbrev='ESHR',
        unit=Unit.KNOTS
    ),
    234: Parameter(
        id=234,
        name='U Component Inflow Based to 50% EL Shear Vector',
        abbrev='UESH',
        unit=Unit.KNOTS
    ),
    235: Parameter(
        id=235,
        name='V Component Inflow Based to 50% EL Shear Vector',
        abbrev='VESH',
        unit=Unit.KNOTS
    ),
    236: Parameter(
        id=236,
        name='U Component Bunkers Effective Right Motion',
        abbrev='UEID',
        unit=Unit.KNOTS
    ),
    237: Parameter(
        id=237,
        name='V Component Bunkers Effective Right Motion',
        abbrev='VEID',
        unit=Unit.KNOTS
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
