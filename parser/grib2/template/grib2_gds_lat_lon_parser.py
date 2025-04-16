from model.grib2 import Grib2GDS
from model.grib2.flag_table import ResolutionAndComponent, ScanningMode
from model.grib2.template.grid_template_3_0_lat_long import GridTemplateLatLong
from parser import ByteParser, BitParser
from parser.grib2.template import GDSTemplateParser


class GDSLatLonTemplateParser(GDSTemplateParser):

    def parse(self, gds: Grib2GDS, template_data: bytearray | ByteParser):
        parser: ByteParser = ByteParser(template_data) if isinstance(template_data, bytearray) else template_data

        section: GridTemplateLatLong = GridTemplateLatLong(gds)
        (section
         .set_shape_of_earth(parser.next_uint_8())
         .set_spherical_earth_rad_scale_factor(parser.next_uint_8())
         .set_spherical_earth_rad_scaled_value(parser.next_uint_32())
         .set_oblate_earth_major_axis_scale_factor(parser.next_uint_8())
         .set_oblate_earth_major_axis_scaled_value(parser.next_uint_32())
         .set_oblate_earth_minor_axis_scale_factor(parser.next_uint_8())
         .set_oblate_earth_minor_axis_scaled_value(parser.next_uint_32())
         .set_points_along_parallel(parser.next_uint_32())
         .set_points_across_meridian(parser.next_uint_32())
         .set_basic_angle(parser.next_uint_32())
         .set_basic_angle_subdivision(parser.next_uint_32())
         .set_latitude_first_grid_point(parser.next_int_32())
         .set_longitude_first_grid_point(parser.next_int_32())
         .set_resolution_and_component(self.parse_resolution_and_component(parser))
         .set_latitude_last_grid_point(parser.next_int_32())
         .set_longitude_last_grid_point(parser.next_int_32())
         .set_parallel_increment(parser.next_uint_32())
         .set_meridian_increment(parser.next_uint_32())
         .set_scanning_mode(self.parse_scanning_mode(parser)))

    @staticmethod
    def parse_resolution_and_component(parser: ByteParser):
        flag: BitParser = parser.next_byte_flag().skip(2)
        return (ResolutionAndComponent()
                .set_parallel_increment_given(flag.next_bool())
                .set_meridian_increment_given(flag.next_bool())
                .set_vectors_relative_to_grid(flag.next_bool()))

    @staticmethod
    def parse_scanning_mode(parser: ByteParser):
        flag: BitParser = parser.next_byte_flag().skip(2)
        return (ScanningMode()
                .set_parallel_scans_negative(flag.next_bool())
                .set_meridian_scans_positive(flag.next_bool())
                .set_row_scans_meridian(flag.next_bool())
                .set_row_alternates_direction(flag.next_bool()))
