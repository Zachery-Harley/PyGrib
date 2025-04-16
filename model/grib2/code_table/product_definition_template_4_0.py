from enum import IntEnum

from parser.exception import Grib2FormatException


def get_product_definition_template(product_def_template: int):
    try:
        return ProductDefinitionTemplate(product_def_template)
    except ValueError:
        raise Grib2FormatException('Unsupported Product Definition Template: {}'.format(product_def_template))


class ProductDefinitionTemplate(IntEnum):
    FORECAST_AT_HORIZONTAL_LEVEL = 0
