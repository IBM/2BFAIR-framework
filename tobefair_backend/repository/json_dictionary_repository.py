import json
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class JsonDictionaryRepository(ABC, Generic[T]):
    _all: List[T] | None = None

    @classmethod
    @abstractmethod
    def file_path(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def dictionary_to_model(cls, dictionary: dict) -> T | None:
        pass

    @classmethod
    def parse_json(cls, json_string: str) -> List[T]:
        json_file_dictionary = json.loads(json_string)
        return [
            metadata_format
            for metadata_format in [
                cls.dictionary_to_model(value)
                for value in list(json_file_dictionary.values())
            ]
            if metadata_format is not None
        ]

    @classmethod
    def all(cls) -> List[T]:
        if cls._all is None:
            with open(cls.file_path(), "r") as json_file:
                cls._all = cls.parse_json(json_file.read())
                return cls._all
        return cls._all
