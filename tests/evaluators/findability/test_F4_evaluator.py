# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.machine_accessible_metadata_evaluator import (  # noqa E501
    MachineAccessibleMetadataEvaluatorF4,
)
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus


class TestF4Evaluator(FAIRnessPrincipleEvaluationTester):
    def setUp(self):

        self.evaluator = MachineAccessibleMetadataEvaluatorF4(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )

    def test_dataset_with_minimum_requirements(self):
        metadata_record = MetadataRecord(
            is_machine_retrieved=True,
            raw_value={"@type": "Dataset", "name": "test", "description": "test"},
        )

        test_result = (
            self.evaluator._evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
                metadata_record
            )
        )

        self.assertTrue(test_result.score > 0)

    def test_dataset_without_minimum_requirements(self):
        metadata_record = MetadataRecord(
            is_machine_retrieved=True, raw_value={"@type": "Dataset", "name": "test"}
        )

        test_result = (
            self.evaluator._evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
                metadata_record
            )
        )

        self.assertTrue(test_result.score == 0)

    def test_article_minimum_requirements(self):
        metadata_record = MetadataRecord(
            is_machine_retrieved=True,
            raw_value={"@type": "Article"},
        )

        test_result = (
            self.evaluator._evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
                metadata_record
            )
        )

        self.assertTrue(test_result.score > 0)

    def test_different_object_type(self):
        metadata_record = MetadataRecord(
            is_machine_retrieved=True, raw_value={"@type": "Event", "name": "test"}
        )

        test_result = (
            self.evaluator._evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
                metadata_record
            )
        )

        self.assertTrue(test_result.status == TestExecutionStatus.not_executed)

    def test_metadata_not_machine_retrieved(self):
        metadata_record = MetadataRecord(
            is_machine_retrieved=False,
            raw_value={"name": "test", "description": "test"},
        )

        test_result = (
            self.evaluator._evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
                metadata_record
            )
        )

        self.assertTrue(test_result.score == 0)
