# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List

from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.F3.value)
class IdentifierInMetadataEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata: dict | None = (
            metadata_record.raw_value
            if (metadata_record := evaluation_subject.metadata_record)
            else None
        )
        return [
            self._evaluate_metadata_contains_data_identifier_f3_01m_1(metadata),
            self._evaluate_metadata_contains_metadata_identifier_f3_02m_1(
                metadata=metadata,
                digital_object_identifier=evaluation_subject.identifier_info.identifier,
            ),
        ]

    def _evaluate_json_ld_contains_metadata_info(
        self, json_ld_metadata: dict, meta_data_identifier: str
    ) -> bool:
        json_ld_metadata_str = str(json_ld_metadata)
        return meta_data_identifier in json_ld_metadata_str

    @fairness_test(FAIRnessTestIDs.F3_01M_1_metadata_contains_data_identifier.value)
    def _evaluate_metadata_contains_data_identifier_f3_01m_1(
        self, metadata: dict | None
    ):
        test_id = FAIRnessTestIDs.F3_01M_1_metadata_contains_data_identifier.value
        test_configuration = self._tests_configuration[test_id]
        if not metadata:
            return test_configuration.make_missing_requirements_test_result()

        object_type = metadata.get("@type", "")

        if requirements := test_configuration.get_requirements_by_object_type(
            digital_object_type=object_type,
            requirements_key="fields_to_search",
        ):
            for requirement in requirements:
                if len(metadata.get(requirement, "")) > 0:
                    return test_configuration.make_passed_test_result()
            return test_configuration.make_failed_test_result()

        else:
            result_description = (
                "Test not executed: This test was not configured nor implemented "
                f"for objects of type {object_type}."
            )

            result_details = (
                "This test was not configured nor implemented for objects "
                f"of type '{object_type}'. "
                f"Developers should update F3-01M-1 FAIRness test implementation so "
                f"that it is applicable to objects of type '{object_type}'"
            )

            return test_configuration.make_not_executed_test_result(
                result_description=result_description, result_details=result_details
            )

    @fairness_test(FAIRnessTestIDs.F3_02M_1_metadata_contains_metadata_identifier.value)
    def _evaluate_metadata_contains_metadata_identifier_f3_02m_1(
        self, metadata: dict | None, digital_object_identifier: str
    ):
        test_id = FAIRnessTestIDs.F3_02M_1_metadata_contains_metadata_identifier.value
        test_configuration = self._tests_configuration[test_id]
        if not metadata:
            return test_configuration.make_missing_requirements_test_result()
        metadata_contains_metadata_identifier = (
            self._evaluate_json_ld_contains_metadata_info(
                metadata, digital_object_identifier
            )
        )
        if metadata_contains_metadata_identifier:
            test_result = test_configuration.make_passed_test_result()
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result
