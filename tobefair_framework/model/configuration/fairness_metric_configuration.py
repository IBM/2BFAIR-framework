# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, ValidationError, field_validator

from tobefair_framework.model.alternate_test_behavior import AlternateTestBehavior
from tobefair_framework.model.composite.identifiable_composite import (
    IdentifiableComposite,
)
from tobefair_framework.model.configuration.fairness_test_configuration import (
    FAIRnessTestConfiguration,
)
from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricID
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID


class MetricPriority(str, Enum):
    Essential = "Essential"
    Important = "Important"
    Useful = "Useful"


class ScoringMechanism(str, Enum):
    alternative = "alternative"
    cumulative = "cumulative"


class FAIRnessMetricConfiguration(
    BaseModel, IdentifiableComposite[FAIRnessTestConfiguration]
):
    alternate_test_behavior: AlternateTestBehavior = AlternateTestBehavior.skip
    id: FAIRnessMetricID
    name: str
    priority: MetricPriority
    tests: Dict[FAIRnessTestID, FAIRnessTestConfiguration]
    scoring_mechanism: ScoringMechanism
    score: float = 0

    def get_children(self) -> List[FAIRnessTestConfiguration]:
        return list(self.tests.values())

    @property
    def get_id(self) -> FAIRnessMetricID:
        return self.id

    @field_validator("alternate_test_behavior")
    @classmethod
    def from_json(cls, value) -> AlternateTestBehavior:
        if isinstance(value, str):
            return AlternateTestBehavior._member_map_[value].value
        elif isinstance(value, AlternateTestBehavior):
            return value
        raise ValidationError
