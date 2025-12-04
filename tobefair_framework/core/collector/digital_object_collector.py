# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import idutils
from pydantic import BaseModel

from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.core.notification.notification_context import (
    Notification,
    NotificationRegistry,
)
from tobefair_framework.model.digital_object_info import (
    DigitalObjectInfo,
    mock_digital_object_info,
)
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo


class DigitalObjectCollector(BaseModel):

    def get_digital_object_info(
        self,
        raw_identifier: str,
        metadata_collector: MetadataCollector,
    ) -> DigitalObjectInfo:
        identifier_info: IdentifierInfo = self.get_identifier_info(
            identifier=raw_identifier
        )
        if not identifier_info.url:
            notification = Notification(
                type="error",
                title="Error",
                description="Digital object's URI could not be resolved to an URL.",
            )
            NotificationRegistry.add_notification(notification)
            return DigitalObjectInfo(
                identifier_info=identifier_info,
                metadata_record=None,
                landing_page=None,
            )
        try:
            return self._read_digital_object_info(
                identifier_info=identifier_info,
                metadata_collector=metadata_collector,
            )
        except Exception:
            notification = Notification(
                type="error",
                title="Error",
                description="Digital object's metadata could not be collected.",
            )
            NotificationRegistry.add_notification(notification)
            return DigitalObjectInfo(
                identifier_info=identifier_info,
                metadata_record=None,
                landing_page=None,
            )

    def _read_digital_object_info(
        self,
        identifier_info: IdentifierInfo,
        metadata_collector: MetadataCollector,
    ) -> DigitalObjectInfo:
        return DigitalObjectInfo(
            identifier_info=identifier_info,
            metadata_record=None,
            landing_page=None,
        )

    @classmethod
    def get_identifier_info(cls, identifier: str) -> IdentifierInfo:
        # parse a Uniform Resource Locator (URL) string into its constituent components,
        # like:
        # - hostname('doi.org'),
        # - netloc ('doi.org'),
        # - path ('/10.5281/zenodo.8255909')
        # - scheme ('https')
        if len(identifier) > 4 and not identifier.isnumeric():
            identifier_schemas = idutils.detect_identifier_schemes(identifier)
            preferred_schema = "url"
            for schema in identifier_schemas:
                if schema != "url":
                    preferred_schema = schema
                    break
            url = idutils.to_url(identifier, preferred_schema)
            return IdentifierInfo(
                identifier=identifier,
                identifier_schemas=identifier_schemas,
                preferred_schema=preferred_schema,
                url=url,
            )
        return IdentifierInfo(identifier=identifier)

    @classmethod
    def obtain_mock_digital_object_info(
        cls, raw_identifier: str, metadata_collector: MetadataCollector
    ) -> DigitalObjectInfo:
        return mock_digital_object_info()
