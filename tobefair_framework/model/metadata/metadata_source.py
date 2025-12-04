# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel

from tobefair_framework.model.metadata.metadata_format import MetadataFormat
from tobefair_framework.model.metadata.metadata_offering_method import (
    MetadataOfferingMethod,
)


class MetadataSource(BaseModel):
    label: str
    acronym: str
    method: MetadataOfferingMethod | None = None
    format: MetadataFormat | None = None
