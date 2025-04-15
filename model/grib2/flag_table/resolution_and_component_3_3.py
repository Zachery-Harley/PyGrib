from __future__ import annotations

from enum import IntEnum


class ResolutionAndComponent(IntEnum):
    _parallel_increment_given: bool = False
    _meridian_increment_given: bool = False
    _vectors_relative_to_grid: bool = False

    def is_parallel_increment_given(self) -> bool:
        return self._parallel_increment_given

    def is_meridian_increment_given(self) -> bool:
        return self._meridian_increment_given

    def is_vectors_relative_to_grid(self) -> bool:
        return self._vectors_relative_to_grid

    def set_parallel_increment_given(self, value: bool) -> ResolutionAndComponent:
        self._parallel_increment_given = value
        return self

    def set_meridian_increment_given(self, value: bool) -> ResolutionAndComponent:
        self._meridian_increment_given = value
        return self

    def set_vectors_relative_to_grid(self, value: bool) -> ResolutionAndComponent:
        self._vectors_relative_to_grid = value
        return self
