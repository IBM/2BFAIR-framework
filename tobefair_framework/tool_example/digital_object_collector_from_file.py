# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json

from tobefair_framework.core.collector.digital_object_collector import (
    DigitalObjectCollector,
)
from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo


class DigitalObjectCollectorFromFile(DigitalObjectCollector):

    file_path: str

    def _read_digital_object_info(
        self,
        identifier_info: IdentifierInfo,
        metadata_collector: MetadataCollector,
    ) -> DigitalObjectInfo:
        with open(self.file_path, "r") as file:
            digital_object_dict = json.load(file)
            metadata_record = metadata_collector.get_metadata_record(
                raw_digital_object=digital_object_dict
            )
        return DigitalObjectInfo(
            identifier_info=identifier_info,
            metadata_record=metadata_record,
            landing_page=None,
        )
