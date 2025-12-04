# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod
from typing import Dict, List, Self, TypeVar

from typing_extensions import Generic

from tobefair_framework.model.composite.composite import Composite
from tobefair_framework.model.composite.identifiable_composite import (
    IdentifiableComposite,
)
from tobefair_framework.model.identifier.id import SerialHierarchicalID
from tobefair_framework.model.results.test_specific_recommendation import (
    TestSpecificRecommendation,
)

CompositeResultChild = TypeVar(
    "CompositeResultChild", bound="IdentifiableCompositeResult"
)


class CompositeResult(
    Generic[CompositeResultChild], Composite[CompositeResultChild], ABC
):

    @abstractmethod
    def get_results(self) -> Dict:
        pass

    @abstractmethod
    def set_results(self, value):
        pass

    def get_total_score(self) -> float:
        total_score: float = 0
        for child in self.get_children():
            total_score += child.get_total_score()
        return total_score

    def get_max_total_score(self) -> float:
        max_total_score: float = 0
        for child in self.get_children():
            max_total_score += child.get_max_total_score()
        return max_total_score

    def get_children(self) -> list[CompositeResultChild]:
        try:
            results = self.get_results()
            return list(results.values())
        except AttributeError:
            raise NotImplementedError

    def get_recommendations(self) -> list:
        recommendations = []
        for child in self.get_children():
            recommendations += child.get_recommendations()
        return recommendations

    def get_necessary_recommendations(self) -> list:
        recommendations = []
        for child in self.get_children():
            recommendations += child.get_necessary_recommendations()
        return recommendations

    def get_last_children(self) -> list[CompositeResultChild]:
        accumulator = []
        [
            accumulator := accumulator + child.get_last_children()
            for child in self.get_children()
        ]
        return accumulator

    def sort_results(self):
        try:
            results = self.get_results()
            sorted_results = dict(sorted(results.items()))
            self.set_results(sorted_results)
        except Exception:
            return

    def sort_all(self):
        for child in self.get_children():
            child.sort_all()
        self.sort_results()

    def get_necessary_test_specific_recommendations(
        self,
    ) -> list[TestSpecificRecommendation]:
        recommendations = []
        for child in self.get_children():
            recommendations += child.get_necessary_test_specific_recommendations()
        return recommendations

    @classmethod
    @abstractmethod
    def _from_configuration_and_results(
        cls, configuration, results: List[CompositeResultChild]
    ) -> Self:
        pass

    @classmethod
    def from_results(
        cls,
        results: List[CompositeResultChild],
        general_configuration: Dict,
    ) -> List[Self]:

        ids = set(
            [
                result.get_id.get_parent_id()
                for result in results
                if result is not None
                if isinstance(result.get_id, SerialHierarchicalID)
            ]
        )
        d = {
            id: [
                result
                for result in results
                if result is not None
                if isinstance(result.get_id, SerialHierarchicalID)
                and result.get_id.get_parent_id() == id
            ]
            for id in ids
        }
        return [
            cls._from_configuration_and_results(
                configuration=configuration, results=d[parent_id]
            )
            for parent_id in d
            if (configuration := general_configuration.get(parent_id))
        ]


IdentifiableCompositeResultChild = TypeVar(
    "IdentifiableCompositeResultChild", bound="IdentifiableCompositeResult"
)


class IdentifiableCompositeResult(
    Generic[IdentifiableCompositeResultChild],
    CompositeResult[IdentifiableCompositeResultChild],
    IdentifiableComposite[IdentifiableCompositeResultChild],
):
    pass
