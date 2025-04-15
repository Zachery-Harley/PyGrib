from __future__ import annotations
from model.grib2 import Grib2GridDefinitionSection
from model.grib2.code_table import EarthShape
from model.grib2.flag_table import ResolutionAndComponent, ScanningMode


class GridTemplateLatLong(Grib2GridDefinitionSection):
    _shape_of_earth: EarthShape = EarthShape.MISSING
    _spherical_earth_rad_scale_factor: int = None
    _spherical_earth_rad_scaled_value: int = None
    _oblate_earth_major_axis_scale_factor: int = None
    _oblate_earth_major_axis_scaled_value: int = None
    _oblate_earth_minor_axis_scale_factor: int = None
    _oblate_earth_minor_axis_scaled_value: int = None
    _points_along_parallel: int = None
    _points_across_meridian: int = None
    _basic_angle: int = None
    _basic_angle_subdivision: int = None
    _latitude_first_grid_point: int = None
    _longitude_first_grid_point: int = None
    _resolution_and_component: ResolutionAndComponent = None
    _latitude_last_grid_point: int = None
    _longitude_last_grid_point: int = None
    _parallel_increment: int = None
    _meridian_increment: int = None
    _scanning_mode: ScanningMode = None

    def get_shape_of_earth(self) -> EarthShape:
        return self._shape_of_earth

    def set_shape_of_earth(self, value: EarthShape) -> GridTemplateLatLong:
        self._shape_of_earth = value
        return self

    def get_spherical_earth_rad_scale_factor(self) -> int:
        return self._spherical_earth_rad_scale_factor

    def set_spherical_earth_rad_scale_factor(self, value: int) -> GridTemplateLatLong:
        self._spherical_earth_rad_scale_factor = value
        return self

    def get_spherical_earth_rad_scaled_value(self) -> int:
        return self._spherical_earth_rad_scaled_value

    def set_spherical_earth_rad_scaled_value(self, value: int) -> GridTemplateLatLong:
        self._spherical_earth_rad_scaled_value = value
        return self

    def get_oblate_earth_major_axis_scale_factor(self) -> int:
        return self._oblate_earth_major_axis_scale_factor

    def set_oblate_earth_major_axis_scale_factor(self, value: int) -> GridTemplateLatLong:
        self._oblate_earth_major_axis_scale_factor = value
        return self

    def get_oblate_earth_major_axis_scaled_value(self) -> int:
        return self._oblate_earth_major_axis_scaled_value

    def set_oblate_earth_major_axis_scaled_value(self, value: int) -> GridTemplateLatLong:
        self._oblate_earth_major_axis_scaled_value = value
        return self

    def get_oblate_earth_minor_axis_scale_factor(self) -> int:
        return self._oblate_earth_minor_axis_scale_factor

    def set_oblate_earth_minor_axis_scale_factor(self, value: int) -> GridTemplateLatLong:
        self._oblate_earth_minor_axis_scale_factor = value
        return self

    def get_oblate_earth_minor_axis_scaled_value(self) -> int:
        return self._oblate_earth_minor_axis_scaled_value

    def set_oblate_earth_minor_axis_scaled_value(self, value: int) -> GridTemplateLatLong:
        self._oblate_earth_minor_axis_scaled_value = value
        return self

    def get_points_along_parallel(self) -> int:
        return self._points_along_parallel

    def set_points_along_parallel(self, value: int) -> GridTemplateLatLong:
        self._points_along_parallel = value
        return self

    def get_points_across_meridian(self) -> int:
        return self._points_across_meridian

    def set_points_across_meridian(self, value: int) -> GridTemplateLatLong:
        self._points_across_meridian = value
        return self

    def get_basic_angle(self) -> int:
        return self._basic_angle

    def set_basic_angle(self, value: int) -> GridTemplateLatLong:
        self._basic_angle = value
        return self

    def get_basic_angle_subdivision(self) -> int:
        return self._basic_angle_subdivision

    def set_basic_angle_subdivision(self, value: int) -> GridTemplateLatLong:
        self._basic_angle_subdivision = value
        return self

    def get_latitude_first_grid_point(self) -> int:
        return self._latitude_first_grid_point

    def set_latitude_first_grid_point(self, value: int) -> GridTemplateLatLong:
        self._latitude_first_grid_point = value
        return self

    def get_longitude_first_grid_point(self) -> int:
        return self._longitude_first_grid_point

    def set_longitude_first_grid_point(self, value: int) -> GridTemplateLatLong:
        self._longitude_first_grid_point = value
        return self

    def get_resolution_and_component(self) -> ResolutionAndComponent:
        return self._resolution_and_component

    def set_resolution_and_component(self, value: ResolutionAndComponent) -> GridTemplateLatLong:
        self._resolution_and_component = value
        return self

    def get_latitude_last_grid_point(self) -> int:
        return self._latitude_last_grid_point

    def set_latitude_last_grid_point(self, value: int) -> GridTemplateLatLong:
        self._latitude_last_grid_point = value
        return self

    def get_longitude_last_grid_point(self) -> int:
        return self._longitude_last_grid_point

    def set_longitude_last_grid_point(self, value: int) -> GridTemplateLatLong:
        self._longitude_last_grid_point = value
        return self

    def get_parallel_increment(self) -> int:
        return self._parallel_increment

    def set_parallel_increment(self, value: int) -> GridTemplateLatLong:
        self._parallel_increment = value
        return self

    def get_meridian_increment(self) -> int:
        return self._meridian_increment

    def set_meridian_increment(self, value: int) -> GridTemplateLatLong:
        self._meridian_increment = value
        return self

    def get_scanning_mode(self) -> ScanningMode:
        return self._scanning_mode

    def set_scanning_mode(self, value: ScanningMode) -> GridTemplateLatLong:
        self._scanning_mode = value
        return self
