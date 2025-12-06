from typing import List

from tobefair_backend.collector.metadata_source_repository_app import (
    MetadataSourceRepositoryApp,
)
from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.metadata.metadata_keys import MetadataSourceKeys
from tobefair_framework.model.metadata.metadata_source import MetadataSource
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.I1.value)
class FormalMetadataEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_source: MetadataSource | None = (
            MetadataSourceRepositoryApp.metadata_source_with_key(
                str(evaluation_subject.metadata_record.metadata_source_key.value)
            )
            if evaluation_subject.metadata_record
            and evaluation_subject.metadata_record.metadata_source_key
            else None
        )
        return [
            self._evaluate_parseable_structured_metadata_available_i1_01m_1(
                metadata_source=metadata_source
            )
        ]

    @fairness_test(
        FAIRnessTestIDs.I1_01M_1_parsable_structured_metadata_available.value
    )
    def _evaluate_parseable_structured_metadata_available_i1_01m_1(
        self, metadata_source: MetadataSource | None
    ):
        test_id = FAIRnessTestIDs.I1_01M_1_parsable_structured_metadata_available.value
        test_configuration = self._tests_configuration[test_id]
        if metadata_source is None:
            return test_configuration.make_missing_requirements_test_result()
        schemaorg_embedded: MetadataSource | None = (
            MetadataSourceRepositoryApp.metadata_source_with_key(
                MetadataSourceKeys.SCHEMA_ORG_EMBEDDED.value
            )
        )
        if schemaorg_embedded is None:
            return test_configuration.make_not_executed_test_result(
                result_description=(
                    "MetadataSourceRepository could not retrieve "
                    "Schema.org Embedded Metadata "
                    "which is a requirement to execute the test. "
                    "The developers should check the I1-01M-1 FAIRness test "
                    "implementation."
                ),
            )
        if metadata_source == schemaorg_embedded:
            return test_configuration.make_passed_test_result(
                result_details=(
                    "Metadata is provided in Schema.org vocabulary"
                    "and encoded in JSON-LD format,"
                    "which is parsable and structured."
                ),
            )

        return test_configuration.make_failed_test_result()
