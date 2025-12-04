# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, ItemsView, List

from pydantic import BaseModel, computed_field, field_serializer

from tobefair_framework.model.alternate_test_behavior import AlternateTestBehavior
from tobefair_framework.model.composite.identifiable_composite_result import (
    IdentifiableCompositeResult,
)
from tobefair_framework.model.configuration.fairness_metric_configuration import (
    FAIRnessMetricConfiguration,
    MetricPriority,
    ScoringMechanism,
)
from tobefair_framework.model.fairness_evaluation_maturity import (
    FAIRnessMaturities,
    FAIRnessMaturity,
)
from tobefair_framework.model.identifier.fairness_metric_id import (
    FAIRnessMetricID,
    FAIRnessMetricIDs,
)
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus
from tobefair_framework.model.results.test_result import TestResult


class MetricResult(BaseModel, IdentifiableCompositeResult[TestResult]):

    alternate_test_behavior: AlternateTestBehavior = AlternateTestBehavior.skip
    metric_id: FAIRnessMetricID
    metric_name: str | None = None
    metric_priority: MetricPriority | None = None
    metric_maturity: FAIRnessMaturity = FAIRnessMaturities.Incomplete.value
    scoring_mechanism: ScoringMechanism = ScoringMechanism.cumulative
    results: Dict[FAIRnessTestID, TestResult] = {}

    def get_results(self) -> Dict[FAIRnessTestID, TestResult]:
        return self.results

    def set_results(self, value: Dict[FAIRnessTestID, TestResult]):
        self.results = value

    @classmethod
    def mock(cls) -> "MetricResult":
        return cls(metric_id=FAIRnessMetricIDs.F1_01MD_GUID_identifier.value)

    @property
    def get_id(self) -> FAIRnessMetricID:
        return self.metric_id

    @computed_field  # type: ignore
    @property
    def metric_score(self) -> float:
        if self.scoring_mechanism == ScoringMechanism.alternative:
            return max(self.results.values()).score
        accumulated_score: float = 0.0
        [
            accumulated_score := accumulated_score + result.score
            for result in self.results.values()
        ]
        return accumulated_score if accumulated_score <= 1 else 1.0

    def alternate_test_results(self):
        best_result = max(self.results.values())
        for test_id, test_result in self.results.items():
            if (
                test_result != best_result
                and self.alternate_test_behavior == AlternateTestBehavior.skip
            ):
                self.results[test_id].alternate_out(best_result.test_id)

    def merge_results(self, test_id: FAIRnessTestID, incoming_test_result: TestResult):
        self.results[test_id] = incoming_test_result

    def update_results(self, test_id: FAIRnessTestID, test_result: TestResult):
        self.results.update({test_id: test_result})

    def get_result(self, test_id: FAIRnessTestID) -> TestResult:
        return self.results[test_id]

    def items(self) -> ItemsView[FAIRnessTestID, TestResult]:
        return self.results.items()

    def get_total_score(self) -> float:
        total_score = 0.0
        for test_id, result in self.items():
            total_score += result.score
        return total_score

    def get_max_total_score(self) -> float:
        max_total_score = 0.0
        if self.scoring_mechanism == ScoringMechanism.cumulative:
            for test_id, result in self.items():
                max_total_score += result.max_score
            return max_total_score
        return max([test_result.max_score for test_result in self.results.values()])

    def check_if_all_tests_passed(self) -> bool:
        for test_result in self.results.values():
            if test_result.status == TestExecutionStatus.failed:
                return False
        return True

    @classmethod
    def _from_configuration_and_results(
        cls, configuration, results: List[TestResult]
    ) -> "MetricResult":
        assert isinstance(configuration, FAIRnessMetricConfiguration)
        return cls(
            metric_id=configuration.id,
            metric_name=configuration.name,
            metric_priority=configuration.priority,
            metric_maturity=max(result.maturity for result in results),
            scoring_mechanism=configuration.scoring_mechanism,
            results={result.test_id: result for result in results},
        )

    @field_serializer("metric_maturity")
    def serialize_metric_maturity(self, metric_maturity: FAIRnessMaturity) -> str:
        return metric_maturity.value

    @field_serializer("scoring_mechanism")
    def serialize_scoring_mechanism(self, scoring_mehanism: ScoringMechanism) -> str:
        def capitalize_first_letter(string: str) -> str:
            capitalized_string = str.capitalize(string[0]) + string[1:]
            return capitalized_string

        return capitalize_first_letter(scoring_mehanism.value)
