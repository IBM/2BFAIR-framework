# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict

from pydantic import BaseModel

from tobefair_framework.model.composite.leaf_result import LeafResult
from tobefair_framework.model.fairness_evaluation_maturity import (
    FAIRnessMaturities,
    FAIRnessMaturity,
)
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.identifier.id import ID
from tobefair_framework.model.recommendation import Recommendation
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus
from tobefair_framework.model.results.test_specific_recommendation import (
    TestSpecificRecommendation,
)


class TestResult(BaseModel, LeafResult):
    test_id: FAIRnessTestID
    test_name: str
    score: float = 0
    max_score: float
    maturity: FAIRnessMaturity
    result_description: str | None = None
    result_details: str | None = (
        None  # TODO: implement here description for missing metadata
    )
    evaluated_requirements: dict | None = None
    status: TestExecutionStatus = TestExecutionStatus.failed
    recommendation: Recommendation | None = None
    recommendation_details: str | None = None
    losses: str | None = None

    @property
    def get_id(self) -> FAIRnessTestID:
        return self.test_id

    # type: ignore
    @property
    def test_specific_recommendation(
        self, exclude=True
    ) -> TestSpecificRecommendation | None:
        return (
            TestSpecificRecommendation(
                recommendation=recommendation, test_id=self.test_id
            )
            if (recommendation := self.recommendation)
            else None
        )

    def get_results(self) -> Dict[ID, LeafResult]:
        return {self.test_id: self}

    def get_total_score(self) -> float:
        return self.score

    def get_max_total_score(self) -> float:
        return self.max_score

    def get_recommendations(self) -> list[Recommendation]:
        if recommendation := self.recommendation:
            return [recommendation]
        return []

    def get_necessary_test_specific_recommendations(
        self,
    ) -> list[TestSpecificRecommendation]:
        return (
            [self.test_specific_recommendation]
            if self.status != TestExecutionStatus.passed
            and (self.test_specific_recommendation is not None)
            else []
        )

    def alternate_out(self, executed_test_id: FAIRnessTestID):
        self.score = 0
        self.status = TestExecutionStatus.not_executed
        self.maturity = FAIRnessMaturities.Incomplete.value
        self.result_description = (
            "Not executed due to alternative evaluation context."
            f"{executed_test_id.value} executed and passed instead."
        )

    def __lt__(self, other) -> bool:
        if isinstance(other, TestResult):
            return self.score < other.score
        return False

    def __eq__(self, value: object) -> bool:
        if isinstance(value, TestResult):
            return value.test_id == self.test_id
        return False

    def apply_optional_test_result_arguments(self, **kwargs) -> "TestResult":
        for field in kwargs:
            if field in dir(self):
                setattr(self, field, kwargs[field])
            else:
                raise Exception(
                    f"'{field}' is not an attribute of TestResult. "
                    f"Error for test {self.test_id.value}."
                )
        return self
