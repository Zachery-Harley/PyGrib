from model.grib2 import Grib2GDS
from model.grib2.code_table import GridDefinitionTemplate
from parser import ByteParser
from parser.exception import Grib2FormatException
from parser.grib2.template import GDSLatLonTemplateParser

GDS_TEMPLATE_MAPPING = {
    GridDefinitionTemplate.LAT_LON: GDSLatLonTemplateParser
}


def parse_gds_template(gds_template: GridDefinitionTemplate, gds: Grib2GDS, byte_parser: ByteParser):
    template_parser = GDS_TEMPLATE_MAPPING.get(gds_template)
    if template_parser is None:
        raise Grib2FormatException(f"No parser available for GDS template: {gds_template}")

    return template_parser().parse(gds, byte_parser)
