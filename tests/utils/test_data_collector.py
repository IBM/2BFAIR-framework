# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json
import unittest

from tests.data_for_testing.mocks import (
    json_ld_metadata_pangaea_908011 as mock_metadata,
)
from tests.data_for_testing.mocks import (
    json_ld_metadata_pangaea_908011_with_distribution_size as mock_metadata_with_size,
)
from tests.data_for_testing.mocks import mock_html_2, mock_html_pangea_908011
from tobefair_backend.utils.data_collector import DataCollector
from tobefair_backend.utils.data_link_collector import DataLinkCollector
from tobefair_backend.utils.list_utils import remove_duplicates
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class TestDataCollector(unittest.TestCase):
    def setUp(self):
        self.data_collector = DataCollector()
        self.link_collector = DataLinkCollector()

    def test_extract_links_from_html(self):
        """
        methodology: to find an HTML body, count the number of typed links in it,
        and assert the number of links extracted is the same as the number of links
        counted
        """
        links = self.link_collector.get_typed_links_from_body(
            landing_html=mock_html_pangea_908011, landing_url=""
        )
        self.assertEqual(len(links), 12)

        links = self.link_collector.get_typed_links_from_body(
            landing_html=mock_html_2, landing_url=""
        )
        self.assertEqual(len(links), 1)

    def test_extract_links_from_metadata(self):
        path = "tests/data_for_testing/pangaea-metadata-in-schema.org.json"
        with open(path, "r") as file:
            text = file.read()
            metadata_record = MetadataRecord(
                is_machine_retrieved=False, raw_value=json.loads(text)
            )
            links = self.link_collector.get_typed_links_from_metadata_record(
                metadata_record
            )
            self.assertEqual(len(links), 2)

    @unittest.skip("TODO: Solve network error on retrieve_all_data")
    def test_retrieve_all_data(self):
        links = []
        links += self.link_collector.get_typed_links_from_body(
            landing_html=mock_html_pangea_908011, landing_url=""
        )
        links += self.link_collector.get_typed_links_from_metadata_record(
            metadata_record=MetadataRecord(
                is_machine_retrieved=False, raw_value=mock_metadata
            )
        )
        all_links = remove_duplicates(links)
        data = self.data_collector.retrieve_all_data(all_links, 1)
        data_list = list(data)
        self.assertTrue(any(data_list), lambda datum: datum.claimed_size == 902.0)
        links += self.link_collector.get_typed_links_from_metadata_record(
            metadata_record=MetadataRecord(
                is_machine_retrieved=False, raw_value=mock_metadata_with_size
            )
        )
        self.assertTrue(any(data_list), lambda datum: datum.claimed_size == 10_891)
