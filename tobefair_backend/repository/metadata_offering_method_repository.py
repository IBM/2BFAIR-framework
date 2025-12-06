# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tobefair_backend.constants import METADATA_OFFERING_METHOD_PATH
from tobefair_backend.repository.json_dictionary_repository import (
    JsonDictionaryRepository,
)
from tobefair_framework.model.metadata.metadata_offering_method import (
    MetadataOfferingMethod,
)


class MetadataOfferingMethodRepository(
    JsonDictionaryRepository[MetadataOfferingMethod]
):

    @classmethod
    def file_path(cls) -> str:
        return METADATA_OFFERING_METHOD_PATH

    @classmethod
    def dictionary_to_model(cls, dictionary: dict) -> MetadataOfferingMethod | None:
        try:
            return MetadataOfferingMethod.model_validate(dictionary)
        except Exception:
            return None

    @classmethod
    def get_metadata_metadata_offering_method(
        cls, acronym: str
    ) -> MetadataOfferingMethod | None:

        matching_offering_method: MetadataOfferingMethod | None = None
        [
            (matching_offering_method := offering_method)
            for offering_method in cls.all()
            if offering_method.acronym.upper() == acronym.upper()
        ]
        return matching_offering_method
