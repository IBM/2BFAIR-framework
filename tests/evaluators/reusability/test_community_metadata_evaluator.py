from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.principle_evaluators.community_metadata_evaluator import (
    CommunityMetadataEvaluator,
)
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class TestCommunityMetadataEvaluator(FAIRnessPrincipleEvaluationTester):
    def setUp(self) -> None:
        self.evaluator = CommunityMetadataEvaluator(
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS,
        )
        self.mock_metadata_record = MetadataRecord(
            is_machine_retrieved=False,
            raw_value={
                "distribution": [
                    {
                        "@type": "DataDownload",
                        "contentUrl": "https://zenodo.org/api/records/8255910/files/ECHA_raw_RB_compounds.csv/content",  # noqa: E501
                        "encodingFormat": "text/csv",
                    }
                ]
            },
        )

    def test_empty_metadata_record(self):
        mock_metadata_record = MetadataRecord(is_machine_retrieved=False, raw_value={})
        result = (
            self.evaluator._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                mock_metadata_record
            )
        )
        self.assert_test_failed(
            result,
        )

    def test_invalid_data_record(self):
        metadata_record = self.mock_metadata_record

        metadata_record.raw_value["distribution"][0]["encodingFormat"] = "foo/cgm"
        result = (
            self.evaluator._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                metadata_record
            )
        )
        self.assert_test_failed(
            result,
        )

    def test_valid_data_record_long_term_file_format(self):
        metadata_record = self.mock_metadata_record
        metadata_record.raw_value["distribution"][0]["encodingFormat"] = "image/cgm"
        result = (
            self.evaluator._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                metadata_record
            )
        )
        self.assert_test_passed(
            result,
        )

    def test_valid_data_record_scientific_file_format(self):
        metadata_record = self.mock_metadata_record
        metadata_record.raw_value["distribution"][0][
            "encodingFormat"
        ] = "chemical/x-cif"
        result = (
            self.evaluator._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                metadata_record
            )
        )
        self.assert_test_passed(
            result,
        )

    def test_valid_data_record_open_file_format(self):
        metadata_record = self.mock_metadata_record
        metadata_record.raw_value["distribution"][0]["encodingFormat"] = "audio/mp4"
        result = (
            self.evaluator._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                metadata_record
            )
        )
        self.assert_test_passed(
            result,
        )

    def test_valid_xml_text_json_format(self):
        metadata_record = self.mock_metadata_record
        metadata_record.raw_value["distribution"][0][
            "encodingFormat"
        ] = "application/json"
        result = (
            self.evaluator._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                metadata_record
            )
        )
        self.assert_test_passed(
            result,
        )
