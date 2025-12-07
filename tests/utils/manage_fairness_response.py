# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json

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
from tobefair_framework.model.results.fairness_result import FAIRnessEvaluationResponse


def save_fairness_evaluation_response_to_file(resource_id: str, file_path: str):
    evaluation_request = FAIRnessEvaluationRequest(resource_id=resource_id)
    fairness_configuration_dao = FAIRnessConfigurationFileDAO(
        file_path=FAIRNESS_CONFIGURATION_FILE_PATH
    )
    fairness_configuration = fairness_configuration_dao.read_configuration()
    evaluation_controller = EvaluationController(
        digital_object_collector=DigitalObjectCollectorFromURL(),
        metadata_collector=MetadataCollectorSchemaOrgJsonLD(),
        fairness_configuration=fairness_configuration,
    )
    evaluation_result: FAIRnessEvaluationResponse = evaluation_controller.evaluate(
        evaluation_request=evaluation_request, evaluators_package=EVALUATORS_PACKAGE
    )
    with open(file_path, "w") as file:
        response_as_dict = evaluation_result.model_dump(mode="json")
        json.dump(response_as_dict, file, indent=4)
