from model.grib2.code_table import ProductDefinitionTemplate


class Grib2PDS:
    _vertical_values_count: int = None
    _product_definition_template: ProductDefinitionTemplate = None