# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
)
from tobefair_backend.principle_evaluators.metadata_uses_semantic_resources import (
    NamespaceEvaluator,
)
from tobefair_backend.repository.metadata_standard_repository import (
    MetadataStandardRepository,
)
from tobefair_framework.model.metadata.metadata_keys import (
    get_metadata_standard_name_from_str,
)
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class TestI201Metric(TestCase):
    def setUp(self) -> None:
        self.evaluator = NamespaceEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        path = "tests/data_for_testing/mock_community_metadata_standards.json"
        with open(path, "r") as file:
            self.community_required_metadata_standards = (
                MetadataStandardRepository.parse_json(file.read())
            )

    def test_i2_01m_1_metadata_uses_semantic_resources(self):
        mock_metadata_record = MetadataRecord(is_machine_retrieved=False, raw_value={})
        mock_metadata_record.metadata_standard_name = (
            get_metadata_standard_name_from_str(
                self.community_required_metadata_standards[1].name,
            )
        )
        result = self.evaluator._extract_namespaces_available_i2_01m_1(
            mock_metadata_record, accepted_namespaces=["schema.org"]
        )
        self.assertTrue(result)

    def test_i2_01m_1_metadata_not_uses_semantic_resources(self):
        mock_metadata_record = MetadataRecord(is_machine_retrieved=False, raw_value={})
        mock_metadata_record.metadata_standard_name = (
            get_metadata_standard_name_from_str(
                self.community_required_metadata_standards[1].name,
            )
        )
        result = self.evaluator._extract_namespaces_available_i2_01m_1(
            mock_metadata_record, accepted_namespaces=["schema.org"]
        )
        self.assertTrue(result)
