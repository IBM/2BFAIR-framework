# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

import jsondiff  # type: ignore

from tests.data_for_testing.sample_evaluated_metadata_response import evaluated_metadata
from tobefair_backend.collector.digital_object_collector_from_url import (
    DigitalObjectCollectorFromURL,
)
from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
from tobefair_backend.constants import (
    EVALUATORS_PACKAGE,
    FAIRNESS_CONFIGURATION_FILE_PATH,
)
from tobefair_framework.controller.evaluation_controller import EvaluationController
from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.model.fairness_evaluation_request import (
    FAIRnessEvaluationRequest,
)


class TestMetadataInResponse(TestCase):

    def setUp(self) -> None:
        fairness_configuration_dao = FAIRnessConfigurationFileDAO(
            file_path=FAIRNESS_CONFIGURATION_FILE_PATH
        )
        fairness_configuration = fairness_configuration_dao.read_configuration()
        self.evaluation_controller = EvaluationController(
            digital_object_collector=DigitalObjectCollectorFromURL(),
            metadata_collector=MetadataCollectorSchemaOrgJsonLD(),
            fairness_configuration=fairness_configuration,
        )

    def test_metadata_in_response(
        self,
    ):
        evaluation_request = FAIRnessEvaluationRequest(
            resource_id="https://doi.org/10.1594/PANGAEA.893286"
        )
        result = self.evaluation_controller.evaluate(
            evaluation_request=evaluation_request, evaluators_package=EVALUATORS_PACKAGE
        )

        msg = ""
        formatted_result = result.model_dump(mode="json")
        if difference := jsondiff.diff(
            formatted_result["evaluated_metadata"], evaluated_metadata
        ):
            print("difference")
            msg = f"The difference is: {difference}"

        self.assertDictEqual(
            formatted_result["evaluated_metadata"], evaluated_metadata, msg
        )
