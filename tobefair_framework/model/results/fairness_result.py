# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Annotated, Dict, List, cast

from pydantic import BaseModel, model_serializer, model_validator
from typing_extensions import Self

from tobefair_framework.core.notification.notification_context import Notification
from tobefair_framework.model.composite.identifiable_composite_result import (
    CompositeResult,
)
from tobefair_framework.model.configuration.fair_dimension_configuration import (
    FAIRDimensionConfiguration,
)
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)
from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionID
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.results.dimension_results import DimensionResult
from tobefair_framework.model.results.metric_result import MetricResult
from tobefair_framework.model.results.principle_result import PrincipleResult
from tobefair_framework.model.results.test_result import TestResult
from tobefair_framework.model.results.test_specific_recommendation import (
    TestSpecificRecommendation,
)


class FAIRnessEvaluationRequest(BaseModel):
    resource_id: str = "https://doi.org/10.1594/PANGAEA.893286"
    community: str | None = None
    task: str | None = None


class FAIRnessEvaluationResponse(BaseModel):

    overall_result: "OverallResult"
    detailed_results: "FAIRResults"
    evaluated_metadata: dict | None = None
    notifications: list["Notification"] = []

    def get_test_results(self) -> List[TestResult]:
        test_results = cast(List[TestResult], self.detailed_results.get_last_children())
        return test_results

    def get_optional_test_result(self, test_id: FAIRnessTestID) -> TestResult | None:
        test_result_dict = {
            test_result.test_id: test_result for test_result in self.get_test_results()
        }
        return test_result_dict.get(test_id)

    def get_test_result(self, test_id: FAIRnessTestID) -> TestResult:
        test_result = self.get_optional_test_result(test_id)
        if test_result is None:
            raise Exception(f"Test with id {test_id.value} not available")
        return test_result


Number = Annotated[int, float]


def simple_average(terms: list[Number]) -> float:
    if (divisor := len(terms)) != 0:
        sum = 0
        terms_list = list(terms)
        while terms_list:
            sum += terms_list.pop()
        return sum / divisor
    return 0


class PrincipleResultScores(BaseModel):
    principle_scores: Dict[str, int] = {}
    total_score: float = 0

    @model_validator(mode="after")
    def average_of_scores(self) -> Self:
        total_average_score = simple_average(list(self.principle_scores.values()))
        self.total_score = total_average_score
        return self

    @model_serializer
    def serializer(self):
        representation = {}
        for dimension_name, result_score in self.principle_scores.items():
            representation[dimension_name] = result_score
        representation["total_score"] = self.total_score
        return representation


class OverallResult(BaseModel):
    evaluation_id: str
    evaluated_digital_object_id: str
    evaluated_metadata_record_id: str
    evaluated_digital_object_landing_page_url: str | None = None
    task: str | None = None
    community: str | None = None
    evaluation_score: PrincipleResultScores
    priority_recommendations: list[TestSpecificRecommendation] = []


class FAIRResults(BaseModel, CompositeResult[DimensionResult]):

    dimension_results: Dict[FAIRDimensionID, DimensionResult]

    def get_results(self) -> Dict[FAIRDimensionID, DimensionResult]:
        return self.dimension_results

    def set_results(self, value: Dict[FAIRDimensionID, DimensionResult]):
        self.dimension_results = value

    @classmethod
    def from_test_results(
        cls,
        test_results: List[TestResult],
        fairness_configuration: FAIRnessConfiguration,
    ) -> "FAIRResults":
        configuration = fairness_configuration.flat_configuration
        dimension_results = DimensionResult.from_results(
            PrincipleResult.from_results(
                results=MetricResult.from_results(
                    results=test_results, general_configuration=configuration
                ),
                general_configuration=configuration,
            ),
            configuration,
        )
        return cls._from_configuration_and_results(configuration, dimension_results)

    @classmethod
    def _from_configuration_and_results(
        cls, configuration, results: List[DimensionResult]
    ) -> Self:
        return cls(
            dimension_results={result.dimension_id: result for result in results}
        )

    def order(
        self,
        dimension_results_order: List[FAIRDimensionID],
    ):
        results: Dict[FAIRDimensionID, DimensionResult] = {}
        for dimension_id in dimension_results_order:
            if principle_results := self.dimension_results.get(dimension_id):
                results[dimension_id] = principle_results
        self.dimension_results = results

    def get_overall_score(
        self, predefined_order: list[FAIRDimensionID] | None = None
    ) -> PrincipleResultScores:
        dimension_ids: List[FAIRDimensionID]
        if predefined_order:
            dimension_ids = predefined_order
        else:
            dimension_ids = list(self.dimension_results.keys())
        principle_result_scores = PrincipleResultScores()
        for dimension_id in dimension_ids:
            if principle_result := self.dimension_results.get(dimension_id):
                score = principle_result.get_percentual_score()
            else:
                score = 0
            principle_result_scores.principle_scores[
                FAIRDimensionConfiguration.get_dimension_name_from_id(dimension_id)
            ] = score
        return principle_result_scores

    def get_children(self) -> list[DimensionResult]:
        return list(self.dimension_results.values())

    @property
    def test_result_dict(self):
        all_test_results = []
        [
            all_test_results := all_test_results + dimension_result.get_last_children()
            for dimension_result in self.dimension_results.values()
        ]
        all_test_results = cast(list[TestResult], all_test_results)
        all_test_results_dict = {
            test_result.test_id: test_result for test_result in all_test_results
        }

        return all_test_results_dict
