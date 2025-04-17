from model.grib2.parameter import Parameter, Unit

meteorological_trace_gases = {
    0: Parameter(id=0, name='Total Ozone', unit=Unit.DOBSON, abbrev='TOZNE'),
    1: Parameter(id=1, name='Ozone Mixing Ratio', unit=Unit.KG_PER_KG, abbrev='O3MR'),
    2: Parameter(id=2, name='Total Column Integrated Ozone', unit=Unit.DOBSON, abbrev='TCIOZ'),
    192: Parameter(id=192, name='Ozone Mixing Ratio', unit=Unit.KG_PER_KG, abbrev='O3MR'),
    193: Parameter(id=193, name='Ozone Concentration', unit=Unit.PPB, abbrev='OZCON'),
    194: Parameter(id=194, name='Categorical Ozone Concentration', unit=Unit.NON_DIM, abbrev='OZCAT'),
    195: Parameter(id=195, name='Ozone Vertical Diffusion', unit=Unit.KG_PER_KG_PER_SECOND, abbrev='VDFOZ'),
    196: Parameter(id=196, name='Ozone Production', unit=Unit.KG_PER_KG_PER_SECOND, abbrev='POZ'),
    197: Parameter(id=197, name='Ozone Tendency', unit=Unit.KG_PER_KG_PER_SECOND, abbrev='TOZ'),
    198: Parameter(id=198, name='Ozone Production from Temperature Term', unit=Unit.KG_PER_KG_PER_SECOND,
                   abbrev='POZT'),
    199: Parameter(id=199, name='Ozone Production from Column Ozone Term', unit=Unit.KG_PER_KG_PER_SECOND,
                   abbrev='POZO'),
    200: Parameter(id=200, name='Ozone Daily Max from 1-hour Average', unit=Unit.PPBV, abbrev='OZMAX1'),
    201: Parameter(id=201, name='Ozone Daily Max from 8-hour Average', unit=Unit.PPBV, abbrev='OZMAX8'),
    202: Parameter(id=202, name='PM 2.5 Daily Max from 1-hour Average', unit=Unit.MICROGRAMS_PER_CUBIC_METER,
                   abbrev='PDMAX1'),
    203: Parameter(id=203, name='PM 2.5 Daily Max from 24-hour Average', unit=Unit.MICROGRAMS_PER_CUBIC_METER,
                   abbrev='PDMAX24'),
    204: Parameter(id=204, name='Acetaldehyde & Higher Aldehydes', unit=Unit.PPBV, abbrev='ALD2'),    255: Parameter(id=255, name="Missing")
}
