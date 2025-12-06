from typing import Callable, Dict, List, TypeAlias

from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD as MtdtColSchOrgJsLd,
)
from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import (
    FAIRnessTestID,
    FAIRnessTestIDs,
)
from tobefair_framework.model.results.test_result import TestResult

TestEvaluatingMethod: TypeAlias = Callable


@evaluator_of_principle(FAIRPrincipleIDs.F2.value)
class MetadataRichnessEvaluatorF2(PrincipleEvaluator):
    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_dict: Dict | None = (
            metadata_record.raw_value
            if (metadata_record := evaluation_subject.metadata_record)
            else None
        )
        metadata_dict = (
            schemaorg_metadata.raw_value
            if (metadata_dict is not None)
            and (
                schemaorg_metadata := MtdtColSchOrgJsLd.get_schema_org_metadata(
                    metadata_dict
                )
            )
            else metadata_dict
        )
        return [
            self._evaluate_citation_metadata_f2_01m_1(metadata_dict),
            self._evaluate_description_metadata_f2_01m_2(metadata_dict),
        ]

    def _evaluate_metadata_requirements(
        self,
        metadata: dict | None,
        test_id: FAIRnessTestID,
        requirements_key: str,
        result_details_msg: str,
        recommendation_details_msg: str,
        passed_default_result_details_msg: str,
        failed_default_result_details_msg: str,
    ) -> TestResult:
        test_configuration = self._tests_configuration[test_id]

        if not metadata:
            return test_configuration.make_missing_requirements_test_result()

        object_type = metadata.get("@type", "")
        requirements = test_configuration.get_requirements_by_object_type(
            digital_object_type=object_type, requirements_key=requirements_key
        )

        if requirements:
            if set(requirements).issubset(metadata):
                return test_configuration.make_passed_test_result(
                    result_details=result_details_msg.format(requirements=requirements),
                    evaluated_requirements=requirements,
                )
            else:
                missing_requirements = list(set(requirements) - set(metadata))
                recommendations = test_configuration.get_requirements_recommendation(
                    digital_object_type=object_type
                )
                recommendation_details = recommendation_details_msg
                for requirement in missing_requirements:
                    if requirement in recommendations:
                        recommendation_details += " " + recommendations[requirement]

                return test_configuration.make_failed_test_result(
                    recommendation_details=recommendation_details,
                    evaluated_requirements=requirements,
                )

        if default_requirements := test_configuration.get_requirements_by_object_type(
            requirements_key=requirements_key
        ):
            if set(default_requirements).issubset(metadata):
                return test_configuration.make_passed_test_result(
                    result_details=passed_default_result_details_msg.format(
                        object_type=object_type, requirements=default_requirements
                    ),
                    evaluated_requirements=default_requirements,
                )
            else:
                missing_requirements = list(set(default_requirements) - set(metadata))
                recommendations = test_configuration.get_requirements_recommendation()
                recommendation_details = recommendation_details_msg
                for requirement in missing_requirements:
                    if requirement in recommendations:
                        recommendation_details += " " + recommendations[requirement]

                return test_configuration.make_failed_test_result(
                    result_details=failed_default_result_details_msg.format(
                        object_type=object_type
                    ),
                    recommendation_details=recommendation_details,
                    evaluated_requirements=default_requirements,
                )

        return test_configuration.make_not_executed_test_result(
            result_description=(
                "Test not executed: Specification for the required "
                f"{requirements_key} not found."
            )
        )

    @fairness_test(FAIRnessTestIDs.F2_01M_1_citation_metadata.value)
    def _evaluate_citation_metadata_f2_01m_1(self, metadata: dict | None) -> TestResult:
        return self._evaluate_metadata_requirements(
            metadata=metadata,
            test_id=FAIRnessTestIDs.F2_01M_1_citation_metadata.value,
            requirements_key="citation_metadata",
            result_details_msg=(
                "The metadata elements {requirements} were found according to the "
                "mapping defined in the implementation. Check test configuration or "
                "the implementation to get more details about the mapping."
            ),
            recommendation_details_msg="Not all core citation metadata were found.",
            passed_default_result_details_msg=(
                "This test was executed using the default configuration. It might not "
                "be the appropriate configuration for objects of type {object_type}. "
                "You can include the appropriate requirements in the fairness "
                "configuration file. Found required core citation metadata elements: "
                "{requirements}."
            ),
            failed_default_result_details_msg=(
                "This test was executed using the default configuration. It might not "
                "be the appropriate configuration for objects of type {object_type}. "
                "You can include the appropriate requirements in the fairness "
                "configuration file."
            ),
        )

    @fairness_test(FAIRnessTestIDs.F2_01M_2_description_metadata.value)
    def _evaluate_description_metadata_f2_01m_2(
        self, metadata: dict | None
    ) -> TestResult:
        return self._evaluate_metadata_requirements(
            metadata=metadata,
            test_id=FAIRnessTestIDs.F2_01M_2_description_metadata.value,
            requirements_key="description_metadata",
            result_details_msg=(
                "The metadata elements {requirements} were found according to the "
                "mapping defined in the implementation. Check test configuration or "
                "the implementation to get more details about the mapping."
            ),
            recommendation_details_msg="Not all core description metadata were found.",
            passed_default_result_details_msg=(
                "This test was executed using the default configuration. It might not "
                "be the appropriate configuration for objects of type {object_type}. "
                "You can include the appropriate requirements in the fairness "
                "configuration file. Found required core description metadata "
                "elements: {requirements}."
            ),
            failed_default_result_details_msg=(
                "This test was executed using the default configuration. It might not "
                "be the appropriate configuration for objects of type {object_type}. "
                "Not all required core description metadata were found."
            ),
        )
