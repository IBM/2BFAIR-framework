# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json
import unittest

import jsondiff  # type: ignore

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
from tobefair_framework.core.notification.notification_context import Notification
from tobefair_framework.model.fairness_evaluation_request import (
    FAIRnessEvaluationRequest,
)
from tobefair_framework.model.results.fairness_result import FAIRnessEvaluationResponse


class TestEvaluationResponse(unittest.TestCase):

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

    @unittest.skip(
        "Skipping this test because it is not idempotent,"
        " i.e., it produces different results when running in different computers. "
    )
    def test_response_values_are_correct(
        self,
    ):
        evaluation_request = FAIRnessEvaluationRequest(
            resource_id="https://doi.org/10.1594/PANGAEA.893286"
        )
        result: FAIRnessEvaluationResponse = self.evaluation_controller.evaluate(
            evaluation_request=evaluation_request, evaluators_package=EVALUATORS_PACKAGE
        )

        formatted_result = result.model_dump(mode="json")

        path = "data_files/mock_pangea_response.json"
        with open(path, "r") as file:
            mock = file.read()
            mock_data = json.loads(mock)

        msg = ""
        if difference := jsondiff.diff(formatted_result, mock_data):
            print("difference")
            msg = f"The difference is: {difference}"

        self.assertDictEqual(formatted_result, mock_data, msg)

    def test_notification(self):
        evaluation_request = FAIRnessEvaluationRequest(
            # TODO: change the resource_id
            # when we solve the problem to get metadata from this one.
            resource_id="0000"
        )
        result: FAIRnessEvaluationResponse = self.evaluation_controller.evaluate(
            evaluation_request=evaluation_request, evaluators_package=EVALUATORS_PACKAGE
        )
        notification = Notification(
            type="error",
            title="Error",
            description="Digital object's URI could not be resolved to an URL.",
        )
        self.assertTrue(notification in result.notifications)
