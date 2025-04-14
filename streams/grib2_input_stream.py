from abc import ABC, abstractmethod


class Grib2InputStream(ABC):

    @abstractmethod
    def end_of_file(self) -> bool:
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def next_record(self):
        pass
