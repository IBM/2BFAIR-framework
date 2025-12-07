# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

from tobefair_backend.collector.digital_object_collector_from_url import (
    DigitalObjectCollectorFromURL,
)
from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
from tobefair_backend.constants import FAIRNESS_CONFIGURATION_FILE_PATH
from tobefair_framework.controller.evaluation_controller import EvaluationController
from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.model.digital_object_info import mock_digital_object_info
from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionIDs
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.metadata.metadata_record import MetadataRecord
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus


class TestFAIRnessEvaluationController(unittest.TestCase):
    def setUp(self):
        self.valid_digital_object_payload = {
            "@context": "http://schema.org/",
            "@id": "https://doi.org/10.1594/PANGAEA.908011",
            "@type": "Dataset",
            "identifier": "https://doi.org/10.1594/PANGAEA.908011",
            "url": "https://doi.pangaea.de/10.1594/PANGAEA.908011",
            "creator": {
                "@id": "https://orcid.org/0000-0003-3000-0020",
                "@type": "Person",
                "name": "Robert Huber",
                "familyName": "Huber",
                "givenName": "Robert",
                "identifier": "https://orcid.org/0000-0003-3000-0020",
                "email": "rhuber@uni-bremen.de",
            },
            "name": "Maximum diameter of Neogloboquadrina pachyderma sinistral from "
            + "surface sediment samples from the Norwegian-Greenland Sea",
            "publisher": {
                "@type": "Organization",
                "name": "PANGAEA",
                "disambiguatingDescription": "Data Publisher for Earth &"
                + " Environmental Science",
                "url": "https://www.pangaea.de/",
            },
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "description": "This data set contains unpublished measurements of the "
            + "maximum diameter of shells of the planktic foraminifer Neogloboquadrina "
            + "pachyderma sin. carried out on surface sediment samples from the "
            + "Norwegian-Greenland Sea.",
            "abstract": "This data set contains unpublished measurements of the "
            + "maximum diameter of shells of the planktic foraminifer "
            + "Neogloboquadrina pachyderma sin. carried out on surface sediment "
            + "samples from the Norwegian-Greenland Sea.",
        }
        self.invalid_digital_object_payload = {}
        self.valid_persistent_guid = "https://doi.org/10.5334/dsj-2020--41"
        fairness_configuration_dao = FAIRnessConfigurationFileDAO(
            file_path=FAIRNESS_CONFIGURATION_FILE_PATH
        )
        fairness_configuration = fairness_configuration_dao.read_configuration()
        self.evaluation_controller = EvaluationController(
            digital_object_collector=DigitalObjectCollectorFromURL(),
            metadata_collector=MetadataCollectorSchemaOrgJsonLD(),
            fairness_configuration=fairness_configuration,
        )

    def test_evaluate_findability_invalid_digital_object_payload(self):
        mock_digital_object = mock_digital_object_info()
        mock_digital_object.metadata_record = MetadataRecord(
            is_machine_retrieved=False,
            raw_value=self.invalid_digital_object_payload,
        )
        results = self.evaluation_controller.evaluate_digital_object(
            mock_digital_object
        )
        f_results = results.detailed_results.dimension_results[FAIRDimensionIDs.F.value]
        f2_01m_results = f_results.get_principle_result(
            FAIRPrincipleIDs.F2.value
        ).get_result(FAIRnessMetricIDs.F2_01M_rich_metadata.value)
        self.assertEqual(
            f2_01m_results.get_result(
                FAIRnessTestIDs.F2_01M_1_citation_metadata.value
            ).status,
            TestExecutionStatus.not_executed,
        )
        self.assertEqual(
            f2_01m_results.get_result(
                FAIRnessTestIDs.F2_01M_2_description_metadata.value
            ).status,
            TestExecutionStatus.not_executed,
        )

    def test_evaluate_findability_invalid_identifier(self):
        mock_digital_object = mock_digital_object_info()
        mock_digital_object.identifier_info.identifier = "0000"
        results = self.evaluation_controller.evaluate_digital_object(
            mock_digital_object
        )
        f2_01m_results = (
            results.detailed_results.dimension_results[FAIRDimensionIDs.F.value]
            .get_principle_result(FAIRPrincipleIDs.F2.value)
            .get_result(FAIRnessMetricIDs.F2_01M_rich_metadata.value)
        )
        self.assertEqual(
            f2_01m_results.get_result(
                FAIRnessTestIDs.F2_01M_1_citation_metadata.value
            ).status,
            TestExecutionStatus.not_executed,
        )
        self.assertEqual(
            f2_01m_results.get_result(
                FAIRnessTestIDs.F2_01M_2_description_metadata.value
            ).status,
            TestExecutionStatus.not_executed,
        )
