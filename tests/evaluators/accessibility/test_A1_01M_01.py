from unittest import TestCase

from tests.data_for_testing.sample_html_response import decoded_html_body_sample
from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
)
from tobefair_backend.principle_evaluators.standardized_protocol_evaluator import (
    StandardizedProtocolEvaluator,
)
from tobefair_framework.model.digital_object_info import mock_digital_object_info
from tobefair_framework.model.landing_page import LandingPage
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus


class TestA101Metric(TestCase):
    def test_a1_01m_1_with_conditions_of_access(self):
        digital_object = mock_digital_object_info()
        digital_object.metadata_record = MetadataRecord(
            is_machine_retrieved=True, raw_value={"conditionsOfAccess": "open"}
        )

        evaluator = StandardizedProtocolEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        test_result = evaluator._test_information_about_access_rights_in_metadata(
            digital_object
        )
        self.assertEqual(test_result.status, TestExecutionStatus.passed)

    def test_a1_01m_1_with_access_status(self):
        digital_object = mock_digital_object_info()
        digital_object.metadata_record = MetadataRecord(
            is_machine_retrieved=True, raw_value={"@type": "Dataset"}
        )
        digital_object.landing_page = LandingPage(
            url="https://teste.com",
            decoded_html_body=decoded_html_body_sample,
        )

        evaluator = StandardizedProtocolEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        test_result = evaluator._test_information_about_access_rights_in_metadata(
            digital_object
        )
        self.assertEqual(test_result.status, TestExecutionStatus.passed)

    def test_a1_01m_1_without_access_rights(self):
        digital_object = mock_digital_object_info()
        digital_object.metadata_record = MetadataRecord(
            is_machine_retrieved=True, raw_value={"@type": "Dataset"}
        )

        evaluator = StandardizedProtocolEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        test_result = evaluator._test_information_about_access_rights_in_metadata(
            digital_object
        )
        self.assertEqual(test_result.status, TestExecutionStatus.failed)
