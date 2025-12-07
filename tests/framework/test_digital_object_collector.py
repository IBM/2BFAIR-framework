# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

from tobefair_framework.core.collector.digital_object_collector import (
    DigitalObjectCollector,
    mock_digital_object_info,
)
from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo


class TestDigitalObjectCollector(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_identifier_infos = {
            # doi
            "10.5281/zenodo.8255909": IdentifierInfo(
                identifier="10.5281/zenodo.8255909",
                identifier_schemas=["doi", "handle"],
                preferred_schema="doi",
                url="http://doi.org/10.5281/zenodo.8255909",
            ),
            # doi url
            "https://zenodo.org/records/8255910": IdentifierInfo(
                identifier="https://zenodo.org/records/8255910",
                identifier_schemas=["url"],
                preferred_schema="url",
                url="https://zenodo.org/records/8255910",
            ),
            # string
            "12345678": IdentifierInfo(identifier="12345678"),
        }
        return super().setUp()

    def test_digital_object_without_url(self):
        raw_identifier = "12345678"
        metadata_collector = MetadataCollector()
        expected_digital_object_info: DigitalObjectInfo = mock_digital_object_info()
        expected_digital_object_info.identifier_info.identifier = raw_identifier
        returned_digital_object_info = DigitalObjectCollector().get_digital_object_info(
            raw_identifier=raw_identifier, metadata_collector=metadata_collector
        )
        self.assertEqual(
            expected_digital_object_info,
            returned_digital_object_info,
            "Expected and returned DigitalObjectInfo are different.",
        )
        print(returned_digital_object_info)

    def test_digital_object_with_url(self):
        raw_identifier = "https://zenodo.org/records/8255910"
        metadata_collector = MetadataCollector()
        expected_identifier_info = self.expected_identifier_infos[raw_identifier]

        returned_digital_object_info = DigitalObjectCollector().get_digital_object_info(
            raw_identifier=raw_identifier, metadata_collector=metadata_collector
        )
        self.assertEqual(
            expected_identifier_info,
            returned_digital_object_info.identifier_info,
            "Expected and returned DigitalObjectInfo.identifier_info are different.",
        )
        self.assertIsNone(
            returned_digital_object_info.metadata_record,
            "returned_digital_object_info.metadata_record should be None.",
        )
        self.assertIsNone(
            returned_digital_object_info.landing_page,
            "returned_digital_object_info.landing_page should be None",
        )

    def test_get_identifier_info(self):
        for (
            identifier,
            expected_identifier_info,
        ) in self.expected_identifier_infos.items():
            returned_identifier_info = DigitalObjectCollector.get_identifier_info(
                identifier=identifier
            )
            self.assertEqual(
                expected_identifier_info,
                returned_identifier_info,
                (
                    f"Expected and returned IdentifierInfos are different "
                    f"for {identifier}."
                ),
            )
