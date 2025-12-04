# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import abc
from abc import abstractmethod
from typing import Any, Callable, ClassVar, Dict, ItemsView, List, TypeAlias, cast

from pydantic import BaseModel, PrivateAttr, model_validator

from tobefair_framework.model.configuration.fair_principle_configuration import (
    FAIRPrincipleConfiguration,
)
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)
from tobefair_framework.model.configuration.fairness_test_configuration import (
    FAIRnessTestConfiguration,
)
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID
from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricID
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.results.dimension_results import DimensionResult
from tobefair_framework.model.results.metric_result import MetricResult
from tobefair_framework.model.results.principle_result import PrincipleResult
from tobefair_framework.model.results.test_result import TestResult


class EvaluationContext(BaseModel):

    # For each metric which test should be executed
    context: Dict[FAIRnessMetricID, List[FAIRnessTestID]] = {}

    def get_metrics_and_tests(
        self,
    ) -> ItemsView[FAIRnessMetricID, List[FAIRnessTestID]]:
        return self.context.items()

    def should_test_metric(self, metric_id: FAIRnessMetricID) -> bool:
        return metric_id in self.context.keys()

    def should_execute_test(self, test_id: FAIRnessTestID) -> bool:
        return self.should_execute_test_for_metric(
            test_id=test_id, metric_id=test_id.get_parent_id()
        )

    def should_execute_test_for_metric(
        self, test_id: FAIRnessTestID, metric_id: FAIRnessMetricID
    ) -> bool:
        return (
            self.should_test_metric(metric_id=metric_id)
            and test_id in self.context[metric_id]
        )


MetricEvaluatingMethod: TypeAlias = Callable
MetricEvaluatingMethodMap: TypeAlias = Dict[FAIRnessMetricID, MetricEvaluatingMethod]


class PrincipleEvaluator(BaseModel, abc.ABC):

    _fair_principle_to_evaluate: ClassVar[FAIRPrincipleID] = PrivateAttr()

    _tests_configuration: Dict[FAIRnessTestID, FAIRnessTestConfiguration] = PrivateAttr(
        {}
    )
    fairness_configuration: FAIRnessConfiguration

    @model_validator(mode="after")
    def set_tests_to_be_executed(self):
        """
        @model_validator(mode='after'): This decorator indicates that
            set_tests_to_be_executed is a model validator that runs
            after all individual field validations have completed, e.g.,
            it runs after fairness_configuration attribute is set.
        Return self: Model validators in Pydantic V2 (when using mode='after')
            are expected to return the modified instance of the model
        """
        flat_configuration = self.fairness_configuration.flat_configuration
        if self.__class__._fair_principle_to_evaluate not in flat_configuration:
            raise Exception(
                f"Error on instantiating {self.__class__.__name__} because "
                f"{self.__class__._fair_principle_to_evaluate.principle_id} "
                "is not in the configuration."
            )
        fair_principle_to_evaluate = cast(
            FAIRPrincipleConfiguration,
            flat_configuration[self.__class__._fair_principle_to_evaluate],
        )
        tests_to_evaluate: List[FAIRnessTestConfiguration] = []
        [
            (tests_to_evaluate := tests_to_evaluate + list(a.tests.values()))
            for a in fair_principle_to_evaluate.metrics.values()
        ]
        self._tests_configuration = {
            test_to_evaluate.id: test_to_evaluate
            for test_to_evaluate in tests_to_evaluate
            if not test_to_evaluate.skip
        }
        return self

    @abstractmethod
    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        pass

    def get_dimension_results(
        self, evaluation_subject: Any, fairness_configuration: FAIRnessConfiguration
    ) -> DimensionResult:
        configuration = fairness_configuration.flat_configuration
        return DimensionResult.from_results(
            PrincipleResult.from_results(
                MetricResult.from_results(
                    self.evaluate(evaluation_subject), configuration
                ),
                configuration,
            ),
            configuration,
        )[0]
