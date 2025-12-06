from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.community_metadata_evaluator import (
    CommunityMetadataEvaluator,
)
from tobefair_backend.repository.metadata_standard_repository import (
    MetadataStandardRepository,
)
from tobefair_framework.model.metadata.metadata_standard import (
    MetadataStandard,
    MetadataStandardType,
)


class TestR13Evaluator(FAIRnessPrincipleEvaluationTester):
    def setUp(self) -> None:
        self.evaluator = CommunityMetadataEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        path = "tests/data_for_testing/mock_community_metadata_standards.json"
        with open(path, "r") as file:
            self.community_required_metadata_standards = (
                MetadataStandardRepository.parse_json(file.read())
            )

    def test_f1_3_01m_3_evaluation_pass(self):
        metadata_standard: MetadataStandard = MetadataStandard(
            name=self.community_required_metadata_standards[0].name,
            type=MetadataStandardType.Generic,
        )
        result = self.evaluator._evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_passed(
            result,
        )

        metadata_standard.name = ""
        metadata_standard.external_ids = self.community_required_metadata_standards[
            0
        ].external_ids
        result = self.evaluator._evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_passed(
            result,
        )

    def test_r1_3_01m_3_evaluation_failed(self):
        metadata_standard = MetadataStandard(
            name=self.community_required_metadata_standards[0].name,
            type=MetadataStandardType.Disciplinary,
        )
        result = self.evaluator._evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_failed(
            result,
        )

        metadata_standard.name = ""
        metadata_standard.external_ids = self.community_required_metadata_standards[
            0
        ].external_ids
        result = self.evaluator._evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_failed(
            result,
        )

        metadata_standard.type = MetadataStandardType.Generic
        metadata_standard.name = ""
        metadata_standard.external_ids = []
        result = self.evaluator._evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_failed(
            result,
        )

    def test_r1_3_01m_1_evaluation_pass(self):
        metadata_standard: MetadataStandard = MetadataStandard(
            name=self.community_required_metadata_standards[0].name,
            type=MetadataStandardType.Disciplinary,
        )
        result = self.evaluator._evaluate_community_specific_metadata_r1_3_01m_1(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_passed(
            result,
        )

        metadata_standard.name = ""
        metadata_standard.external_ids = self.community_required_metadata_standards[
            0
        ].external_ids
        result = self.evaluator._evaluate_community_specific_metadata_r1_3_01m_1(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_passed(
            result,
        )

    def test_r1_3_01m_1_evaluation_fail(self):
        metadata_standard: MetadataStandard = MetadataStandard(
            name=self.community_required_metadata_standards[0].name,
            type=MetadataStandardType.Generic,
        )
        result = self.evaluator._evaluate_community_specific_metadata_r1_3_01m_1(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_failed(
            result,
        )

        metadata_standard.name = ""
        metadata_standard.external_ids = self.community_required_metadata_standards[
            0
        ].external_ids
        result = self.evaluator._evaluate_community_specific_metadata_r1_3_01m_1(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_failed(
            result,
        )

        metadata_standard.type = MetadataStandardType.Disciplinary
        metadata_standard.name = ""
        metadata_standard.external_ids = []
        result = self.evaluator._evaluate_community_specific_metadata_r1_3_01m_1(  # noqa: E501
            metadata_standard=metadata_standard,
            community_required_metadata_standards=(
                self.community_required_metadata_standards
            ),
        )
        self.assert_test_failed(
            result,
        )
