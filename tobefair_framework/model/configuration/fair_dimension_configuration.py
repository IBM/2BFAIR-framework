# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List

from pydantic import BaseModel

from tobefair_framework.model.composite.identifiable_composite import (
    IdentifiableComposite,
)
from tobefair_framework.model.configuration.fair_principle_configuration import (
    FAIRPrincipleConfiguration,
)
from tobefair_framework.model.identifier.fair_dimension_id import (
    FAIRDimensionID,
    FAIRDimensionIDs,
)
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID


class FAIRDimensionConfiguration(
    BaseModel, IdentifiableComposite[FAIRPrincipleConfiguration]
):
    id: FAIRDimensionID
    name: str
    principles: Dict[FAIRPrincipleID, FAIRPrincipleConfiguration]

    @property
    def get_id(self) -> FAIRDimensionID:
        return self.id

    @classmethod
    def get_dimension_name_from_id(cls, id: FAIRDimensionID) -> str:
        match id:
            case FAIRDimensionIDs.F.value:
                return "Findability"
            case FAIRDimensionIDs.A.value:
                return "Accessibility"
            case FAIRDimensionIDs.I.value:
                return "Interoperability"
            case FAIRDimensionIDs.R.value:
                return "Reusability"
            case _:
                raise Exception("Dimension ID not recognized")

    def get_children(self) -> List[FAIRPrincipleConfiguration]:
        return list(self.principles.values())
