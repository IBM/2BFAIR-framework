# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel, ConfigDict

from tobefair_framework.model.identifier.identifier_info import (
    IdentifierInfo,
    mocked_identifier_info,
)
from tobefair_framework.model.landing_page import LandingPage
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class DigitalObjectInfo(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    identifier_info: IdentifierInfo
    metadata_record: MetadataRecord | None
    landing_page: LandingPage | None


def mock_digital_object_info() -> DigitalObjectInfo:
    return DigitalObjectInfo(
        identifier_info=mocked_identifier_info, metadata_record=None, landing_page=None
    )
