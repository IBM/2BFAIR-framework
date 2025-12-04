# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tobefair_framework.core.collector.digital_object_collector import (
    DigitalObjectCollector,
)
from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.core.evaluator.evaluator import Evaluator, load_evaluators
from tobefair_framework.core.notification.notification_context import (
    NotificationRegistry,
)
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.fairness_evaluation_request import (
    FAIRnessEvaluationRequest,
)
from tobefair_framework.model.results.fairness_result import FAIRnessEvaluationResponse


class EvaluationController:

    def __init__(
        self,
        digital_object_collector: DigitalObjectCollector,
        metadata_collector: MetadataCollector,
        fairness_configuration: FAIRnessConfiguration,
    ):
        self.digital_object_collector = digital_object_collector
        self.metadata_collector = metadata_collector
        self.fairness_configuration = fairness_configuration

    def evaluate(
        self,
        evaluation_request: FAIRnessEvaluationRequest,
        evaluators_package: str,
    ) -> FAIRnessEvaluationResponse:
        digital_object_info = self.digital_object_collector.get_digital_object_info(
            raw_identifier=evaluation_request.resource_id,
            metadata_collector=self.metadata_collector,
        )
        community = evaluation_request.community
        task = evaluation_request.task
        load_evaluators(evaluators_package)
        return self.evaluate_digital_object(
            digital_object_info=digital_object_info,
            community=community,
            task=task,
        )

    def evaluate_digital_object(
        self,
        digital_object_info: DigitalObjectInfo,
        community: str | None = None,
        task: str | None = None,
    ) -> FAIRnessEvaluationResponse:
        detailed_result = Evaluator.evaluate(
            digital_object=digital_object_info,
            fairness_configuration=self.fairness_configuration,
        )
        evaluated_metadata_record = Evaluator.get_metadata_info(
            digital_object_info=digital_object_info
        )
        overall_results = Evaluator.get_overall_results(
            digital_object_info, detailed_result, community or "", task or ""
        )
        notifications = NotificationRegistry.get_notifications()
        response = FAIRnessEvaluationResponse(
            overall_result=overall_results,
            detailed_results=detailed_result,
            evaluated_metadata=evaluated_metadata_record,
            notifications=notifications,
        )
        return response
