# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List, cast

from pydantic import BaseModel, ValidationError

from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionID
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.recommendation import Recommendation


class TestSpecificRecommendation(BaseModel):
    recommendation: Recommendation
    test_id: FAIRnessTestID
    dimension_id: FAIRDimensionID

    def __init__(self, **data):
        try:
            test_id = cast(FAIRnessTestID, data["test_id"])
            data["dimension_id"] = (
                test_id.get_parent_id().get_parent_id().get_parent_id()
            )
            super().__init__(**data)
        except Exception:
            raise ValidationError

    @classmethod
    def get_priority_test_specific_recommendations(
        cls,
        test_specific_recommendations: List["TestSpecificRecommendation"],
        number_of_recommendations: int,
    ) -> List["TestSpecificRecommendation"]:
        test_specific_recommendations.sort()
        return test_specific_recommendations[:number_of_recommendations]

    def __lt__(self, other: "TestSpecificRecommendation") -> bool:
        return self.recommendation.priority < other.recommendation.priority
