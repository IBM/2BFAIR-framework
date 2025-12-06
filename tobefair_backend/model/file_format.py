# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List

from pydantic import BaseModel, ValidationError, field_validator

from tobefair_backend.model.resources.data_record import DataType


class FileFormat(BaseModel):
    ext: List[str]
    name: str
    mime: List[DataType]
    reason: List[str]
    source: List[str]

    @field_validator("mime", mode="before")
    @classmethod
    def validate_mime(cls, value):
        if isinstance(value, list):
            if all([isinstance(item, str) for item in value]):
                return [DataType(value=item) for item in value]
            if all([isinstance(item, DataType) for item in value]):
                return value
        raise ValidationError


def mime_types(formats: List[FileFormat]) -> List[DataType]:
    acc = []
    [acc := acc + format.mime for format in formats]
    return acc
