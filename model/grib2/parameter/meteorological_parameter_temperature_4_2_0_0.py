from model.grib2.parameter import Parameter, Unit

meteorological_temperature = {
    0: Parameter(
        id=0,
        name='Temperature',
        abbrev='TMP',
        unit=Unit.KELVIN
    ),
    1: Parameter(
        id=1,
        name='Virtual Temperature',
        abbrev='VTMP',
        unit=Unit.KELVIN
    ),
    2: Parameter(
        id=2,
        name='Potential Temperature',
        abbrev='POT',
        unit=Unit.KELVIN
    ),
    3: Parameter(
        id=3,
        name='Pseudo-Adiabatic Potential Temperature',
        abbrev='EPOT',
        unit=Unit.KELVIN
    ),
    4: Parameter(
        id=4,
        name='Maximum Temperature',
        abbrev='TMAX',
        unit=Unit.KELVIN,
        deprecated=True
    ),
    5: Parameter(
        id=5,
        name='Minimum Temperature',
        abbrev='TMIN',
        unit=Unit.KELVIN,
        deprecated=True
    ),
    6: Parameter(
        id=6,
        name='Dew Point Temperature',
        abbrev='DPT',
        unit=Unit.KELVIN
    ),
    7: Parameter(
        id=7,
        name='Dew Point Depression',
        abbrev='DEPR',
        unit=Unit.KELVIN
    ),
    8: Parameter(
        id=8,
        name='Lapse Rate',
        abbrev='LAPR',
        unit=Unit.KELVIN_PER_METER
    ),
    9: Parameter(
        id=9,
        name='Temperature Anomaly',
        abbrev='TMPA',
        unit=Unit.KELVIN
    ),
    10: Parameter(
        id=10,
        name='Latent Heat Net Flux',
        abbrev='LHTFL',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    11: Parameter(
        id=11,
        name='Sensible Heat Net Flux',
        abbrev='SHTFL',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    12: Parameter(
        id=12,
        name='Heat Index',
        abbrev='HEATX',
        unit=Unit.KELVIN
    ),
    13: Parameter(
        id=13,
        name='Wind Chill Factor',
        abbrev='WCF',
        unit=Unit.KELVIN
    ),
    14: Parameter(
        id=14,
        name='Minimum Dew Point Depression',
        abbrev='MINDPD',
        unit=Unit.KELVIN,
        deprecated=True
    ),
    15: Parameter(
        id=15,
        name='Virtual Potential Temperature',
        abbrev='VPTMP',
        unit=Unit.KELVIN
    ),
    16: Parameter(
        id=16,
        name='Snow Phase Change Heat Flux',
        abbrev='SNOHF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    17: Parameter(
        id=17,
        name='Skin Temperature',
        abbrev='SKINT',
        unit=Unit.KELVIN
    ),
    18: Parameter(
        id=18,
        name='Snow Temperature',
        abbrev='SNOT',
        unit=Unit.KELVIN
    ),
    19: Parameter(
        id=19,
        name='Turbulent Transfer Coefficient for Heat',
        abbrev='TTCHT',
        unit=Unit.NUMERIC
    ),
    20: Parameter(
        id=20,
        name='Turbulent Diffusion Coefficient for Heat',
        abbrev='TDCHT',
        unit=Unit.SQUARE_METERS_PER_SECOND
    ),
    21: Parameter(
        id=21,
        name='Apparent Temperature',
        abbrev='APTMP',
        unit=Unit.KELVIN
    ),
    22: Parameter(
        id=22,
        name='Temperature Tendency due to Short-Wave Radiation',
        abbrev='TTSWR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    23: Parameter(
        id=23,
        name='Temperature Tendency due to Long-Wave Radiation',
        abbrev='TTLWR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    24: Parameter(
        id=24,
        name='Temperature Tendency due to Short-Wave Radiation, Clear Sky',
        abbrev='TTSWRCS',
        unit=Unit.KELVIN_PER_SECOND
    ),
    25: Parameter(
        id=25,
        name='Temperature Tendency due to Long-Wave Radiation, Clear Sky',
        abbrev='TTLWRCS',
        unit=Unit.KELVIN_PER_SECOND
    ),
    26: Parameter(
        id=26,
        name='Temperature Tendency due to parameterizations',
        abbrev='TTPARM',
        unit=Unit.KELVIN_PER_SECOND
    ),
    27: Parameter(
        id=27,
        name='Wet Bulb Temperature',
        abbrev='WETBT',
        unit=Unit.KELVIN
    ),
    28: Parameter(
        id=28,
        name='Unbalanced Component of Temperature',
        abbrev='UCTMP',
        unit=Unit.KELVIN
    ),
    29: Parameter(
        id=29,
        name='Temperature Advection',
        abbrev='TMPADV',
        unit=Unit.KELVIN_PER_SECOND
    ),
    30: Parameter(
        id=30,
        name='Latent Heat Net Flux Due to Evaporation',
        abbrev='LHFLXE',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    31: Parameter(
        id=31,
        name='Latent Heat Net Flux Due to Sublimation',
        abbrev='LHFLXS',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    32: Parameter(
        id=32,
        name='Wet-Bulb Potential Temperature',
        abbrev='WETBPT',
        unit=Unit.KELVIN
    ),
    192: Parameter(
        id=192,
        name='Snow Phase Change Heat Flux',
        abbrev='SNOHF',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    193: Parameter(
        id=193,
        name='Temperature Tendency by All Radiation',
        abbrev='TTRAD',
        unit=Unit.KELVIN_PER_SECOND
    ),
    194: Parameter(
        id=194,
        name='Relative Error Variance',
        abbrev='REV',
    ),
    195: Parameter(
        id=195,
        name='Large Scale Condensate Heating Rate',
        abbrev='LRGHR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    196: Parameter(
        id=196,
        name='Deep Convective Heating Rate',
        abbrev='CNVHR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    197: Parameter(
        id=197,
        name='Total Downward Heat Flux at Surface',
        abbrev='THFLX',
        unit=Unit.WATTS_PER_METER_SQUARED
    ),
    198: Parameter(
        id=198,
        name='Temperature Tendency by All Physics',
        abbrev='TTDIA',
        unit=Unit.KELVIN_PER_SECOND
    ),
    199: Parameter(
        id=199,
        name='Temperature Tendency by Non-radiation Physics',
        abbrev='TTPHY',
        unit=Unit.KELVIN_PER_SECOND
    ),
    200: Parameter(
        id=200,
        name='Standard Dev. of IR Temp. over 1x1 deg. area',
        abbrev='TSD1D',
        unit=Unit.KELVIN
    ),
    201: Parameter(
        id=201,
        name='Shallow Convective Heating Rate',
        abbrev='SHAHR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    202: Parameter(
        id=202,
        name='Vertical Diffusion Heating rate',
        abbrev='VDFHR',
        unit=Unit.KELVIN_PER_SECOND
    ),
    203: Parameter(
        id=203,
        name='Potential Temperature at Top of Viscous Sublayer',
        abbrev='THZ0',
        unit=Unit.KELVIN
    ),
    204: Parameter(
        id=204,
        name='Tropical Cyclone Heat Potential',
        abbrev='TCHP',
        unit=Unit.JOULES_PER_SQUARE_METER_PER_KELVIN
    ),
    205: Parameter(
        id=205,
        name='Effective Layer (EL) Temperature',
        abbrev='ELMELT',
        unit=Unit.CELSIUS
    ),
    206: Parameter(
        id=206,
        name='Wet Bulb Globe Temperature',
        abbrev='WETGLBT',
        unit=Unit.KELVIN
    ),
    255: Parameter(
        id=255,
        name="Missing"
    )
}
