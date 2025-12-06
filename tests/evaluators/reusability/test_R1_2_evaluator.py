from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.detailed_provenance_metadata_evaluator import (  # noqa E501
    DetailedProvenanceMetadataEvaluator,
)
from tobefair_framework.model.metadata.metadata_keys import MetadataStandardName
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.metadata.metadata_standard import (
    ExternalID,
    MetadataStandard,
)


class TestR12Evaluator(FAIRnessPrincipleEvaluationTester):
    def setUp(self):
        self.evaluator = DetailedProvenanceMetadataEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
        )

    def test_r1_2_01m_1_passes(self):
        test_result = self.evaluator._evaluate_provenance_information_r1_2_01m_1(
            metadata_record=MetadataRecord(
                is_machine_retrieved=False,
                raw_value={
                    "publisher": "IBM Research Brazil",
                    "creator": "Foo",
                    "datePublished": "11/11/1111",
                },
            )
        )
        self.assert_test_passed(
            test_result,
        )

    def test_f1_2_01m_1_fails(self):
        test_result = self.evaluator._evaluate_provenance_information_r1_2_01m_1(
            metadata_record=MetadataRecord(
                is_machine_retrieved=False,
                raw_value={"publisher": "", "creator": "Foo"},
            )
        )
        self.assert_test_failed(
            test_result,
        )
        test_result = self.evaluator._evaluate_provenance_information_r1_2_01m_1(
            metadata_record=MetadataRecord(
                is_machine_retrieved=False,
                raw_value={"publisher": "IBM Research Brazil", "creator": ""},
            )
        )
        self.assert_test_failed(
            test_result,
        )

    def test_r1_2_01m_2_passes(self):
        accepted_provo_metadata_standard_uris = [
            "http://purl.org/pav",
            "http://www.w3.org/ns/prov",
        ]
        metadata_standard: MetadataStandard = MetadataStandard(
            name=str(MetadataStandardName.PROV),
            external_ids=[ExternalID(value=accepted_provo_metadata_standard_uris[0])],
        )
        test_result = self.evaluator._evaluate_metadata_schema_r1_2_01m_2(
            metadata_standard=metadata_standard,
        )
        self.assert_test_passed(
            test_result,
        )

    def test_r1_2_01m_2_fails(self):
        metadata_standard: MetadataStandard = MetadataStandard(
            name=str(MetadataStandardName.PROV), external_ids=[]
        )
        test_result = self.evaluator._evaluate_metadata_schema_r1_2_01m_2(
            metadata_standard=metadata_standard,
        )
        self.assert_test_failed(
            test_result,
        )

        metadata_standard: MetadataStandard = MetadataStandard(
            name="", external_ids=[ExternalID(value="wrong")]
        )
        test_result = self.evaluator._evaluate_metadata_schema_r1_2_01m_2(
            metadata_standard=metadata_standard,
        )
        self.assert_test_failed(
            test_result,
        )
