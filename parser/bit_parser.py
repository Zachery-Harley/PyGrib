from __future__ import annotations


class BitParser:
    _byte_: int
    _current_bit_index: int

    def __init__(self, byte: int):
        """Initialize the BitParser with a single byte.

        Args:
            byte (int): A single byte represented as an integer (0-255).
        """
        if not (0 <= byte <= 255):
            raise ValueError("byte must be an integer between 0 and 255 inclusive.")
        self._byte_ = byte
        self._current_bit_index = 0

    def next_bool(self) -> bool:
        """Return the next bit as a boolean.

        Returns:
            bool: True if the bit is 1, False if the bit is 0.

        Raises:
            Exception: If no more bits are available.
        """
        if self._current_bit_index >= 8:
            raise Exception("No more bits available.")

        # Get the next bit, shift and mask
        bit = (self._byte_ >> (7 - self._current_bit_index)) & 1
        self._current_bit_index += 1
        return bool(bit)

    def skip(self, length: int) -> BitParser:
        """Skip the specified number of bits.
        Args:
            length (int): The number of bits to skip.

        Returns:
            BitParser: The current BitParser instance.

        Raises:
            Exception: If skipping exceeds the 8-bit boundary.
        """
        if self._current_bit_index + length > 8:
            raise Exception("Skipping exceeds available bits.")

        self._current_bit_index += length
        return self
