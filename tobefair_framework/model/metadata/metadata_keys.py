# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class MetadataStandardName(Enum):
    SCHEMA_ORG = "Schema.org"
    PROV = "prov"


def get_metadata_standard_name_from_str(name: str) -> MetadataStandardName | None:
    for member in MetadataStandardName:
        if MetadataStandardName(name) == member:
            return member
    return None


class MetadataSourceKeys(Enum):
    SCHEMA_ORG_EMBEDDED = "SCHEMAORG_EMBEDDED"
    RDFA_EMBEDDED = "RDFA_EMBEDDED"
