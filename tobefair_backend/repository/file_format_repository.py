from typing import List

from tobefair_backend.constants import FILE_FORMAT_PATH
from tobefair_backend.model.file_format import FileFormat
from tobefair_backend.repository.json_dictionary_repository import (
    JsonDictionaryRepository,
)


class FileFormatRepository(JsonDictionaryRepository[FileFormat]):
    @classmethod
    def file_path(cls) -> str:
        return FILE_FORMAT_PATH

    @classmethod
    def dictionary_to_model(cls, dictionary: dict, **kwargs) -> FileFormat | None:
        try:
            return FileFormat.model_validate(dictionary)
        except Exception:
            return None

    @classmethod
    def science_file_formats(cls) -> List[FileFormat]:
        return [
            file_format
            for file_format in cls.all()
            if "scientific format" in file_format.reason
        ]

    @classmethod
    def long_term_file_formats(cls) -> List[FileFormat]:
        return [
            file_format
            for file_format in cls.all()
            if "long term format" in file_format.reason
        ]

    @classmethod
    def open_file_formats(cls) -> List[FileFormat]:
        return [
            file_format
            for file_format in cls.all()
            if "open format" in file_format.reason
        ]
