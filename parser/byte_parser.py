import struct
from enum import Enum

from parser import BitParser


class IntMode(Enum):
    TWOS_COMPLEMENT = 0
    SIGN_MAGNITUDE = 1


class FloatPrecision(Enum):
    SINGLE = 4  # Single-precision (32-bit, 4 bytes)
    DOUBLE = 8  # Double-precision (64-bit, 8 bytes)


class ByteParser:
    _default_int_mode: IntMode
    _bytes_: bytearray
    _position = 0

    def __init__(self, bytes_: bytearray, int_mode: IntMode = IntMode.SIGN_MAGNITUDE):
        self._bytes_ = bytes_
        self._default_int_mode = int_mode

    def skip(self, length: int):
        self._position += length

    def next_bytes(self, length: int) -> bytearray:
        value = self._bytes_[self._position: self._position + length]
        self._position += length
        return value

    def next_byte_flag(self) -> BitParser:
        return BitParser(self.next_uint_8())

    def next_uint(self, length: int) -> int:
        return int.from_bytes(self.next_bytes(length), byteorder='big', signed=False)

    def next_uint_8(self) -> int:
        return self.next_uint(1)

    def next_uint_16(self):
        return self.next_uint(2)

    def next_uint_24(self):
        return self.next_uint(3)

    def next_uint_32(self):
        return self.next_uint(4)

    def next_int(self, length: int, mode: IntMode = None):
        mode = mode or self._default_int_mode

        match mode:
            case IntMode.SIGN_MAGNITUDE:
                return self._convert_sign_magnitude_to_int(self.next_uint(length), length)
            case IntMode.TWOS_COMPLEMENT:
                return int.from_bytes(self.next_bytes(length), byteorder='big', signed=True)
            case _:
                raise Exception(f'Unsupported integer mode: {mode}')

    def next_int_8(self, mode: IntMode = None):
        return self.next_int(1, mode)

    def next_int_16(self, mode: IntMode = None):
        return self.next_int(2, mode)

    def next_int_24(self, mode: IntMode = None):
        return self.next_int(3, mode)

    def next_int_32(self, mode: IntMode = None):
        return self.next_int(4, mode)

    def next_ieee_float(self, precision: FloatPrecision) -> float:
        if precision == FloatPrecision.SINGLE:
            format_char = 'f'  # 4 bytes for single-precision
        elif precision == FloatPrecision.DOUBLE:
            format_char = 'd'  # 8 bytes for double-precision
        else:
            raise ValueError(f"Unsupported precision: {precision}")

        raw_bytes = self.next_bytes(precision.value)
        return struct.unpack(f'>{format_char}', raw_bytes)[0]  # '>' for big-endian

    @staticmethod
    def _convert_sign_magnitude_to_int(unsigned_value: int, length: int) -> int:
        sign_bit_mask = 1 << (length * 8 - 1)
        if unsigned_value & sign_bit_mask:
            # If the sign bit is set, clear it (to get the magnitude) and negate
            magnitude = unsigned_value & ~sign_bit_mask
            return -magnitude
        else:
            # Otherwise, just return the magnitude
            return unsigned_value

    def get_remaining_bytes(self):
        return self._bytes_[self._position:]
