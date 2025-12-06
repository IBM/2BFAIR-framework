from typing import List

from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.I2.value)
class NamespaceEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_record: MetadataRecord | None = evaluation_subject.metadata_record
        accepted_namespaces: List | None = None
        if (
            test := self._tests_configuration.get(
                FAIRnessTestIDs.I2_01M_1_namespace_are_available.value
            )
        ) and (agnostic_requirements := test.agnostic_requirements):
            accepted_namespaces = agnostic_requirements.get("accepted_namespaces")
        return [
            self._extract_namespaces_available_i2_01m_1(
                metadata_record, accepted_namespaces
            ),
        ]

    @fairness_test(FAIRnessTestIDs.I2_01M_1_namespace_are_available.value)
    def _extract_namespaces_available_i2_01m_1(
        self,
        metadata_record: MetadataRecord | None,
        accepted_namespaces: List[str] | None,
    ) -> TestResult:
        test_id = FAIRnessTestIDs.I2_01M_1_namespace_are_available.value
        test_configuration = self._tests_configuration[test_id]
        if (
            metadata_record is not None
            and metadata_record.metadata_standard_name is not None
        ):
            if accepted_namespaces is None:
                return test_configuration.make_missing_requirements_test_result(
                    [accepted_namespaces],
                    result_details=(
                        "Test not executed: " "Accepted namespace were not found."
                    ),
                )

            if metadata_record.metadata_standard_name.value in accepted_namespaces:
                return test_configuration.make_passed_test_result()
            return test_configuration.make_failed_test_result()
        return test_configuration.make_not_executed_test_result()
