# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
    FAIRnessPrincipleEvaluationTester,
)
from tobefair_backend.collector.digital_object_collector_from_url import (
    DigitalObjectCollectorFromURL,
)
from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
from tobefair_backend.constants import EVALUATORS_PACKAGE
from tobefair_framework.controller.evaluation_controller import EvaluationController
from tobefair_framework.model.fairness_evaluation_request import (
    FAIRnessEvaluationRequest,
)
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs


class TestMainIdentifiers(FAIRnessPrincipleEvaluationTester):
    def setUp(self) -> None:
        self.metadata_collector = MetadataCollectorSchemaOrgJsonLD()

        self.evaluation_controller = EvaluationController(
            digital_object_collector=DigitalObjectCollectorFromURL(),
            metadata_collector=self.metadata_collector,
            fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS,
        )

    def test_0000_identifier(self):
        result = self.evaluation_controller.evaluate(
            FAIRnessEvaluationRequest(resource_id="0000"),
            evaluators_package=EVALUATORS_PACKAGE,
        )
        self.assert_all_tests_failed(result)

    def is_main_identifier_available(self, main_identifier: str) -> bool:
        # The identifier landing page should be always available.
        # The test cannot be executed if it is not.
        # So, we are going to check the landing page availability before running the
        # unit test.
        digital_object_info = DigitalObjectCollectorFromURL().get_digital_object_info(
            raw_identifier=main_identifier, metadata_collector=self.metadata_collector
        )
        if not digital_object_info.landing_page:
            return False
        return True

    def test_pangaea_identifier(self):
        main_identifier: str = "https://doi.org/10.1594/PANGAEA.893286"
        if not self.is_main_identifier_available(main_identifier=main_identifier):
            return

        result = self.evaluation_controller.evaluate(
            FAIRnessEvaluationRequest(resource_id=main_identifier),
            evaluators_package=EVALUATORS_PACKAGE,
        )
        self.assess_fairness_evaluation_result(
            evaluation_result=result,
            ignored_attributes=["recommendation_details"],
            approved_tests_ids=[
                FAIRnessTestIDs.F1_01MD_2_GUID.value,
                FAIRnessTestIDs.F1_02MD_1_GUPRI.value,
                FAIRnessTestIDs.F2_01M_1_citation_metadata.value,
                FAIRnessTestIDs.F3_01M_1_metadata_contains_data_identifier.value,
                FAIRnessTestIDs.F4_01M_1_metadata_retrievable_by_search_engines.value,
                FAIRnessTestIDs.A1_01M_1_access_rights_info_in_metadata.value,
                FAIRnessTestIDs.A1_02M_1_identifier_resolves_to_landing_page.value,
                FAIRnessTestIDs.I1_01M_1_parsable_structured_metadata_available.value,
                FAIRnessTestIDs.R1_01M_1_minimal_data_information_available.value,
                FAIRnessTestIDs.R1_01M_2_data_type_and_size_available.value,
                FAIRnessTestIDs.R1_1_01M_1_license_information_available.value,
                FAIRnessTestIDs.R1_2_01M_1_provenance_information_available.value,
                FAIRnessTestIDs.R1_3_01M_3_multidisciplinary_community_endorsed_metadata.value,  # noqa: E501
            ],
            failed_test_ids=[
                FAIRnessTestIDs.F1_01MD_1_Hash_or_UUID.value,
                FAIRnessTestIDs.F2_01M_2_description_metadata.value,
                FAIRnessTestIDs.R1_01M_6_measured_variable_matches_metadata.value,
                FAIRnessTestIDs.R1_3_01M_1_community_specific_metadata.value,
            ],
        )
        self.assert_test_passed(
            result.get_test_result(
                FAIRnessTestIDs.R1_01M_4_data_type_matches_metadata.value
            ),
            ignored_fields=["recommendation", "recommendation_details"],
        )

    def test_embrapa_identifier(self):
        main_identifier: str = (
            "https://www.redape.dados.embrapa.br/"
            "dataset.xhtml?persistentId=doi:10.48432/1CY2AN"
        )
        if not self.is_main_identifier_available(main_identifier=main_identifier):
            return
        result = self.evaluation_controller.evaluate(
            FAIRnessEvaluationRequest(resource_id=main_identifier),
            evaluators_package=EVALUATORS_PACKAGE,
        )
        self.assess_fairness_evaluation_result(
            evaluation_result=result,
            approved_tests_ids=[
                FAIRnessTestIDs.F1_01MD_2_GUID.value,
                FAIRnessTestIDs.F2_01M_1_citation_metadata.value,
                FAIRnessTestIDs.F2_01M_2_description_metadata.value,
                FAIRnessTestIDs.F3_01M_1_metadata_contains_data_identifier.value,
                FAIRnessTestIDs.F4_01M_1_metadata_retrievable_by_search_engines.value,
                FAIRnessTestIDs.A1_02M_1_identifier_resolves_to_landing_page.value,
                FAIRnessTestIDs.A1_03M_1_standard_protocol_for_metadata.value,
                FAIRnessTestIDs.I1_01M_1_parsable_structured_metadata_available.value,
                FAIRnessTestIDs.R1_01M_1_minimal_data_information_available.value,
                FAIRnessTestIDs.R1_01M_4_data_type_matches_metadata.value,
                FAIRnessTestIDs.R1_01M_2_data_type_and_size_available.value,
                FAIRnessTestIDs.R1_01M_4_data_type_matches_metadata.value,
                FAIRnessTestIDs.R1_1_01M_1_license_information_available.value,
                FAIRnessTestIDs.R1_2_01M_1_provenance_information_available.value,
                FAIRnessTestIDs.R1_3_01M_3_multidisciplinary_community_endorsed_metadata.value,  # noqa: E501
            ],
            failed_test_ids=[
                FAIRnessTestIDs.F1_02MD_1_GUPRI.value,
                FAIRnessTestIDs.F2_01M_3.value,
                FAIRnessTestIDs.A1_01M_1_access_rights_info_in_metadata.value,
                FAIRnessTestIDs.R1_3_01M_1_community_specific_metadata.value,
            ],
        )

    def test_pubchem_identifier(self):
        main_identifier: str = "https://pubchem.ncbi.nlm.nih.gov/compound/Benzene"
        if not self.is_main_identifier_available(main_identifier=main_identifier):
            return
        result = self.evaluation_controller.evaluate(
            FAIRnessEvaluationRequest(resource_id=main_identifier),
            evaluators_package=EVALUATORS_PACKAGE,
        )
        self.assess_fairness_evaluation_result(
            evaluation_result=result,
            ignored_attributes=["recommendation_details"],
            approved_tests_ids=[
                FAIRnessTestIDs.F1_01MD_2_GUID.value,
                FAIRnessTestIDs.A1_02M_1_identifier_resolves_to_landing_page.value,
                FAIRnessTestIDs.A1_03M_1_standard_protocol_for_metadata.value,
                FAIRnessTestIDs.I1_01M_1_parsable_structured_metadata_available.value,
                FAIRnessTestIDs.R1_01M_1_minimal_data_information_available.value,
                FAIRnessTestIDs.R1_3_01M_3_multidisciplinary_community_endorsed_metadata.value,  # noqa: E501
            ],
            failed_test_ids=[
                FAIRnessTestIDs.F1_02MD_1_GUPRI.value,
                FAIRnessTestIDs.F2_01M_1_citation_metadata.value,
                FAIRnessTestIDs.F2_01M_2_description_metadata.value,
                FAIRnessTestIDs.A1_01M_1_access_rights_info_in_metadata.value,
                FAIRnessTestIDs.R1_01M_2_data_type_and_size_available.value,
                FAIRnessTestIDs.R1_2_01M_1_provenance_information_available.value,
                FAIRnessTestIDs.R1_3_01M_1_community_specific_metadata.value,
                FAIRnessTestIDs.R1_1_01M_1_license_information_available.value,
            ],
            not_executed_test_ids=[
                FAIRnessTestIDs.F3_01M_1_metadata_contains_data_identifier.value,
                FAIRnessTestIDs.F4_01M_1_metadata_retrievable_by_search_engines.value,
                FAIRnessTestIDs.R1_01M_3_measured_variable_information_available.value,
                FAIRnessTestIDs.R1_01M_5_data_size_matches_metadata.value,
                FAIRnessTestIDs.R1_01M_6_measured_variable_matches_metadata.value,
            ],
        )
        self.assert_test_not_executed(
            result.get_test_result(
                FAIRnessTestIDs.R1_01M_4_data_type_matches_metadata.value
            ),
            ignored_fields=["recommendation", "recommendation_details"],
        )
