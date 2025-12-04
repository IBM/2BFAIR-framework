# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel

from tobefair_framework.model.metadata.metadata_keys import (
    MetadataSourceKeys,
    MetadataStandardName,
)


class MetadataRecord(BaseModel):

    is_machine_retrieved: bool
    raw_value: dict
    metadata_source_key: MetadataSourceKeys | None = None
    metadata_standard_name: MetadataStandardName | None = None
