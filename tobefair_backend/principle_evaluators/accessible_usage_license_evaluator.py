from typing import List

from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
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


@evaluator_of_principle(FAIRPrincipleIDs.R1_1.value)
class AccessibleUsageLicenseMetadataEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_record: MetadataRecord | None = evaluation_subject.metadata_record
        return [
            self._evaluate_usage_license_information_available_r1_1_01m_1(
                metadata_record
            )
        ]

    @fairness_test(FAIRnessTestIDs.R1_1_01M_1_license_information_available.value)
    def _evaluate_usage_license_information_available_r1_1_01m_1(
        self, metadata_record: MetadataRecord | None
    ) -> TestResult:
        test_id = FAIRnessTestIDs.R1_1_01M_1_license_information_available.value
        test_configuration = self._tests_configuration[test_id]
        license_key = (
            test_configuration.agnostic_requirements["license_metadata_key"]
            if test_configuration.agnostic_requirements is not None
            and "license_metadata_key"
            in test_configuration.agnostic_requirements.keys()
            else None
        )
        if metadata_record:
            if license_information := (
                MetadataCollectorSchemaOrgJsonLD.get_license_information(
                    schemaorg_raw_value=metadata_record.raw_value,
                    license_metadata_key=license_key,
                )
            ):
                return test_configuration.make_passed_test_result(
                    result_details=f"Found license {license_information.raw_value}"
                )
            return test_configuration.make_failed_test_result()
        else:
            return test_configuration.make_missing_requirements_test_result()
