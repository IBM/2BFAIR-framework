# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List

from pydantic import BaseModel

from tobefair_framework.model.composite.identifiable_composite import (
    IdentifiableComposite,
)
from tobefair_framework.model.configuration.fairness_metric_configuration import (
    FAIRnessMetricConfiguration,
)
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID
from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricID


class FAIRPrincipleConfiguration(
    BaseModel, IdentifiableComposite[FAIRnessMetricConfiguration]
):
    id: FAIRPrincipleID
    name: str
    metrics: Dict[FAIRnessMetricID, FAIRnessMetricConfiguration]

    @property
    def get_id(self) -> FAIRPrincipleID:
        return self.id

    def get_children(self) -> List[FAIRnessMetricConfiguration]:
        return list(self.metrics.values())
