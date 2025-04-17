from model.grib2.parameter import Parameter, Unit

meteorological_aerosols = {
    0: Parameter(id=0, name='Aerosol Type', abbrev='AEROT'),
    192: Parameter(id=192, name='Particulate matter (coarse)', unit=Unit.MICROGRAMS_PER_CUBIC_METER, abbrev='PMTC'),
    193: Parameter(id=193, name='Particulate matter (fine)', unit=Unit.MICROGRAMS_PER_CUBIC_METER, abbrev='PMTF'),
    194: Parameter(id=194, name='Particulate matter (fine)', unit=Unit.LOG_MICROGRAMS_PER_CUBIC_METER, abbrev='LPMTF'),
    195: Parameter(id=195, name='Integrated column particulate matter (fine)', unit=Unit.LOG_MICROGRAMS_PER_CUBIC_METER,
                   abbrev='LIPMF'),
    255: Parameter(id=255, name="Missing")
}
