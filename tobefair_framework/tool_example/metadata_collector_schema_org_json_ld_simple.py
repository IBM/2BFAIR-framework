# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class MetadataCollectorSchemaorgJsonldSimple(MetadataCollector):

    @classmethod
    def get_metadata_record(
        cls, raw_digital_object: str | dict
    ) -> MetadataRecord | None:
        if not isinstance(raw_digital_object, dict):
            raise Exception("raw_digital_object should be a dict.")
        return MetadataRecord(
            is_machine_retrieved=True,
            raw_value=raw_digital_object,
        )
