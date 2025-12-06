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


@evaluator_of_principle(FAIRPrincipleIDs.F4.value)
class MachineAccessibleMetadataEvaluatorF4(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_record: MetadataRecord | None = evaluation_subject.metadata_record
        return [
            self._evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
                metadata_record
            )
        ]

    @fairness_test(
        FAIRnessTestIDs.F4_01M_1_metadata_retrievable_by_search_engines.value
    )
    def _evaluate_metadata_retrievable_by_search_engines_f4_01m_1(
        self,
        metadata_record: MetadataRecord | None,
    ):
        test_id = FAIRnessTestIDs.F4_01M_1_metadata_retrievable_by_search_engines.value
        test_configuration = self._tests_configuration[test_id]

        if not metadata_record:
            test_result = test_configuration.make_missing_requirements_test_result()
            return test_result

        if metadata_record.is_machine_retrieved:
            if (
                requirements := test_configuration.get_requirements_by_object_type(
                    digital_object_type=metadata_record.raw_value.get("@type", ""),
                    requirements_key="required_properties",
                )
            ) is not None:
                if set(requirements).issubset(metadata_record.raw_value):
                    msg = (
                        "Metadata is given in JSON-LD "
                        "which can be ingested in the catalogs of major search engines "
                        "and minimum required properties: "
                    )
                    result_details = msg + str(requirements) + " were found."
                    test_result = test_configuration.make_passed_test_result(
                        result_details=result_details,
                        evaluated_requirements=requirements,
                    )
                else:
                    missing_properties = list(
                        set(requirements) - set(metadata_record.raw_value)
                    )
                    msg = (
                        "Metadata is given in JSON-LD "
                        "which can be ingested in the catalogs of major search engines "
                        "but not all minimum required properties were found. "
                    )
                    msg = msg + "The following ones are missing: "
                    result_details = msg + str(missing_properties) + "."
                    test_result = test_configuration.make_failed_test_result(
                        result_details=result_details,
                        evaluated_requirements=requirements,
                    )
            else:
                result_description = (
                    "Test not executed: No minimum required properties "
                    "were found for your object type."
                )

                result_details = (
                    "Include the minimum requirements to your object type "
                    "in the fairness configuration file."
                )

                test_result = test_configuration.make_not_executed_test_result(
                    result_description=result_description, result_details=result_details
                )
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result
