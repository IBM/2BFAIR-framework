# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel, model_serializer

from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID


class Recommendation(BaseModel):
    priority: int = 0
    value: str

    @model_serializer
    def ser_model(self) -> str:
        return self.value

    def add_test_id_prefix(self, test_id: FAIRnessTestID) -> "Recommendation":
        copy = self.model_copy()
        copy.value = f"{test_id.value}: {self.value}"
        return copy

    @classmethod
    def get_priority_recommendations(
        cls, number_of_recommendations: int, recommendations: list["Recommendation"]
    ) -> list["Recommendation"]:
        recommendations_sorted_by_priority = sorted(
            recommendations, key=lambda recommendation: recommendation.priority
        )
        if len(recommendations_sorted_by_priority) < number_of_recommendations:
            return recommendations_sorted_by_priority
        return recommendations_sorted_by_priority[:number_of_recommendations]
