# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

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


class TestResultOrder(unittest.TestCase):

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

    def test_correct_order(self):
        result = self.evaluation_controller.evaluate(
            evaluation_request=FAIRnessEvaluationRequest(resource_id="0000"),
            evaluators_package=EVALUATORS_PACKAGE,
        )
        keys = list(result.detailed_results.dimension_results.keys())
        self.assertEqual(keys[0].raw_value, "F")
        self.assertEqual(keys[1].raw_value, "A")
        self.assertEqual(keys[2].raw_value, "I")
        self.assertEqual(keys[3].raw_value, "R")
