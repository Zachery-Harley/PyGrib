from model.grib2.parameter import Parameter, Unit

meteorological_mass = {
    0: Parameter(
        id=0,
        name='Pressure',
        abbrev='PRES',
        unit=Unit.PASCAL
    ),
    1: Parameter(
        id=1,
        name='Pressure Reduced to MSL',
        abbrev='PRMSL',
        unit=Unit.PASCAL
    ),
    2: Parameter(
        id=2,
        name='Pressure Tendency',
        abbrev='PTEND',
        unit=Unit.PASCAL_PER_SECOND
    ),
    3: Parameter(
        id=3,
        name='ICAO Standard Atmosphere Reference Height',
        abbrev='ICAHT',
        unit=Unit.METERS
    ),
    4: Parameter(
        id=4,
        name='Geopotential',
        abbrev='GP',
        unit=Unit.SQUARE_METERS_PER_SECOND_SQUARED
    ),
    5: Parameter(
        id=5,
        name='Geopotential Height',
        abbrev='HGT',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    6: Parameter(
        id=6,
        name='Geometric Height',
        abbrev='DIST',
        unit=Unit.METERS
    ),
    7: Parameter(
        id=7,
        name='Standard Deviation of Height',
        abbrev='HSTDV',
        unit=Unit.METERS
    ),
    8: Parameter(
        id=8,
        name='Pressure Anomaly',
        abbrev='PRESA',
        unit=Unit.PASCAL
    ),
    9: Parameter(
        id=9,
        name='Geopotential Height Anomaly',
        abbrev='GPA',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    10: Parameter(
        id=10,
        name='Density',
        abbrev='DEN',
        unit=Unit.KG_PER_METER_CUBED
    ),
    11: Parameter(
        id=11,
        name='Altimeter Setting',
        abbrev='ALTS',
        unit=Unit.PASCAL
    ),
    12: Parameter(
        id=12,
        name='Thickness',
        abbrev='THICK',
        unit=Unit.METERS
    ),
    13: Parameter(
        id=13,
        name='Pressure Altitude',
        abbrev='PRESALT',
        unit=Unit.METERS
    ),
    14: Parameter(
        id=14,
        name='Density Altitude',
        abbrev='DENALT',
        unit=Unit.METERS
    ),
    15: Parameter(
        id=15,
        name='5-Wave Geopotential Height',
        abbrev='5WAVH',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    16: Parameter(
        id=16,
        name='Zonal Flux of Gravity Wave Stress',
        abbrev='U-GWD',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    17: Parameter(
        id=17,
        name='Meridional Flux of Gravity Wave Stress',
        abbrev='V-GWD',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    18: Parameter(
        id=18,
        name='Planetary Boundary Layer Height',
        abbrev='HPBL',
        unit=Unit.METERS
    ),
    19: Parameter(
        id=19,
        name='5-Wave Geopotential Height Anomaly',
        abbrev='5WAVA',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    20: Parameter(
        id=20,
        name='Standard Deviation of Sub-Grid Scale Orography',
        abbrev='SDSGSO',
        unit=Unit.METERS
    ),
    21: Parameter(
        id=21,
        name='Angle of Sub-Grid Scale Orography',
        abbrev='AOSGSO',
        unit=Unit.RADIANS
    ),
    22: Parameter(
        id=22,
        name='Slope of Sub-Grid Scale Orography',
        abbrev='SSGSO',
        unit=Unit.NUMERIC
    ),
    23: Parameter(
        id=23,
        name='Gravity Wave Dissipation',
        abbrev='GWD',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    24: Parameter(
        id=24,
        name='Anisotropy of Sub-Grid Scale Orography',
        abbrev='ASGSO',
        unit=Unit.NUMERIC
    ),
    25: Parameter(
        id=25,
        name='Natural Logarithm of Pressure in Pa',
        abbrev='NLPRES',
        unit=Unit.NUMERIC
    ),
    26: Parameter(
        id=26,
        name='Exner Pressure',
        abbrev='EXPRES',
        unit=Unit.NUMERIC
    ),
    27: Parameter(
        id=27,
        name='Updraught Mass Flux',
        abbrev='UMFLX',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    28: Parameter(
        id=28,
        name='Downdraught Mass Flux',
        abbrev='DMFLX',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    29: Parameter(
        id=29,
        name='Updraught Detrainment Rate',
        abbrev='UDRATE',
        unit=Unit.KG_PER_METER_CUBED_PER_SECOND
    ),
    30: Parameter(
        id=30,
        name='Downdraught Detrainment Rate',
        abbrev='DDRATE',
        unit=Unit.KG_PER_METER_CUBED_PER_SECOND
    ),
    31: Parameter(
        id=31,
        name='Unbalanced Component of Logarithm of Surface Pressure',
        abbrev='UCLSPRS'
    ),
    32: Parameter(
        id=32,
        name='Saturation water vapour pressure',
        abbrev='SWATERVP',
        unit=Unit.PASCAL
    ),
    33: Parameter(
        id=33,
        name='Geometric altitude above mean sea level',
        abbrev='GAMSL',
        unit=Unit.METERS
    ),
    34: Parameter(
        id=34,
        name='Geometric height above ground level',
        abbrev='GHAGRD',
        unit=Unit.METERS
    ),
    35: Parameter(
        id=35,
        name='Column integrated divergence of total mass flux',
        abbrev='CDTMF',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    36: Parameter(
        id=36,
        name='Column integrated eastward total mass flux',
        abbrev='CETMF',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    37: Parameter(
        id=37,
        name='Column integrated northward total mass flux',
        abbrev='CNTMF',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    38: Parameter(
        id=38,
        name='Standard deviation of filtered subgrid orography',
        abbrev='SDFSO',
        unit=Unit.METERS
    ),
    39: Parameter(
        id=39,
        name='Column integrated mass of atmosphere',
        abbrev='CMATMOS',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    40: Parameter(
        id=40,
        name='Column integrated eastward geopotential flux',
        abbrev='CEGFLUX',
        unit=Unit.WATTS_PER_METER
    ),
    41: Parameter(
        id=41,
        name='Column integrated northward geopotential flux',
        abbrev='CNGFLUX',
        unit=Unit.WATTS_PER_METER
    ),
    42: Parameter(
        id=42,
        name='Column integrated divergence of water geopotential flux',
        abbrev='CDWGFLUX',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    43: Parameter(
        id=43,
        name='Column integrated divergence of geopotential flux',
        abbrev='CDGFLUX',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    44: Parameter(
        id=44,
        name='Height of zero-degree wet-bulb temperature',
        abbrev='HWBT',
        unit=Unit.METERS
    ),
    45: Parameter(
        id=45,
        name='Height of one-degree wet-bulb temperature',
        abbrev='WOBT',
        unit=Unit.METERS
    ),
    46: Parameter(
        id=46,
        name='Pressure departure from hydrostatic state',
        abbrev='PRESDHS',
        unit=Unit.PASCAL
    ),

    192: Parameter(
        id=192,
        name='MSLP (Eta model reduction)',
        abbrev='MSLET',
        unit=Unit.PASCAL
    ),
    193: Parameter(
        id=193,
        name='5-Wave Geopotential Height',
        abbrev='5WAVH',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    194: Parameter(
        id=194,
        name='Zonal Flux of Gravity Wave Stress',
        abbrev='U-GWD',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    195: Parameter(
        id=195,
        name='Meridional Flux of Gravity Wave Stress',
        abbrev='V-GWD',
        unit=Unit.NEWTONS_PER_METER_SQUARED
    ),
    196: Parameter(
        id=196,
        name='Planetary Boundary Layer Height',
        abbrev='HPBL',
        unit=Unit.METERS
    ),
    197: Parameter(
        id=197,
        name='5-Wave Geopotential Height Anomaly',
        abbrev='5WAVA',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    198: Parameter(
        id=198,
        name='MSLP (MAPS System Reduction)',
        abbrev='MSLMA',
        unit=Unit.PASCAL
    ),
    199: Parameter(
        id=199,
        name='3-hr pressure tendency (Std. Atmos. Reduction)',
        abbrev='TSLSA',
        unit=Unit.PASCAL_PER_SECOND
    ),
    200: Parameter(
        id=200,
        name='Pressure of level from which parcel was lifted',
        abbrev='PLPL',
        unit=Unit.PASCAL
    ),
    201: Parameter(
        id=201,
        name='X-gradient of Log Pressure',
        abbrev='LPSX',
        unit=Unit.PER_METER
    ),
    202: Parameter(
        id=202,
        name='Y-gradient of Log Pressure',
        abbrev='LPSY',
        unit=Unit.PER_METER
    ),
    203: Parameter(
        id=203,
        name='X-gradient of Height',
        abbrev='HGTX',
        unit=Unit.PER_METER
    ),
    204: Parameter(
        id=204,
        name='Y-gradient of Height',
        abbrev='HGTY',
        unit=Unit.PER_METER
    ),
    205: Parameter(
        id=205,
        name='Layer Thickness',
        abbrev='LAYTH',
        unit=Unit.METERS
    ),
    206: Parameter(
        id=206,
        name='Natural Log of Surface Pressure',
        abbrev='NLGSP',
        unit=Unit.NATURAL_LOG_KILO_PASCAL
    ),
    207: Parameter(
        id=207,
        name='Convective updraft mass flux',
        abbrev='CNVUMF',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    208: Parameter(
        id=208,
        name='Convective downdraft mass flux',
        abbrev='CNVDMF',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    209: Parameter(
        id=209,
        name='Convective detrainment mass flux',
        abbrev='CNVDEMF',
        unit=Unit.KG_PER_SQUARE_METER_PER_SECOND
    ),
    210: Parameter(
        id=210,
        name='Mass Point Model Surface',
        abbrev='LMH'
    ),
    211: Parameter(
        id=211,
        name='Geopotential Height (nearest grid point)',
        abbrev='HGTN',
        unit=Unit.GEOPOTENTIAL_METERS
    ),
    212: Parameter(
        id=212,
        name='Pressure (nearest grid point)',
        abbrev='PRESN',
        unit=Unit.PASCAL
    ),
    213: Parameter(
        id=213,
        name='Orographic Convexity',
        abbrev='ORCONV'
    ),
    214: Parameter(
        id=214,
        name='Orographic Asymmetry, W Component',
        abbrev='ORASW'
    ),
    215: Parameter(
        id=215,
        name='Orographic Asymmetry, S Component',
        abbrev='ORASS'
    ),
    216: Parameter(
        id=216,
        name='Orographic Asymmetry, SW Component',
        abbrev='ORASSW'
    ),
    217: Parameter(
        id=217,
        name='Orographic Asymmetry, NW Component',
        abbrev='ORASNW'
    ),
    218: Parameter(
        id=218,
        name='Orographic Length Scale, W Component',
        abbrev='ORLSW'
    ),
    219: Parameter(
        id=219,
        name='Orographic Length Scale, S Component',
        abbrev='ORLSS'
    ),
    220: Parameter(
        id=220,
        name='Orographic Length Scale, SW Component',
        abbrev='ORLSSW'
    ),
    221: Parameter(
        id=221,
        name='Orographic Length Scale, NW Component',
        abbrev='ORLSNW'
    ),
    222: Parameter(
        id=222,
        name='Effective Surface Height',
        abbrev='EFSH',
        unit=Unit.METERS
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
