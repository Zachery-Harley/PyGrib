from model.grib2.parameter import Parameter, Unit

meteorological_electrodynamics = {
    0: Parameter(id=0, name='Lightning Strike Density', unit=Unit.METERS_SQUARED_PER_SECOND, abbrev='LTNGSD'),
    1: Parameter(id=1, name='Lightning Potential Index (LPI)', unit=Unit.JULES_PER_KG, abbrev='LTPINX'),
    2: Parameter(id=2, name='Cloud-to-Ground Lightning Flash Density', unit=Unit.KM_SQUARED_PER_DAY, abbrev='CDGDLTFD'),
    3: Parameter(id=3, name='Cloud-to-Cloud Lightning Flash Density', unit=Unit.KM_SQUARED_PER_DAY, abbrev='CDCDLTFD'),
    4: Parameter(id=4, name='Total Lightning Flash Density', unit=Unit.KM_SQUARED_PER_DAY, abbrev='TLGTFD'),
    5: Parameter(id=5, name='Subgrid-scale lightning potential index', unit=Unit.JULES_PER_KG,
                 abbrev='SLNGPIDX'),
    192: Parameter(id=192, name='Lightning', unit=Unit.NON_DIM, abbrev='LTNG'),
    255: Parameter(id=255, name="Missing")
}

