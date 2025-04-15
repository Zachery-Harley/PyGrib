from __future__ import annotations

from model.grib2.code_table import GridDefinitionSource, QuasiRegularGridInterpretation, get_grid_definition_source, \
    GridDefinitionTemplate, get_quasi_regular_grid_interpretation, get_grid_definition_template


class Grib2GridDefinitionSection:
    _source_of_grid_definition: GridDefinitionSource = None
    _number_of_data_points: int = None
    _quasi_regular_octets_per_value: int = None
    _quasi_regular_grid_interpretation: QuasiRegularGridInterpretation = QuasiRegularGridInterpretation.NO_LIST
    _grid_definition_template_number: GridDefinitionTemplate = GridDefinitionTemplate.MISSING

    def __init__(self, grib2_grid_definition_section: Grib2GridDefinitionSection = None):
        if grib2_grid_definition_section is not None:
            self._source_of_grid_definition = grib2_grid_definition_section.get_source_of_grid_definition()
            self._number_of_data_points = grib2_grid_definition_section.get_number_of_data_points()
            self._quasi_regular_octets_per_value = grib2_grid_definition_section.get_quasi_regular_octets_per_value()
            self._quasi_regular_grid_interpretation = grib2_grid_definition_section.get_quasi_regular_grid_interpretation()
            self._grid_definition_template_number = grib2_grid_definition_section.get_grid_definition_template_number()

    def get_source_of_grid_definition(self) -> GridDefinitionSource:
        return self._source_of_grid_definition

    def set_source_of_grid_definition(self,
                                      source_of_grid_definition: GridDefinitionSource | int) -> Grib2GridDefinitionSection:
        if isinstance(source_of_grid_definition, GridDefinitionSource):
            self._source_of_grid_definition = source_of_grid_definition
        else:
            self._source_of_grid_definition = get_grid_definition_source(source_of_grid_definition)
        return self

    def get_number_of_data_points(self) -> int:
        return self._number_of_data_points

    def set_number_of_data_points(self, number_of_data_points: int) -> Grib2GridDefinitionSection:
        self._number_of_data_points = number_of_data_points
        return self

    def get_quasi_regular_octets_per_value(self) -> int:
        return self._quasi_regular_octets_per_value

    def set_quasi_regular_octets_per_value(self, quasi_regular_octets_per_value: int) -> Grib2GridDefinitionSection:
        self._quasi_regular_octets_per_value = quasi_regular_octets_per_value
        return self

    def get_quasi_regular_grid_interpretation(self) -> QuasiRegularGridInterpretation:
        return self._quasi_regular_grid_interpretation

    def set_quasi_regular_grid_interpretation(self,
                                              quasi_regular_grid_interpretation: QuasiRegularGridInterpretation | int) -> Grib2GridDefinitionSection:
        if isinstance(quasi_regular_grid_interpretation, QuasiRegularGridInterpretation):
            self._quasi_regular_grid_interpretation = quasi_regular_grid_interpretation
        else:
            self._quasi_regular_grid_interpretation = get_quasi_regular_grid_interpretation(
                quasi_regular_grid_interpretation)
        return self

    def get_grid_definition_template_number(self) -> GridDefinitionTemplate:
        return self._grid_definition_template_number

    def set_grid_definition_template_number(self,
                                            grid_definition_template_number: GridDefinitionTemplate | int) -> Grib2GridDefinitionSection:
        if isinstance(grid_definition_template_number, GridDefinitionTemplate):
            self._grid_definition_template_number = grid_definition_template_number
        else:
            self._grid_definition_template_number = get_grid_definition_template(grid_definition_template_number)
        return self
