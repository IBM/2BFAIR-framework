# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List

from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_backend.repository.metadata_standard_repository import (
    MetadataStandardRepository,
)
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.metadata.metadata_standard import MetadataStandard
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.R1_2.value)
class DetailedProvenanceMetadataEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        metadata_record: MetadataRecord | None = evaluation_subject.metadata_record
        metadata_standard: MetadataStandard | None = (
            MetadataStandardRepository.get_metadata_standards_by_name(
                metadata_record.metadata_standard_name
            )
            if metadata_record and metadata_record.metadata_standard_name
            else None
        )
        return [
            self._evaluate_provenance_information_f1_2_01m_1(metadata_record),
            self._evaluate_metadata_schema_f1_2_01m_2(
                metadata_standard=metadata_standard
            ),
        ]

    @fairness_test(FAIRnessTestIDs.R1_2_01M_1_provenance_information_available.value)
    def _evaluate_provenance_information_f1_2_01m_1(
        self, metadata_record: MetadataRecord | None
    ) -> TestResult:
        test_id = FAIRnessTestIDs.R1_2_01M_1_provenance_information_available.value
        test_configuration = self._tests_configuration[test_id]
        if not metadata_record:
            return test_configuration.make_missing_requirements_test_result()

        if (
            required_provenance_metadata := (
                test_configuration.get_requirements_by_object_type(
                    requirements_key="provenance_metadata"
                )
            )
        ) is not None:
            set_required_provenance_metadata = set(required_provenance_metadata)
            found_metadata = set(metadata_record.raw_value)
            if set_required_provenance_metadata.issubset(found_metadata) and (
                all(
                    map(
                        lambda provenance_metadata_key: (
                            value := metadata_record.raw_value.get(
                                provenance_metadata_key
                            )
                        )
                        is not None
                        and value != "",
                        required_provenance_metadata,
                    )
                )
            ):
                return test_configuration.make_passed_test_result()

            missing_required_metadata = (
                set_required_provenance_metadata - found_metadata
            )
            msg = (
                "Not all required provenance metadata were found."
                "The following ones are missing: "
                f"{str(missing_required_metadata)}."
            )
            return test_configuration.make_failed_test_result(result_description=msg)

        else:
            return test_configuration.make_missing_requirements_test_result()

    @fairness_test(FAIRnessTestIDs.R1_2_01M_2_metadata_comply_to_standard_schema.value)
    def _evaluate_metadata_schema_f1_2_01m_2(
        self, metadata_standard: MetadataStandard | None
    ) -> TestResult:
        test_id = FAIRnessTestIDs.R1_2_01M_2_metadata_comply_to_standard_schema.value
        test_configuration = self._tests_configuration[test_id]
        if metadata_standard is not None:
            if (
                accepted_metadata_schemas := (
                    test_configuration.get_requirements_by_object_type(
                        requirements_key="accepted_metadata_schemas"
                    )
                )
            ) is not None:
                if (
                    set(metadata_standard.external_id_uris()).intersection(
                        set(accepted_metadata_schemas)
                    )
                    and list(metadata_standard.external_id_uris()) != []
                ):
                    return test_configuration.make_passed_test_result()
                return test_configuration.make_failed_test_result()

            else:
                return test_configuration.make_missing_requirements_test_result(
                    result_details=(
                        "Test not executed: "
                        "Accepted Metadata Schemas were not found."
                    ),
                )

        return test_configuration.make_missing_requirements_test_result()
