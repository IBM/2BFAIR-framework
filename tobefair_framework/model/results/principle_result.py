# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, ItemsView, List

from pydantic import BaseModel, computed_field

from tobefair_framework.model.composite.identifiable_composite_result import (
    IdentifiableCompositeResult,
)
from tobefair_framework.model.configuration.fair_principle_configuration import (
    FAIRPrincipleConfiguration,
)
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID
from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricID
from tobefair_framework.model.results.metric_result import MetricResult


class PrincipleResult(BaseModel, IdentifiableCompositeResult[MetricResult]):

    principle_id: FAIRPrincipleID
    principle_name: str | None = None
    results: Dict[FAIRnessMetricID, MetricResult] = {}

    def get_results(self) -> Dict[FAIRnessMetricID, MetricResult]:
        return self.results

    def set_results(self, value: Dict[FAIRnessMetricID, MetricResult]):
        self.results = value

    @property
    def get_id(self) -> FAIRPrincipleID:
        return self.principle_id

    @computed_field  # type: ignore
    @property
    def score(self) -> float:
        return self.get_total_score()

    def merge_results(
        self, metric_id: FAIRnessMetricID, incoming_test_results: MetricResult
    ):
        if not self.results.get(metric_id):
            self.results[metric_id] = incoming_test_results
        else:
            for (
                incoming_test_id,
                incoming_single_test_result,
            ) in incoming_test_results.items():
                self.results[metric_id].merge_results(
                    incoming_test_id, incoming_single_test_result
                )
        return

    def update_results(self, metric_id: FAIRnessMetricID, test_results: MetricResult):
        self.results.update({metric_id: test_results})

    def get_result(self, metric_id: FAIRnessMetricID) -> MetricResult:
        return self.results[metric_id]

    def items(self) -> ItemsView[FAIRnessMetricID, MetricResult]:
        return self.results.items()

    def get_total_score(self) -> float:
        total_score = 0.0
        qtd_metric = 0
        for test_id, result in self.items():
            total_score = total_score + result.get_total_score()
            qtd_metric += 1
        return round(total_score / qtd_metric, 2)

    def get_max_total_score(self) -> float:
        max_total_score = 0.0
        qtd_metric = 0
        for test_id, result in self.items():
            max_total_score += result.get_max_total_score()
            qtd_metric += 1
        return max_total_score / qtd_metric

    def check_if_all_tests_passed(self) -> bool:
        for metric_id, test_results in self.results.items():
            if not test_results.check_if_all_tests_passed():
                return False
        return True

    @classmethod
    def _from_configuration_and_results(
        cls, configuration, results: List[MetricResult]
    ) -> "PrincipleResult":
        assert isinstance(configuration, FAIRPrincipleConfiguration)
        return PrincipleResult(
            principle_id=configuration.id,
            principle_name=configuration.name,
            results={result.metric_id: result for result in results},
        )
