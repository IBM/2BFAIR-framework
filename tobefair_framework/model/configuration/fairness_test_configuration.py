# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, List

from pydantic import BaseModel, field_validator

from tobefair_framework.model.composite.identifiable_composite import (
    IdentifiableComposite,
)
from tobefair_framework.model.fairness_evaluation_maturity import (
    FAIRnessMaturities,
    FAIRnessMaturity,
)
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.recommendation import Recommendation
from tobefair_framework.model.results.test_execution_status import TestExecutionStatus
from tobefair_framework.model.results.test_result import TestResult


class FAIRnessTestConfiguration(
    BaseModel, IdentifiableComposite["FAIRnessTestConfiguration"]
):
    id: FAIRnessTestID
    name: str
    description_for_passed: str
    description_for_failure: str
    description_for_missing_information: str | None = None
    agnostic_requirements: dict | None = None
    community_requirements: dict | None = None
    max_score: float
    maturity: FAIRnessMaturity
    recommendation: Recommendation
    recommendation_details: str
    skip: bool = False
    losses: str

    @property
    def get_id(self) -> FAIRnessTestID:
        return self.id

    def get_children(self) -> None:
        return None

    @field_validator("recommendation_details", mode="before")
    @classmethod
    def array_to_str(cls, v: Any) -> str:
        if isinstance(v, list):
            agglutinated_recommendations = ""
            for recommendation in v:
                assert isinstance(recommendation, str)
                agglutinated_recommendations += recommendation + "\n"
            return agglutinated_recommendations
        return v

    def make_passed_test_result(self, **kwargs) -> TestResult:
        test_result = self.make_test_result()
        test_result.status = TestExecutionStatus.passed
        test_result.maturity = self.maturity
        test_result.result_description = self.description_for_passed
        test_result.score = self.max_score
        return test_result.apply_optional_test_result_arguments(**kwargs)

    def make_not_executed_test_result(self, **kwargs) -> TestResult:
        test_result = self.make_test_result()
        test_result.result_description = "test not executed"
        test_result.maturity = FAIRnessMaturities.Incomplete.value
        test_result.score = 0
        test_result.status = TestExecutionStatus.not_executed
        return test_result.apply_optional_test_result_arguments(**kwargs)

    def make_failed_test_result(self, **kwargs) -> TestResult:
        test_result = self.make_test_result()
        test_result.status = TestExecutionStatus.failed
        test_result.maturity = FAIRnessMaturities.Incomplete.value
        test_result.result_description = self.description_for_failure
        return test_result.apply_optional_test_result_arguments(**kwargs)

    def make_missing_requirements_test_result(
        self,
        missing_requirements: List[Any] | None = None,
        **kwargs,
    ) -> TestResult:
        test_result = self.make_test_result()
        test_result.status = TestExecutionStatus.not_executed
        test_result.maturity = FAIRnessMaturities.Incomplete.value
        result_description = (
            self.description_for_missing_information
            or FAIRnessTestConfiguration._make_missing_digital_object_information_description(  # noqa: E501
                missing_requirements=missing_requirements
            )
            if (missing_requirements := missing_requirements)
            else "Test failed due to missing requirements."
        )
        test_result.result_description = result_description
        return test_result.apply_optional_test_result_arguments(**kwargs)

    def make_test_result(self) -> TestResult:
        test_result = TestResult(
            test_id=self.id,
            test_name=self.name,
            max_score=self.max_score,
            status=TestExecutionStatus.not_executed,
            score=0,
            maturity=FAIRnessMaturities.Incomplete.value,
            result_description=None,
            recommendation=self.recommendation,
            recommendation_details=self.recommendation_details,
            losses=self.losses,
        )
        return test_result

    @classmethod
    def _make_missing_digital_object_information_description(
        cls,
        missing_requirements: List[Any | None],
    ) -> str:
        description = "missing following requirements: "
        for missing_requirement in missing_requirements:
            if not missing_requirement:
                description += missing_requirement.__class__.__name__ + ","
        description = description.rstrip(", ")
        return description

    def get_requirements_by_object_type(
        self,
        requirements_key: str,
        digital_object_type: str = "default",
    ) -> list | None:
        """
        Returns a list of requirements for a specific object type in a FAIRness test.

        Args:
            digital_object_type (String): used to get the requirements corresponding
            to the type of digital object.
            requirements_key (String): used to get the required data in the agnostic
            requirements.

        Returns:
            A list of requirements defined for the object_type.
            None if no requirements are defined for the object_type.
        """

        if (
            self.agnostic_requirements
            and isinstance(self.agnostic_requirements, dict)
            and "requirements" in self.agnostic_requirements.keys()
        ):
            requirements: List[dict] = self.agnostic_requirements.get(
                "requirements", []
            )
            for object in requirements:
                if digital_object_type.lower() in object.get("types", []):
                    return object.get(requirements_key, None)
        return None

    def get_requirements_recommendation(
        self,
        digital_object_type: str = "default",
    ) -> dict:
        """
        Returns a dictionary of recommendations for each missing requirements of
        a specific object type in a FAIRness test.

        Args:
            digital_object_type (String): used to get the requirements corresponding
            to the type of digital object.
            requirements_key (String): used to get the required data in the agnostic
            requirements.

        Returns:
            A dictionary of recommendations for missing requirements defined for
            the object_type.
        """

        if (
            self.agnostic_requirements
            and isinstance(self.agnostic_requirements, dict)
            and "requirements" in self.agnostic_requirements.keys()
        ):
            requirements: List[dict] = self.agnostic_requirements.get(
                "requirements", []
            )
            for object in requirements:
                if digital_object_type.lower() in object.get("types", []):
                    return object.get("recommendation_for_missing", {})
        return {}
