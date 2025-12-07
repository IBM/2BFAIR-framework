# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.metadata_richness_evaluator import (
    MetadataRichnessEvaluatorF2,
)
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.identifier.identifier_info import mocked_identifier_info
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class TestF2Evaluation(FAIRnessPrincipleEvaluationTester):
    def setUp(self):
        self.metadata_richness_evaluator = MetadataRichnessEvaluatorF2(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        self.complete_citation_description_metadata = {
            "name": (
                "Maximum diameter of Neogloboquadrina pachyderma sinistral"
                "from surface sediment samples from the Norwegian-Greenland Sea"
            ),
            "@type": "Dataset",
            "datePublished": None,
            "modified_date": None,
            "creator": "Robert Huber",
            "creator_first": "Robert",
            "creator_last": "Huber",
            "contributor": None,
            "right_holder": None,
            "publisher": "PANGAEA",
            "license": ["https://creativecommons.org/licenses/by/4.0/"],
            "description": (
                "This data set contains unpublished measurements of the maximum "
                "diameter of shells of the planktic foraminifer Neogloboquadrina "
                "pachyderma sin. carried out on surface sediment samples from the "
                "Norwegian-Greenland Sea."
            ),
            "keywords": None,
            "identifier": ["https://doi.org/10.1594/PANGAEA.908011"],
            "access_level": None,
            "access_free": None,
            "measured_variable": None,
            "object_size": None,
            "object_content_identifier": [None],
            "language": None,
        }
        self.incomplete_citation_metadata = (
            self.complete_citation_description_metadata.copy()
        )
        del self.incomplete_citation_metadata["creator"]
        self.incomplete_description_metadata = (
            self.complete_citation_description_metadata.copy()
        )
        del self.incomplete_description_metadata["keywords"]

    def test_digital_object_payload_contains_required_citation_description_metadata(
        self,
    ):
        payload = self.complete_citation_description_metadata
        mock_digital_object = self.mock_digital_object_from(payload)
        results = self.metadata_richness_evaluator.get_dimension_results(
            evaluation_subject=mock_digital_object,
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS,
        )
        f2_01m_1_result = results.get_test_result_with_id(
            FAIRnessTestIDs.F2_01M_1_citation_metadata.value
        )
        assert f2_01m_1_result is not None
        self.assert_test_passed(f2_01m_1_result)

        f2_01m_2_result = results.get_test_result_with_id(
            FAIRnessTestIDs.F2_01M_2_description_metadata.value
        )
        assert f2_01m_2_result is not None
        self.assert_test_passed(f2_01m_2_result)

    def mock_digital_object_from(self, payload) -> DigitalObjectInfo:
        mock_digital_object = DigitalObjectInfo(
            identifier_info=mocked_identifier_info,
            metadata_record=MetadataRecord(
                is_machine_retrieved=False, raw_value=payload
            ),
            landing_page=None,
        )

        return mock_digital_object

    def test_incomplete_citation_metadata(
        self,
    ):
        payload = self.incomplete_citation_metadata
        mock_digital_object_info = self.mock_digital_object_from(payload)
        results = self.metadata_richness_evaluator.get_dimension_results(
            evaluation_subject=mock_digital_object_info,
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS,
        )
        f2_01m_1_result = results.get_test_result_with_id(
            FAIRnessTestIDs.F2_01M_1_citation_metadata.value
        )
        assert f2_01m_1_result is not None
        self.assert_test_failed(
            ignored_attributes=["recommendation_details"], test_result=f2_01m_1_result
        )
        f2_01m_2_result = results.get_test_result_with_id(
            FAIRnessTestIDs.F2_01M_2_description_metadata.value
        )
        assert f2_01m_2_result is not None
        self.assert_test_failed(
            ignored_attributes=["recommendation_details"], test_result=f2_01m_2_result
        )
        # require descriptive metadata contain the required citation metadata

    def test_incomplete_description_metadata(
        self,
    ):
        payload = self.incomplete_description_metadata
        mock_digital_object_info = self.mock_digital_object_from(payload)
        results = self.metadata_richness_evaluator.get_dimension_results(
            evaluation_subject=mock_digital_object_info,
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS,
        )
        f2_01m_1_result = results.get_test_result_with_id(
            FAIRnessTestIDs.F2_01M_1_citation_metadata.value
        )
        assert f2_01m_1_result is not None
        self.assert_test_passed(f2_01m_1_result)
        f2_01m_2_result = results.get_test_result_with_id(
            FAIRnessTestIDs.F2_01M_2_description_metadata.value
        )
        assert f2_01m_2_result is not None
        self.assert_test_failed(
            ignored_attributes=["recommendation_details"], test_result=f2_01m_2_result
        )
