import re
from typing import Iterable, List

import jmespath

from tobefair_backend.model.file_format import mime_types
from tobefair_backend.model.resources.data_record import DataType
from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_backend.repository.file_format_repository import FileFormatRepository
from tobefair_backend.repository.metadata_standard_repository import (
    MetadataStandardRepository,
)
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
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.metadata.metadata_standard import (
    MetadataStandard,
    MetadataStandardType,
)
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.R1_3.value)
class CommunityMetadataEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_record: MetadataRecord | None = evaluation_subject.metadata_record
        metadata_standard: MetadataStandard | None = (
            MetadataStandardRepository.get_metadata_standards_by_name(
                metadata_record.metadata_standard_name
            )
            if metadata_record and metadata_record.metadata_standard_name
            else None
        )
        standards_1 = self.get_test_community_required_metadata_standards(
            FAIRnessTestIDs.R1_3_01M_3_multidisciplinary_community_endorsed_metadata.value  # noqa: E501
        )
        standards_2 = self.get_test_community_required_metadata_standards(
            FAIRnessTestIDs.R1_3_01M_1_community_specific_metadata.value
        )
        return [
            self._evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(
                metadata_standard, standards_1
            ),
            self._evaluate_community_specific_metadata_f1_3_01m_1(
                metadata_standard, standards_2
            ),
            self._evaluate_community_endorsed_file_format_used_r1_3_02d_1(
                metadata_record=metadata_record
            ),
        ]

    def get_test_community_required_metadata_standards(
        self, test_id: FAIRnessTestID
    ) -> Iterable[MetadataStandard]:
        test_configuration = self._tests_configuration[test_id]
        community_required_metadata_standard_uris = (
            test_configuration.agnostic_requirements or {}
        ).get("metadata_standards") or []
        community_required_metadata_standards = (
            MetadataStandardRepository.metadata_standards_from_external_id_uris(
                uris=community_required_metadata_standard_uris
            )
        )
        return community_required_metadata_standards

    @fairness_test(
        FAIRnessTestIDs.R1_3_01M_3_multidisciplinary_community_endorsed_metadata.value
    )
    def _evaluate_multidisciplinary_community_endorsed_metadata_r1_3_01m_3(
        self,
        metadata_standard: MetadataStandard | None,
        community_required_metadata_standards: Iterable[MetadataStandard],
    ) -> TestResult:
        test_id = (
            FAIRnessTestIDs.R1_3_01M_3_multidisciplinary_community_endorsed_metadata.value  # noqa: E501
        )
        test_configuration = self._tests_configuration[test_id]
        if metadata_standard is None:
            return test_configuration.make_missing_requirements_test_result()
        if (
            metadata_standard.type is not None
            and metadata_standard.type == MetadataStandardType.Generic
            and metadata_standard in community_required_metadata_standards
        ):
            return test_configuration.make_passed_test_result()
        else:
            return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.R1_3_01M_1_community_specific_metadata.value)
    def _evaluate_community_specific_metadata_f1_3_01m_1(
        self,
        metadata_standard: MetadataStandard | None,
        community_required_metadata_standards: Iterable[MetadataStandard],
    ) -> TestResult:
        test_id = FAIRnessTestIDs.R1_3_01M_1_community_specific_metadata.value
        test_configuration = self._tests_configuration[test_id]
        if metadata_standard is None:
            return test_configuration.make_missing_requirements_test_result()
        if (
            metadata_standard.type is not None
            and metadata_standard.type == MetadataStandardType.Disciplinary
            and metadata_standard in community_required_metadata_standards
        ):
            return test_configuration.make_passed_test_result()
        else:
            return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.R1_3_02D_1_community_endorsed_file_format.value)
    def _evaluate_community_endorsed_file_format_used_r1_3_02d_1(
        self, metadata_record: MetadataRecord | None
    ) -> TestResult:
        test_id = FAIRnessTestIDs.R1_3_02D_1_community_endorsed_file_format.value
        test_configuration = self._tests_configuration[test_id]
        if not metadata_record:
            return test_configuration.make_missing_requirements_test_result()
        # this regex checks whether the mime type is text/xml, text/text or text/json
        # or text/+xml, text/+text or text/+json
        text_format_regex = r"(^text)[\/]|[\/\+](xml|text|json)"
        jmespath_query = (
            "(distribution[*].{url: (contentUrl || url), "
            "type: (encodingFormat || fileFormat), size: (contentSize || fileSize),"
            " profile: schemaVersion} || [distribution.{url: (contentUrl || url), "
            "type: (encodingFormat || fileFormat), size: (contentSize || fileSize)"
            ", profile: schemaVersion}])"
        )
        results = jmespath.search(jmespath_query, metadata_record.raw_value)

        for data in results:
            if data:
                if DataType(value=data["type"]) in mime_types(
                    FileFormatRepository.science_file_formats()
                    + FileFormatRepository.long_term_file_formats()
                    + FileFormatRepository.open_file_formats()
                ) or re.search(text_format_regex, data["type"]):
                    result_details = f"Found data file with  '{data['type']}' format."
                    return test_configuration.make_passed_test_result(
                        result_details=result_details
                    )

        return test_configuration.make_failed_test_result()
