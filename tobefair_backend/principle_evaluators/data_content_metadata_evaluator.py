# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List

import jmespath

from tobefair_backend.model.resources.data_record import DataRecord
from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_backend.utils.data_collector import DataCollector
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.recommendation import Recommendation
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.R1.value)
class DataContentMetadataEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        data_records = DataCollector().retrieve_data_from_digital_object(
            evaluation_subject
        )
        data_record: DataRecord | None = (
            data_records[0] if len(data_records) > 0 else None
        )
        return [
            self._test_minimal_information_about_data_content_available_f1_01m_1(
                evaluation_subject.metadata_record
            ),
            self._test_file_size_and_type_available_r1_01m_2(
                evaluation_subject.metadata_record
            ),
            self._test_measured_variable_available_f1_01m_3(data_record),
            self._test_file_type_matches_metadata_r1_01m_4(data_record),
            self._test_file_size_matches_metadata_r1_01m_5(data_record),
            self._test_variable_matches_metadata_f1_01m_6(data_record),
        ]

    @fairness_test(FAIRnessTestIDs.R1_01M_1_minimal_data_information_available.value)
    def _test_minimal_information_about_data_content_available_f1_01m_1(
        self, metadata_record: MetadataRecord | None
    ):
        test_id = FAIRnessTestIDs.R1_01M_1_minimal_data_information_available.value
        test_configuration = self._tests_configuration[test_id]
        if metadata_record is None:
            return test_configuration.make_missing_requirements_test_result(
                [metadata_record]
            )
        if required_metadata := test_configuration.get_requirements_by_object_type(
            requirements_key="resource_type"
        ):
            for metadata in required_metadata:
                if (
                    object_type := metadata_record.raw_value.get(metadata, None)
                ) is not None:
                    result_details = (
                        f"Found resource type metadata '{metadata}' "
                        f"with value '{object_type}'."
                    )
                    return test_configuration.make_passed_test_result(
                        result_details=result_details
                    )

            missing_requirements = list(
                set(required_metadata) - set(metadata_record.raw_value)
            )
            recommendations = test_configuration.get_requirements_recommendation()
            recommendation_details = "Resource type metadata were not found."
            for requirement in missing_requirements:
                if requirement in recommendations:
                    recommendation_details += " " + recommendations[requirement]

            return test_configuration.make_failed_test_result(
                recommendation_details=recommendation_details,
                evaluated_requirements=required_metadata,
            )
        else:
            result_description = (
                "Test not executed: Configuration error occurred during the execution "
                "of this test."
            )

            result_details = (
                "Developers should update R1-01M-1 FAIRness test configuration so "
                "that it includes an identifier of the metadata that represents the"
                "resource type."
            )

            return test_configuration.make_not_executed_test_result(
                result_description=result_description, result_details=result_details
            )

    @fairness_test(FAIRnessTestIDs.R1_01M_2_data_type_and_size_available.value)
    def _test_file_size_and_type_available_r1_01m_2(
        self, metadata_record: MetadataRecord | None
    ):
        test_id = FAIRnessTestIDs.R1_01M_2_data_type_and_size_available.value
        test_configuration = self._tests_configuration[test_id]
        if not metadata_record:
            return test_configuration.make_not_executed_test_result()
        type_attributes = test_configuration.get_requirements_by_object_type(
            requirements_key="type_attributes"
        )
        size_attributes = test_configuration.get_requirements_by_object_type(
            requirements_key="size_attributes"
        )

        if not type_attributes or not size_attributes:
            result_description = (
                "Test not executed: Minimum required criteria for size and type "
                "evaluation were not found in the configuration file."
            )

            result_details = (
                "Include the minimum criteria in the fairness configuration file."
            )

            return test_configuration.make_not_executed_test_result(
                result_description=result_description, result_details=result_details
            )

        type_expr = " || ".join(str(attr) for attr in type_attributes)
        size_expr = " || ".join(str(attr) for attr in size_attributes)

        jmespath_query = f"{{formats: {type_expr}, contentSize: {size_expr}}}"

        try:
            data = jmespath.search(jmespath_query, metadata_record.raw_value)

            if data["formats"] is None:
                return test_configuration.make_failed_test_result(
                    result_details="File type/format not found."
                )

            if data["contentSize"] is None:
                return test_configuration.make_failed_test_result(
                    result_details="File size not found."
                )

            return test_configuration.make_passed_test_result()

        except Exception:
            return test_configuration.make_failed_test_result()

    @fairness_test(
        FAIRnessTestIDs.R1_01M_3_measured_variable_information_available.value
    )
    def _test_measured_variable_available_f1_01m_3(
        self, data_record: DataRecord | None
    ):
        test_id = FAIRnessTestIDs.R1_01M_3_measured_variable_information_available.value
        test_configuration = self._tests_configuration[test_id]
        if data_record is None:
            return test_configuration.make_missing_requirements_test_result(
                [data_record]
            )
        measured_variable_given: bool = data_record.measured_variables is not None
        if measured_variable_given:
            return test_configuration.make_passed_test_result()
        return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.R1_01M_4_data_type_matches_metadata.value)
    def _test_file_type_matches_metadata_r1_01m_4(self, data_record: DataRecord | None):
        test_id = FAIRnessTestIDs.R1_01M_4_data_type_matches_metadata.value
        test_configuration = self._tests_configuration[test_id]
        if data_record is None:
            return test_configuration.make_missing_requirements_test_result(
                [data_record]
            )
        type_matches: bool = (
            data_record.header_content_type == data_record.claimed_type
            or data_record.claimed_type in data_record.tika_content_types
        ) and (
            data_record.header_content_type is not None
            and data_record.claimed_type is not None
        )
        if type_matches:
            return test_configuration.make_passed_test_result()
        elif not type_matches and data_record.claimed_type is None:
            return test_configuration.make_failed_test_result(
                result_details=(
                    "This test failed because the metadata specify no content type."
                ),
                recommendation=Recommendation(
                    value="Specify the content type in the metadata"
                ),
                recommendation_details=[
                    (
                        "Verify what the metadata standard you "
                        "currently use specifies as content type."
                    ),
                    (
                        "Check the type of the content your metadata "
                        "refer to, and include it in the metadata."
                    ),
                ],
            )
        return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.R1_01M_5_data_size_matches_metadata.value)
    def _test_file_size_matches_metadata_r1_01m_5(self, data_record: DataRecord | None):
        test_id = FAIRnessTestIDs.R1_01M_5_data_size_matches_metadata.value
        test_configuration = self._tests_configuration[test_id]
        if data_record is None:
            return test_configuration.make_missing_requirements_test_result(
                [data_record]
            )
        size_matches: bool = (
            data_record.claimed_size == data_record.content_size
        ) and (
            data_record.claimed_size is not None
            and data_record.content_size is not None
        )
        if size_matches:
            return test_configuration.make_passed_test_result()
        elif not size_matches and data_record.claimed_size is None:
            return test_configuration.make_failed_test_result(
                result_details=(
                    "This test failed because the "
                    "metadata specify no size for the content."
                ),
                recommendation=Recommendation(
                    value="Specify the content's " "size in the metadata"
                ),
                recommendation_details=[
                    (
                        "Verify what the metadata standard you "
                        "currently use specifies as content size."
                    ),
                    (
                        "Check the size of the content your metadata "
                        "refer to, and include it in the metadata."
                    ),
                ],
            )
        return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.R1_01M_6_measured_variable_matches_metadata.value)
    def _test_variable_matches_metadata_f1_01m_6(self, data_record: DataRecord | None):
        test_id = FAIRnessTestIDs.R1_01M_6_measured_variable_matches_metadata.value
        test_configuration = self._tests_configuration[test_id]
        if data_record is None:
            return test_configuration.make_missing_requirements_test_result(
                [data_record]
            )
        any_variables_in_tika_metadata = [
            measured_variable in (data_record.tika_data_content or "")
            for measured_variable in data_record.measured_variables or []
        ]
        if any_variables_in_tika_metadata:
            return test_configuration.make_passed_test_result()
        return test_configuration.make_failed_test_result()
