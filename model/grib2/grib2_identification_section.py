from __future__ import annotations

from model.grib2.code_table import Centre, get_centre, TableVersion, ReferenceTimeSignificance, ProductionStatus, \
    DataType, get_table_version

class Grib2IdentificationSection:

    _centre: Centre = None
    _sub_centre: int = None
    _table_version: TableVersion = TableVersion.MISSING
    _local_table_version: int = ReferenceTimeSignificance.MISSING
    _year: int = None
    _month: int = None
    _day: int = None
    _hour: int = None
    _minute: int = None
    _second: int = None
    _production_status: ProductionStatus = ProductionStatus.MISSING
    _data_type: DataType = DataType.MISSING

    def get_centre(self) -> Centre:
        return self._centre

    def set_centre(self, centre_id: int | Centre) -> Grib2IdentificationSection:
        self._centre = centre_id if isinstance(centre_id, Centre) else get_centre(centre_id)
        return self

    def get_sub_centre(self) -> int:
        return self._sub_centre

    def set_sub_centre(self, sub_centre: int) -> Grib2IdentificationSection:
        self._sub_centre = sub_centre
        return self

    def get_table_version(self) -> TableVersion:
        return self._table_version

    def set_table_version(self, table_version: TableVersion | int) -> Grib2IdentificationSection:
        self._table_version = table_version if isinstance(table_version, TableVersion) else get_table_version(
            table_version)
        return self

    def get_local_table_version(self) -> int:
        return self._local_table_version

    def set_local_table_version(self, local_table_version: int) -> Grib2IdentificationSection:
        self._local_table_version = local_table_version
        return self

    def get_year(self) -> int:
        return self._year

    def set_year(self, year: int) -> Grib2IdentificationSection:
        if year <= 0:
            raise ValueError("Year must be a positive integer.")
        self._year = year
        return self

    def get_month(self) -> int:
        return self._month

    def set_month(self, month: int) -> Grib2IdentificationSection:
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        self._month = month
        return self

    def get_day(self) -> int:
        return self._day

    def set_day(self, day: int) -> Grib2IdentificationSection:
        if day < 1 or day > 366:  # Accounting for leap years
            raise ValueError("Day must be between 1 and 366.")
        self._day = day
        return self

    def get_hour(self) -> int:
        return self._hour

    def set_hour(self, hour: int) -> Grib2IdentificationSection:
        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23.")
        self._hour = hour
        return self

    def get_minute(self) -> int:
        return self._minute

    def set_minute(self, minute: int) -> Grib2IdentificationSection:
        if minute < 0 or minute > 59:
            raise ValueError("Minute must be between 0 and 59.")
        self._minute = minute
        return self

    def get_second(self) -> int:
        return self._second

    def set_second(self, second: int) -> Grib2IdentificationSection:
        if second < 0 or second > 59:
            raise ValueError("Second must be between 0 and 59.")
        self._second = second
        return self

    def get_production_status(self) -> ProductionStatus:
        return self._production_status

    def set_production_status(self, production_status: ProductionStatus | int) -> Grib2IdentificationSection:
        self._production_status = production_status if isinstance(production_status,
                                                                  ProductionStatus) else ProductionStatus(
            production_status)
        return self

    def get_data_type(self) -> DataType:
        return self._data_type

    def set_data_type(self, data_type: DataType | int) -> Grib2IdentificationSection:
        self._data_type = data_type if isinstance(data_type, DataType) else DataType(data_type)
        return self
