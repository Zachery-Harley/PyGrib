from model.grib2.parameter import Parameter, Unit

meteorological_forecast_radar_imagery = {
    0: Parameter(id=0, name='Equivalent radar reflectivity factor for rain', unit=Unit.MM_M6_M3, abbrev='REFZR'),
    1: Parameter(id=1, name='Equivalent radar reflectivity factor for snow', unit=Unit.MM_M6_M3, abbrev='REFZI'),
    2: Parameter(id=2, name='Equivalent radar reflectivity factor for parameterized convection', unit=Unit.MM_M6_M3,
                 abbrev='REFZC'),
    3: Parameter(id=3, name='Echo Top', unit=Unit.METERS, abbrev='RETOP'),
    4: Parameter(id=4, name='Reflectivity', unit=Unit.DECIBEL, abbrev='REFD'),
    5: Parameter(id=5, name='Composite reflectivity', unit=Unit.DECIBEL, abbrev='REFC'),
    192: Parameter(id=192, name='Equivalent radar reflectivity factor for rain', unit=Unit.MM_M6_M3, abbrev='REFZR'),
    193: Parameter(id=193, name='Equivalent radar reflectivity factor for snow', unit=Unit.MM_M6_M3, abbrev='REFZI'),
    194: Parameter(id=194, name='Equivalent radar reflectivity factor for parameterized convection', unit=Unit.MM_M6_M3,
                   abbrev='REFZC'),
    195: Parameter(id=195, name='Reflectivity', unit=Unit.DECIBEL, abbrev='REFD'),
    196: Parameter(id=196, name='Composite reflectivity', unit=Unit.DECIBEL, abbrev='REFC'),
    197: Parameter(id=197, name='Echo Top', unit=Unit.METERS, abbrev='RETOP'),
    198: Parameter(id=198, name='Hourly Maximum of Simulated Reflectivity', unit=Unit.DECIBEL, abbrev='MAXREF'),
    255: Parameter(id=255, name="Missing")
}

