import json
from typing import ClassVar, Dict, List

from tobefair_backend.constants import METADATA_SOURCE_PATH
from tobefair_backend.repository.metadata_format_repository import (
    MetadataFormatRepository as MtdtFtRepository,
)
from tobefair_backend.repository.metadata_offering_method_repository import (
    MetadataOfferingMethodRepository as MtdtOfferMetRepo,
)
from tobefair_framework.core.collector.metadata_source_repository import (
    MetadataSourceRepository,
)
from tobefair_framework.model.metadata.metadata_format import MetadataFormat
from tobefair_framework.model.metadata.metadata_offering_method import (
    MetadataOfferingMethod,
)
from tobefair_framework.model.metadata.metadata_source import MetadataSource


class MetadataSourceRepositoryApp(MetadataSourceRepository):
    _all_dict: ClassVar[Dict[str, MetadataSource] | None] = None

    @classmethod
    def all(cls) -> List[MetadataSource]:
        all_dict = cls.all_as_dict()
        return list(all_dict.values())

    @classmethod
    def all_as_dict(cls) -> Dict[str, MetadataSource]:
        if cls._all_dict is None:
            path = METADATA_SOURCE_PATH
            with open(path, "r") as file:
                json_string = file.read()
                json_dict = json.loads(json_string)
                cls._all_dict = {}
                [
                    cls._all_dict.update({key: value})
                    for key in json_dict.keys()
                    if (value := cls.get_metadata_source(json_dict[key]))
                ]
                return cls._all_dict
        return cls._all_dict

    @classmethod
    def metadata_source_with_key(cls, key: str) -> MetadataSource | None:
        return cls.all_as_dict().get(key)

    @classmethod
    def get_metadata_source(cls, metadata_source_dict: Dict) -> MetadataSource | None:
        if label := metadata_source_dict.get("label"):
            if acronym := metadata_source_dict.get("acronym"):
                method = None
                format = None
                if method_value := metadata_source_dict.get("method"):
                    method = cls.get_metadata_source_method(value=method_value)
                if format_value := metadata_source_dict.get("format"):
                    format = cls.get_metadata_source_format(value=format_value)
                return MetadataSource(
                    label=label, acronym=acronym, method=method, format=format
                )
        return None

    @classmethod
    def get_metadata_source_method(
        cls, value: MetadataOfferingMethod | str
    ) -> MetadataOfferingMethod | None:
        if isinstance(value, MetadataOfferingMethod):
            return value
        elif isinstance(value, str):
            if method := MtdtOfferMetRepo.get_metadata_metadata_offering_method(value):
                return method
        return None

    @classmethod
    def get_metadata_source_format(
        cls, value: MetadataFormat | str
    ) -> MetadataFormat | None:
        if isinstance(value, MetadataFormat):
            return value
        elif isinstance(value, str):
            if format := MtdtFtRepository.get_metadata_format_with_label(value):
                return format
        return None
