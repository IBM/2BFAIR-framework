# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC

from pydantic import BaseModel

from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class MetadataCollector(ABC, BaseModel):

    @classmethod
    def get_metadata_record(
        cls, raw_digital_object: str | dict
    ) -> MetadataRecord | None:
        return None
