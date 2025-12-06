import json
from typing import List
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Tag

from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_backend.repository.uri_protocol_repository import URIProtocolRepository
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.landing_page import LandingPage
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.A1.value)
class StandardizedProtocolEvaluator(PrincipleEvaluator):

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        return [
            self._test_information_about_access_rights_in_metadata(evaluation_subject),
            self._evaluate_identifier_resolves_to_landing_page_a1_02m_1(
                evaluation_subject.landing_page
            ),
            self._test_standardized_protocol_metadata_used_in_uri(
                digital_object=evaluation_subject
            ),
            self._test_standardized_protocol_used_in_data_link(
                digital_object=evaluation_subject
            ),
        ]

    @fairness_test(FAIRnessTestIDs.A1_01M_1_access_rights_info_in_metadata.value)
    def _test_information_about_access_rights_in_metadata(
        self, digital_object: DigitalObjectInfo
    ) -> TestResult:
        test_id = FAIRnessTestIDs.A1_01M_1_access_rights_info_in_metadata.value
        test_configuration = self._tests_configuration[test_id]
        if (metadata_record := digital_object.metadata_record) is None:
            return test_configuration.make_missing_requirements_test_result()
        if requirements := test_configuration.get_requirements_by_object_type(
            requirements_key="fields_to_search"
        ):
            for requirement in requirements:
                if (
                    access_level := metadata_record.raw_value.get(requirement, None)
                ) is not None:
                    result_details = (
                        f"Found minimum required property '{requirement}' with "
                        f"value '{access_level}'."
                    )
                    return test_configuration.make_passed_test_result(
                        result_details=result_details
                    )
                else:
                    if digital_object.landing_page:
                        parsed_data = BeautifulSoup(
                            digital_object.landing_page.decoded_html_body, "html.parser"
                        )

                        div = parsed_data.find("div", {"id": "recordVersions"})
                        if isinstance(div, Tag):
                            data_record = div.get("data-record")
                            if isinstance(data_record, str):
                                record_json = json.loads(data_record)

                                if access := record_json["access"]["status"]:
                                    result_details = (
                                        f"Found minimum required property access.status"
                                        f" with value '{access}'."
                                    )
                                    return test_configuration.make_passed_test_result(
                                        result_details=result_details
                                    )

        else:
            result_description = (
                "Test not executed: No minimum required properties for conditions "
                "of access were found for your object type."
            )

            result_details = (
                "Include the minimum requirements to your object type "
                "in the fairness configuration file."
            )

            return test_configuration.make_not_executed_test_result(
                result_description=result_description, result_details=result_details
            )

        return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.A1_02M_1_identifier_resolves_to_landing_page.value)
    def _evaluate_identifier_resolves_to_landing_page_a1_02m_1(
        self, landing_page: LandingPage | None
    ):
        test_id = FAIRnessTestIDs.A1_02M_1_identifier_resolves_to_landing_page.value
        test_configuration = self._tests_configuration[test_id]
        if landing_page:
            test_result = test_configuration.make_passed_test_result()
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result

    @fairness_test(FAIRnessTestIDs.A1_03M_1_standard_protocol_for_metadata.value)
    def _test_standardized_protocol_metadata_used_in_uri(
        self, digital_object: DigitalObjectInfo
    ) -> TestResult:
        test_id = FAIRnessTestIDs.A1_03M_1_standard_protocol_for_metadata.value
        test_configuration = self._tests_configuration[test_id]
        if digital_object.landing_page is None:
            return test_configuration.make_missing_requirements_test_result(
                [digital_object.landing_page]
            )
        landing_page_url = digital_object.landing_page.url
        scheme = urlparse(landing_page_url).scheme
        if scheme in URIProtocolRepository.all():
            return test_configuration.make_passed_test_result()
        return test_configuration.make_failed_test_result()

    @fairness_test(FAIRnessTestIDs.A1_03MD_2_standard_protocol_in_data_link.value)
    def _test_standardized_protocol_used_in_data_link(
        self, digital_object: DigitalObjectInfo
    ) -> TestResult:
        test_id = FAIRnessTestIDs.A1_03MD_2_standard_protocol_in_data_link.value
        test_configuration = self._tests_configuration[test_id]
        if not (metadata_record := digital_object.metadata_record):
            return test_configuration.make_missing_requirements_test_result()
        elif not (
            links := MetadataCollectorSchemaOrgJsonLD.get_content_links(
                metadata_record.raw_value
            )
        ):
            return test_configuration.make_missing_requirements_test_result(
                result_details=(
                    "No content link is available to check the use of "
                    "standardized protocol in data link."
                )
            )
        if any(
            [
                urlparse(link.href).scheme in URIProtocolRepository.all()
                for link in links
            ]
        ):
            return test_configuration.make_passed_test_result()
        return test_configuration.make_failed_test_result()
