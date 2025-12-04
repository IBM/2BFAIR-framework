# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import Iterable, List

from pydantic import BaseModel


class MetadataStandard(BaseModel):

    name: str
    subjects: List[str] = []
    external_ids: List["ExternalID"] = []
    type: "MetadataStandardType | None" = None

    @classmethod
    def get_type_from_subjects(cls, subjects: List[str]) -> "MetadataStandardType":
        if subjects == ["sciences"] or all(
            subject == "Multidisciplinary" for subject in subjects
        ):
            return MetadataStandardType.Generic
        else:
            return MetadataStandardType.Disciplinary

    def __eq__(self, value: object) -> bool:
        try:
            value_name = getattr(value, "name", None)
            value_external_ids: List["ExternalID"] = getattr(value, "external_ids", [])
            return self.name == value_name or any(
                map(
                    lambda external_id: external_id in value_external_ids,
                    self.external_ids,
                )
            )
        except Exception:
            return False

    def external_id_uris(self) -> Iterable[str]:
        return map(lambda external_id: external_id.value, self.external_ids)


class ExternalID(BaseModel):
    value: str

    def __eq__(self, value: object) -> bool:
        if isinstance(value, ExternalID):
            return self.value == value.value
        return False


class MetadataStandardType(Enum):
    Generic = "Generic"
    Disciplinary = "Disciplinary"


class MetadataStandardSubject(BaseModel):
    value: str
