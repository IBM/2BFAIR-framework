# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json
from typing import Iterable, List

from tobefair_backend.constants import METADATA_STANDARD_PATH
from tobefair_framework.model.metadata.metadata_keys import MetadataStandardName
from tobefair_framework.model.metadata.metadata_standard import (
    ExternalID,
    MetadataStandard,
)


class MetadataStandardRepository:
    @classmethod
    def dictionary_to_metadata_standard(
        cls, raw_metadata_standard_dictionary: dict, metadata_standard_name: str
    ) -> MetadataStandard | None:
        try:
            subjects = raw_metadata_standard_dictionary["field_of_science"]
            external_ids = list(
                map(
                    lambda external_id_info: ExternalID(
                        value=str(external_id_info["value"])
                    ),
                    list(raw_metadata_standard_dictionary["identifier"]),
                )
            )
            metadata_standard_type = MetadataStandard.get_type_from_subjects(subjects)
            return MetadataStandard(
                name=metadata_standard_name,
                subjects=subjects,
                external_ids=external_ids,
                type=metadata_standard_type,
            )
        except KeyError:
            return None

    @classmethod
    def parse_json(cls, json_string: str) -> List[MetadataStandard]:
        dictionary = json.loads(json_string)
        return [
            standard
            for standard in map(
                lambda metadata_standard_name: cls.dictionary_to_metadata_standard(
                    raw_metadata_standard_dictionary=dictionary[metadata_standard_name],
                    metadata_standard_name=metadata_standard_name,
                ),
                dictionary.keys(),
            )
            if standard is not None
        ]

    @classmethod
    def all(cls) -> List[MetadataStandard]:
        path = METADATA_STANDARD_PATH
        with open(path, "r") as json_file:
            return cls.parse_json(json_file.read())

    @classmethod
    def get_metadata_standards_by_name(
        cls, name: MetadataStandardName
    ) -> MetadataStandard | None:
        all_metadata_standards = cls.all()
        metadata_standards = list(
            filter(
                lambda metadata_standard: metadata_standard is not None
                and name.value == metadata_standard.name,
                all_metadata_standards,
            )
        )
        if len(metadata_standards) > 1:
            raise Exception(
                f"Only one metadata standard should be returned for {name}."
            )
        elif len(metadata_standards) == 0:
            return None
        else:
            return metadata_standards[0]

    @classmethod
    def metadata_standards_from_external_id_uri(
        cls, uri: str
    ) -> Iterable[MetadataStandard]:
        all_metadata_standards = cls.all()
        return filter(
            lambda metadata_standard: metadata_standard is not None
            and uri in metadata_standard.external_id_uris(),
            all_metadata_standards,
        )

    @classmethod
    def metadata_standards_from_external_id_uris(
        cls, uris: Iterable[str]
    ) -> Iterable[MetadataStandard]:
        community_required_metadata_standards: List[MetadataStandard] = []

        for found_standards in map(
            lambda metadata_standard_uri: list(
                MetadataStandardRepository.metadata_standards_from_external_id_uri(
                    uri=metadata_standard_uri
                )
            ),
            uris,
        ):
            community_required_metadata_standards.extend(found_standards)
        return community_required_metadata_standards
