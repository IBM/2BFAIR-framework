# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Self

from tobefair_framework.model.composite.identifiable_composite_result import (
    IdentifiableCompositeResult,
)


class LeafResult(IdentifiableCompositeResult["LeafResult"]):
    def get_children(self) -> list["LeafResult"]:
        return [self]

    def sort_all(self):
        self.sort_results()

    def get_last_children(self) -> list["LeafResult"]:
        return [self]

    @classmethod
    def from_results(
        cls, results: List["LeafResult"], general_configuration: Dict
    ) -> List[Self]:
        return []

    def get_results(self) -> Dict:
        return {}

    def set_results(self, value):
        return

    @classmethod
    def _from_configuration_and_results(
        cls, configuration, results: List["LeafResult"]
    ) -> Self:
        return super()._from_configuration_and_results(configuration, results)
