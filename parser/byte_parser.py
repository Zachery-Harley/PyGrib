class ByteParser:
    _bytes_: bytearray
    _position = 0

    def __init__(self, bytes_: bytearray):
        self._bytes_ = bytes_

    def skip(self, length: int):
        self._position += length

    def next_bytes(self, length: int) -> bytearray:
        value = self._bytes_[self._position: self._position + length]
        self._position += length
        return value

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

