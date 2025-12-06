import json
from typing import ClassVar, List

from tobefair_backend.constants import METADATA_FORMAT_PATH
from tobefair_framework.model.metadata.metadata_format import MetadataFormat


class MetadataFormatRepository:
    _all: ClassVar[List[MetadataFormat] | None] = None

    @classmethod
    def dictionary_to_metadata_format(
        cls, metadata_formats_dict: dict, metadata_format_name: str
    ) -> MetadataFormat | None:
        if (
            format_dict := metadata_formats_dict.get(metadata_format_name)
        ) and isinstance(format_dict, dict):
            return MetadataFormat(
                label=format_dict["label"], acronym=format_dict["acronym"]
            )
        return None

    @classmethod
    def parse_json(cls, json_string: str) -> List[MetadataFormat]:
        metadata_format_dictionary = json.loads(json_string)
        map_fun = (
            lambda metadata_format_name: cls.dictionary_to_metadata_format(  # noqa E731
                metadata_format_dictionary, metadata_format_name
            )
        )
        return [
            metadata_format
            for metadata_format in [
                map_fun(format_name)
                for format_name in list(metadata_format_dictionary.keys())
            ]
            if metadata_format is not None
        ]

    @classmethod
    def get_metadata_format_with_label(cls, label: str) -> MetadataFormat | None:
        all = cls.all()
        matching_metadata_format: MetadataFormat | None = None
        [
            (matching_metadata_format := metadata_format)
            for metadata_format in all
            if metadata_format.label.upper() == label.upper()
        ]
        return matching_metadata_format

    @classmethod
    def all(cls) -> List[MetadataFormat]:
        if cls._all is None:
            path = METADATA_FORMAT_PATH
            with open(path, "r") as json_file:
                cls._all = cls.parse_json(json_file.read())
                return cls._all
        return cls._all
