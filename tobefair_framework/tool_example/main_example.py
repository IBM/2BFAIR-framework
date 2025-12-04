# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tobefair_framework.controller.evaluation_controller import EvaluationController
from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.framework_constants import (
    FAIRNESS_CONFIGURATION_FILE_PATH_FOR_THE_FRAMEWORK,
)
from tobefair_framework.model.fairness_evaluation_request import (
    FAIRnessEvaluationRequest,
)
from tobefair_framework.tool_example.digital_object_collector_from_file import (
    DigitalObjectCollectorFromFile,
)
from tobefair_framework.tool_example.metadata_collector_schema_org_json_ld_simple import (  # noqa E501
    MetadataCollectorSchemaorgJsonldSimple,
)

EVALUATORS_PACKAGE: str = "tobefair_framework.tool_example.principle_evaluators"
evaluation_request: FAIRnessEvaluationRequest = FAIRnessEvaluationRequest(
    resource_id="https://zenodo.org/records/8255910"
)

file_path: str = "tobefair_framework/tool_example/digital_object_example.json"

digital_object_collector = DigitalObjectCollectorFromFile(file_path=file_path)


fairness_configuration_dao = FAIRnessConfigurationFileDAO(
    file_path=FAIRNESS_CONFIGURATION_FILE_PATH_FOR_THE_FRAMEWORK
)
fairness_configuration = fairness_configuration_dao.read_configuration()

evaluation_controller = EvaluationController(
    digital_object_collector=digital_object_collector,
    metadata_collector=MetadataCollectorSchemaorgJsonldSimple(),
    fairness_configuration=fairness_configuration,
)

result = evaluation_controller.evaluate(
    evaluation_request=evaluation_request,
    evaluators_package=EVALUATORS_PACKAGE,
)
print(result)
