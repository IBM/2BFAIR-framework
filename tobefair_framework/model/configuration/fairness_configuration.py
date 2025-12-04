# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List

from pydantic import BaseModel

from tobefair_framework.model.composite.identifiable_composite import (
    IdentifiableComposite,
)
from tobefair_framework.model.configuration.fair_dimension_configuration import (
    FAIRDimensionConfiguration,
)
from tobefair_framework.model.configuration.fair_principle_configuration import (
    FAIRPrincipleConfiguration,
)
from tobefair_framework.model.configuration.fairness_metric_configuration import (
    FAIRnessMetricConfiguration,
)
from tobefair_framework.model.configuration.fairness_test_configuration import (
    FAIRnessTestConfiguration,
)
from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionID
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID
from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricID
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID
from tobefair_framework.model.identifier.id import ID


def flatten(composite: IdentifiableComposite) -> Dict[ID, IdentifiableComposite]:
    flattened_self = {composite.get_id: composite}
    if not (children := composite.get_children()):
        return flattened_self
    for child in children:
        flattened_self.update(flatten(child))
    return flattened_self


class FAIRnessConfiguration(BaseModel):

    configuration: Dict[FAIRDimensionID, FAIRDimensionConfiguration] = {}
    _flat_configuration: Dict[ID, IdentifiableComposite] = {}

    @property
    def flat_configuration(self) -> Dict[ID, Any]:
        if self._flat_configuration == {}:
            for dimension in self.configuration.values():
                self._flat_configuration.update(flatten(dimension))
        return self._flat_configuration

    def get_fairness_tests(self) -> Dict[FAIRnessTestID, FAIRnessTestConfiguration]:
        fairness_tests = {}
        context = self.configuration
        for dimension_key in context:
            dimension = context[dimension_key]
            for principle_key in dimension.principles:
                principle = dimension.principles[principle_key]
                for metric_key in principle.metrics:
                    metric = principle.metrics[metric_key]
                    fairness_tests.update(metric.tests)
        return fairness_tests

    def get_fairness_test_ids_to_evaluate(self) -> List[FAIRnessTestID]:
        all_tests = self.get_fairness_tests()
        return [test.id for test in all_tests.values() if not test.skip]

    def get_fairness_test_from_id(
        self, id: FAIRnessTestID
    ) -> FAIRnessTestConfiguration:
        fairness_tests = self.get_fairness_tests()
        return fairness_tests[id]

    def get_principle(
        self, principle_id: FAIRPrincipleID
    ) -> FAIRPrincipleConfiguration:
        return self.configuration[principle_id.get_parent_id()].principles[principle_id]

    def get_metric(
        self, principle_id: FAIRPrincipleID, metric_id: FAIRnessMetricID
    ) -> FAIRnessMetricConfiguration:
        principle = self.get_principle(principle_id=principle_id)
        return principle.metrics[metric_id]

    def set_configuration(self, json_data: dict):
        for json_dimension_id, json_dimension in json_data.items():
            self.configuration.update(
                {
                    FAIRDimensionID(
                        dimension_id=json_dimension_id
                    ): FAIRDimensionConfiguration.model_validate(json_dimension)
                }
            )
