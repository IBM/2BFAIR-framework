from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.accessible_usage_license_evaluator import (
    AccessibleUsageLicenseMetadataEvaluator,
)
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class TestR11LicenseEvaluator(FAIRnessPrincipleEvaluationTester):
    def setUp(self):
        self.evaluator = AccessibleUsageLicenseMetadataEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )

    def test_r1_1_01m_1_passes(self):
        test_result = (
            self.evaluator._evaluate_usage_license_information_available_r1_1_01m_1(
                metadata_record=MetadataRecord(
                    is_machine_retrieved=False,
                    raw_value={"license": "License Information"},
                )
            )
        )
        self.assert_test_passed(test_result)

    def test_r1_1_01m_1_fails(self):
        test_result = (
            self.evaluator._evaluate_usage_license_information_available_r1_1_01m_1(
                metadata_record=MetadataRecord(
                    is_machine_retrieved=False, raw_value={"license": ""}
                )
            )
        )
        self.assert_test_failed(test_result)

        test_result = (
            self.evaluator._evaluate_usage_license_information_available_r1_1_01m_1(
                metadata_record=MetadataRecord(is_machine_retrieved=False, raw_value={})
            )
        )
        self.assert_test_failed(test_result)
