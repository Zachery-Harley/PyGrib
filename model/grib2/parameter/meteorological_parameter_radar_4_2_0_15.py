from model.grib2.parameter import Parameter, Unit

meteorological_radar = {
    0: Parameter(id=0, name='Base Spectrum Width', unit=Unit.METERS_PER_SECOND, abbrev='BSWID'),
    1: Parameter(id=1, name='Base Reflectivity', unit=Unit.DECIBEL, abbrev='BREF'),
    2: Parameter(id=2, name='Base Radial Velocity', unit=Unit.METERS_PER_SECOND, abbrev='BRVEL'),
    3: Parameter(id=3, name='Vertically-Integrated Liquid Water', unit=Unit.KG_PER_SQUARE_METER, abbrev='VIL'),
    4: Parameter(id=4, name='Layer Maximum Base Reflectivity', unit=Unit.DECIBEL, abbrev='LMAXBR'),
    5: Parameter(id=5, name='Precipitation', unit=Unit.KG_PER_SQUARE_METER, abbrev='PREC'),
    6: Parameter(id=6, name='Radar Spectra (1)', abbrev='RDSP1'),
    7: Parameter(id=7, name='Radar Spectra (2)', abbrev='RDSP2'),
    8: Parameter(id=8, name='Radar Spectra (3)', abbrev='RDSP3'),
    9: Parameter(id=9, name='Reflectivity of Cloud Droplets', unit=Unit.DECIBEL, abbrev='RFCD'),
    10: Parameter(id=10, name='Reflectivity of Cloud Ice', unit=Unit.DECIBEL, abbrev='RFCI'),
    11: Parameter(id=11, name='Reflectivity of Snow', unit=Unit.DECIBEL, abbrev='RFSNOW'),
    12: Parameter(id=12, name='Reflectivity of Rain', unit=Unit.DECIBEL, abbrev='RFRAIN'),
    13: Parameter(id=13, name='Reflectivity of Graupel', unit=Unit.DECIBEL, abbrev='RFGRPL'),
    14: Parameter(id=14, name='Reflectivity of Hail', unit=Unit.DECIBEL, abbrev='RFHAIL'),
    15: Parameter(id=15, name='Hybrid Scan Reflectivity', unit=Unit.DECIBEL, abbrev='HSR'),
    16: Parameter(id=16, name='Hybrid Scan Reflectivity Height', unit=Unit.METERS, abbrev='HSRHT'),
    255: Parameter(id=255, name="Missing")
}

