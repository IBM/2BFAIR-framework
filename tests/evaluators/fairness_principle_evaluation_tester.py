# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict
from unittest import TestCase

from tobefair_backend.constants import FAIRNESS_CONFIGURATION_FILE_PATH
from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.model.configuration.fairness_test_configuration import (
    FAIRnessTestConfiguration,
)
from tobefair_framework.model.fairness_evaluation_maturity import FAIRnessMaturities
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.results.fairness_result import FAIRnessEvaluationResponse
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus
from tobefair_framework.model.results.test_result import TestResult


def _fairness_test_assertion(func):
    def wrapper(
        self,
        test_result: TestResult,
        key: FAIRnessTestConfiguration | None = None,
        use_key: bool = True,
        ignored_attributes: list[str] = [],
        **expected_values,
    ) -> None:
        if use_key:
            if key is None and not (
                key := self._test_configuration.get(test_result.test_id)
            ):
                self.fail("Key for FAIRness test assertion not supplied.")
        func(self, test_result, key, ignored_attributes, **expected_values)

    return wrapper


fairness_configuration_dao = FAIRnessConfigurationFileDAO(
    file_path=FAIRNESS_CONFIGURATION_FILE_PATH
)
FAIRNESS_CONFIGURATION_FOR_TESTS = fairness_configuration_dao.read_configuration()


class FAIRnessPrincipleEvaluationTester(TestCase):

    @property
    def _test_configuration(self) -> Dict[FAIRnessTestID, FAIRnessTestConfiguration]:
        fairness_configuration_dao = FAIRnessConfigurationFileDAO(
            file_path=FAIRNESS_CONFIGURATION_FILE_PATH
        )
        fairness_configuration = fairness_configuration_dao.read_configuration()
        return fairness_configuration.get_fairness_tests()

    def _assess_fairness_test(
        self,
        test_result: TestResult,
        key: FAIRnessTestConfiguration | None = None,
        ignored_attributes: list[str] = [],
        **expected_values,
    ):
        """
        ignored fields are not evaluated.
        if expected values are received, they are compared with the values of the
        test result.
        if a key is received, values of the key's attributes that are not received
        as expected values are compared with values of the test result.
        if a key is not received, the configuration for the test is used as key.
        """
        key_values = (
            {k: getattr(key, k) for k in key.model_fields if k not in expected_values}
            if key is not None
            else {}
        )
        expected_values.update(key_values)
        if not expected_values:
            raise Exception(
                "Result was not checked against any criteria "
                "(key unavailable and expected values empty)."
            )
        for attribute_name, expected_value in expected_values.items():
            if attribute_name in ignored_attributes:
                continue
            if received_value := getattr(test_result, attribute_name, None):
                self.assertEqual(
                    received_value,
                    expected_value,
                    f"Test id: {test_result.get_id.value}",
                )

    @_fairness_test_assertion
    def assert_test_failed(
        self,
        test_result: TestResult,
        key: FAIRnessTestConfiguration | None = None,
        ignored_attributes: list[str] = [],
        **expected_values,
    ):
        expected_values["maturity"] = FAIRnessMaturities.Incomplete.value
        expected_values["status"] = TestExecutionStatus.failed
        expected_values["score"] = 0
        self._assess_fairness_test(
            test_result=test_result,
            key=key,
            ignored_attributes=ignored_attributes,
            **expected_values,
        )

    @_fairness_test_assertion
    def assert_test_passed(
        self,
        test_result: TestResult,
        key: FAIRnessTestConfiguration | None = None,
        ignored_attributes: list[str] = [],
        **expected_values,
    ):
        if key is not None:
            expected_values["score"] = key.max_score
        expected_values["status"] = TestExecutionStatus.passed
        self._assess_fairness_test(
            test_result=test_result,
            key=key,
            ignored_attributes=ignored_attributes,
            **expected_values,
        )

    def assert_test_not_executed(
        self,
        test_result: TestResult,
        key: FAIRnessTestConfiguration | None = None,
        ignored_attributes: list[str] = [],
        **expected_values,
    ):
        expected_values["maturity"] = FAIRnessMaturities.Incomplete.value
        expected_values["status"] = TestExecutionStatus.not_executed
        self._assess_fairness_test(
            test_result=test_result,
            key=key,
            ignored_attributes=ignored_attributes,
            **expected_values,
        )

    def assess_fairness_evaluation_result(
        self,
        evaluation_result: FAIRnessEvaluationResponse,
        approved_tests_ids: list[FAIRnessTestID] = [],
        failed_test_ids: list[FAIRnessTestID] = [],
        not_executed_test_ids: list[FAIRnessTestID] = [],
        ignored_attributes: list[str] = [],
    ):
        all_test_results_dict = evaluation_result.detailed_results.test_result_dict
        for approved_test_id in approved_tests_ids:
            if result := all_test_results_dict.get(approved_test_id):
                self.assert_test_passed(
                    ignored_attributes=ignored_attributes, test_result=result
                )
        for failed_test_id in failed_test_ids:
            if result := all_test_results_dict.get(failed_test_id):
                self.assert_test_failed(
                    ignored_attributes=ignored_attributes, test_result=result
                )
        for not_executed_test_id in not_executed_test_ids:
            if result := all_test_results_dict.get(not_executed_test_id):
                self.assert_test_not_executed(
                    ignored_attributes=ignored_attributes, test_result=result
                )

    def assess_single_test_from_result(
        self,
        test_id: FAIRnessTestID,
        result: FAIRnessEvaluationResponse,
        key: FAIRnessTestConfiguration | None = None,
        ignored_fields: list[str] = [],
        **expected_values,
    ):
        if test_result := result.get_optional_test_result(test_id):
            self._assess_fairness_test(
                test_result, key, ignored_fields, **expected_values
            )

    def assert_all_tests_failed(self, evaluation_result: FAIRnessEvaluationResponse):
        all_test_results = evaluation_result.detailed_results.test_result_dict
        for result in all_test_results.values():
            self.assertTrue(
                result.status == TestExecutionStatus.failed
                or result.status == TestExecutionStatus.not_executed
            )
