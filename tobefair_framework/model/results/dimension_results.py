# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, ItemsView, List, cast

from pydantic import BaseModel, computed_field

from tobefair_framework.model.composite.identifiable_composite_result import (
    IdentifiableCompositeResult,
)
from tobefair_framework.model.configuration.fair_dimension_configuration import (
    FAIRDimensionConfiguration,
)
from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionID
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.results.principle_result import PrincipleResult
from tobefair_framework.model.results.test_result import TestResult


class DimensionResult(BaseModel, IdentifiableCompositeResult[PrincipleResult]):
    dimension_id: FAIRDimensionID
    dimension_name: str | None = None
    results: Dict[FAIRPrincipleID, PrincipleResult] = {}

    def get_results(self) -> Dict[FAIRPrincipleID, PrincipleResult]:
        return self.results

    def set_results(self, value: Dict[FAIRPrincipleID, PrincipleResult]):
        self.results = value

    @property
    def get_id(self) -> FAIRDimensionID:
        return self.dimension_id

    @property
    @computed_field
    def score(self) -> float:
        return self.get_total_score()

    @classmethod
    def grouped_by_dimension(
        cls, results: list["DimensionResult"]
    ) -> Dict[FAIRDimensionID, "DimensionResult"]:
        if not (results_grouped := cls.merge_all(results)):
            return {}
        results_sorted_by_dimension: Dict[FAIRDimensionID, "DimensionResult"] = {}
        for (
            principle_result_id,
            metric_results,
        ) in results_grouped.results.items():
            parent_dimension_id = principle_result_id.get_parent_id()
            if dimension_results := results_sorted_by_dimension.get(
                parent_dimension_id
            ):
                dimension_results.merge_results(principle_result_id, metric_results)
            else:
                results_sorted_by_dimension[parent_dimension_id] = DimensionResult(
                    results={principle_result_id: metric_results},
                    dimension_id=parent_dimension_id,
                    dimension_name=(
                        FAIRDimensionConfiguration.get_dimension_name_from_id(
                            parent_dimension_id
                        )
                    ),
                )

        return results_sorted_by_dimension

    @classmethod
    def merge_all(
        cls, principle_results: list["DimensionResult"]
    ) -> "DimensionResult | None":
        if len(principle_results) == 0:
            return None
        base = principle_results.pop()
        for result in principle_results:
            base.merge(result)
        return base

    def merge(self, other_principle_results: "DimensionResult"):
        self.results = self.results | other_principle_results.results

    def merge_results(
        self, principle_id: FAIRPrincipleID, incoming_metric_results: PrincipleResult
    ):
        if not self.results.get(principle_id):
            self.results[principle_id] = incoming_metric_results
        else:
            for (
                incoming_metric_id,
                incoming_test_results,
            ) in incoming_metric_results.items():
                self.results[principle_id].merge_results(
                    incoming_metric_id, incoming_test_results
                )
        return

    def get_test_result_with_id(self, test_id: FAIRnessTestID) -> TestResult | None:
        try:
            test_results = cast(List[TestResult], self.get_last_children())
        except Exception:
            return None
        test_with_seeked_id: TestResult | None = None
        [
            test_with_seeked_id := test_result
            for test_result in test_results
            if test_result.test_id == test_id
        ]
        return test_with_seeked_id

    def update_principle_results(
        self, principle_id: FAIRPrincipleID, metric_results: PrincipleResult
    ):
        self.results.update({principle_id: metric_results})

    def get_principle_result(self, principle_id: FAIRPrincipleID) -> PrincipleResult:
        return self.results[principle_id]

    def items(self) -> ItemsView[FAIRPrincipleID, PrincipleResult]:
        return self.results.items()

    def check_if_all_tests_passed(self) -> bool:
        for principle_id, metric_results in self.results.items():
            if not metric_results.check_if_all_tests_passed():
                return False
        return True

    def get_percentual_score(self) -> int:
        return int(100 * self.get_total_score() / self.get_max_total_score())

    @classmethod
    def _from_configuration_and_results(
        cls, configuration, results: List[PrincipleResult]
    ) -> "DimensionResult":
        assert isinstance(configuration, FAIRDimensionConfiguration)
        return DimensionResult(
            dimension_id=configuration.id,
            dimension_name=configuration.name,
            results={result.principle_id: result for result in results},
        )
