import re
from enum import Enum

from pydantic import BaseModel


class DataType(BaseModel):
    value: str


class DataUnit(BaseModel):
    name: str


class DataUnits(Enum):
    byte = DataUnit(name="byte")


class DataSize(BaseModel):
    value: int
    unit: DataUnit = DataUnits.byte.value

    def __eq__(self, value: object) -> bool:
        if isinstance(value, DataSize):
            return self.value == value.value
        elif isinstance(value, int) or isinstance(value, float):
            return self.value == value
        return NotImplemented

    def __lt__(self, value: object) -> bool:
        if isinstance(value, DataSize):
            return self.value < value.value
        elif isinstance(value, int) or isinstance(value, float):
            return self.value < value
        return NotImplemented

    @classmethod
    def from_string(cls, size) -> "DataSize":
        try:
            bytematch = re.search(
                r"([0-9]+(?:[\.,][0-9]+)*)\s*([kMGTP]?(?:[Bb](?:ytes?)?))?", str(size)
            )
            if bytematch:
                size = bytematch[1]
                mult = str(bytematch[2])
                size = float(size)
                if mult.startswith("k"):
                    size = size * 1000
                elif mult.startswith("M"):
                    size = size * 1000000
                elif mult.startswith("G"):
                    size = size * 1000000000
                elif mult.startswith("P"):
                    size = size * 1000000000000
        except Exception as e:
            print("Content site Byte parsing error: ", str(e))
        return DataSize(value=int(size), unit=DataUnits.byte.value)
