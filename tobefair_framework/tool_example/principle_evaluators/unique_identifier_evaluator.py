# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List

from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo
from tobefair_framework.model.identifier.identifier_type import IdentifierType
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.F1.value)
class UniqueIdentifierEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        identifier_info: IdentifierInfo = evaluation_subject.identifier_info
        identifier_type: IdentifierType = identifier_info.get_identifier_type()
        test_results: List[TestResult] = []
        if FAIRnessTestIDs.F1_01MD_1_Hash_or_UUID.value in self._tests_configuration:
            test_results.append(
                self._evaluate_identifier_type_hash_or_uuid_f1_01md_1(
                    identifier_type=identifier_type
                )
            )
        if FAIRnessTestIDs.F1_01MD_2_GUID.value in self._tests_configuration:
            test_results.append(
                self._evaluate_identifier_is_guid_f1_01md_2(
                    identifier_type=identifier_type,
                    preferred_schema=identifier_info.preferred_schema,
                )
            )
        return test_results

    def _evaluate_identifier_type_hash_or_uuid_f1_01md_1(
        self, identifier_type: IdentifierType
    ) -> TestResult:
        test_id = FAIRnessTestIDs.F1_01MD_1_Hash_or_UUID.value
        test_configuration = self._tests_configuration[test_id]
        if (
            identifier_type == IdentifierType.UUID
            or identifier_type == IdentifierType.HASH
        ):
            prefix = "an" if identifier_type == IdentifierType.UUID else "a"
            result_details = (
                f"Identifier follows {prefix} {identifier_type} type syntax."
            )
            test_result = test_configuration.make_passed_test_result(
                result_details=result_details,
            )
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result

    def _evaluate_identifier_is_guid_f1_01md_2(
        self, identifier_type: IdentifierType, preferred_schema: str | None
    ) -> TestResult:
        test_id = FAIRnessTestIDs.F1_01MD_2_GUID.value
        test_configuration = self._tests_configuration[test_id]
        evaluated_requirements = test_configuration.agnostic_requirements
        if identifier_type == IdentifierType.GUID:
            assert (
                preferred_schema
            ), "Preferred schema cannot be None if the identifier is a GUID"
            description = (
                "Identifier follows a defined unique identifier syntax "
                f"({preferred_schema})."
            )
            test_result = test_configuration.make_passed_test_result(
                result_description=description,
                evaluated_requirements=evaluated_requirements,
            )
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result
