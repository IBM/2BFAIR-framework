from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.unique_identifier_evaluator import (
    UniqueIdentifierEvaluator,
)
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo


class TestF1Evaluation(FAIRnessPrincipleEvaluationTester):

    def setUp(self):
        self.identifier_evaluator = UniqueIdentifierEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )
        evaluator = self.identifier_evaluator
        self.F1_02MD_1_evaluating_method = (
            evaluator._evaluate_identifier_syntax_against_persistence_schema_f1_02md_1
        )

    def test_persistent_guid_identifier(self):
        identifier_info: IdentifierInfo = IdentifierInfo(
            identifier="https://doi.org/10.5334/dsj-2020-041",
            identifier_schemas=["doi", "url"],
            preferred_schema="doi",
            url="https://doi.org/10.5334/dsj-2020-041",
        )
        identifier_type = identifier_info.get_identifier_type()
        result = self.identifier_evaluator._evaluate_identifier_type_f1_01md_1(
            identifier_type=identifier_type
        )
        self.assert_test_failed(result)
        result = self.identifier_evaluator._evaluate_identifier_is_guid_f1_01md_2(
            identifier_type=identifier_type,
            preferred_schema=identifier_info.preferred_schema,
        )
        self.assert_test_passed(result)
        result = self.F1_02MD_1_evaluating_method(
            preferred_schema=identifier_info.preferred_schema
        )
        self.assert_test_passed(result)

    def test_non_persistent_guid_identifier(self):
        url = (
            "https://danielskatzblog.wordpress.com"
            "/2017/06/22/fair-is-not-fair-enough/"
        )
        identifier_info = IdentifierInfo(
            identifier=url, identifier_schemas=["url"], preferred_schema="url", url=url
        )
        identifier_type = identifier_info.get_identifier_type()
        result = self.identifier_evaluator._evaluate_identifier_is_guid_f1_01md_2(
            identifier_type=identifier_type,
            preferred_schema=identifier_info.preferred_schema,
        )
        self.assert_test_passed(result)
        result = self.identifier_evaluator._evaluate_identifier_type_f1_01md_1(
            identifier_type=identifier_type
        )
        self.assert_test_failed(result)
        result = self.F1_02MD_1_evaluating_method(
            preferred_schema=identifier_info.preferred_schema
        )
        self.assert_test_failed(result)

    def test_broken_link_identifier(self):
        invalid_ip_url = "http://0.0.0.0:8000/"
        always_broken_identifier_info = IdentifierInfo(
            identifier=invalid_ip_url,
            identifier_schemas=["url"],
            preferred_schema="url",
            url=invalid_ip_url,
        )
        identifier_type = always_broken_identifier_info.get_identifier_type()
        result = self.identifier_evaluator._evaluate_identifier_is_guid_f1_01md_2(
            identifier_type=identifier_type,
            preferred_schema=always_broken_identifier_info.preferred_schema,
        )
        self.assert_test_passed(result)
        result = self.identifier_evaluator._evaluate_identifier_type_f1_01md_1(
            identifier_type=identifier_type
        )
        self.assert_test_failed(result)
        result = self.F1_02MD_1_evaluating_method(
            preferred_schema=always_broken_identifier_info.preferred_schema
        )
        self.assert_test_failed(result)

    def test_hash_identifier(self):
        mock_hash_info = IdentifierInfo(
            identifier=(
                "466e503607a0b9838a6d1c09fd2a21a926c92f9dd8249929822f64643dcd9534"
            )
        )
        identifier_type = mock_hash_info.get_identifier_type()
        result = self.identifier_evaluator._evaluate_identifier_type_f1_01md_1(
            identifier_type=identifier_type
        )
        self.assert_test_passed(result)
        result = self.F1_02MD_1_evaluating_method(
            preferred_schema=mock_hash_info.preferred_schema
        )
        self.assert_test_failed(result)

    def test_uuid_identifier(self):
        identifier_info = IdentifierInfo(
            identifier="70f926a6-6cb8-445c-9026-3fa36fa31f7e",
        )
        identifier_type = identifier_info.get_identifier_type()

        result = self.identifier_evaluator._evaluate_identifier_type_f1_01md_1(
            identifier_type=identifier_type
        )
        self.assert_test_passed(result)
        result = self.F1_02MD_1_evaluating_method(
            preferred_schema=identifier_info.preferred_schema
        )
        self.assert_test_failed(result)
