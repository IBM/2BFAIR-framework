# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import Any

from pydantic import (
    BaseModel,
    ValidationError,
    ValidationInfo,
    model_serializer,
    model_validator,
)
from pydantic.functional_validators import ModelWrapValidatorHandler

from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionID
from tobefair_framework.model.identifier.id import SerialHierarchicalID


class FAIRPrincipleID(BaseModel, SerialHierarchicalID[str]):

    principle_id: str

    @property
    def raw_value(self) -> str:
        return str(self.principle_id)

    def get_parent_id(self) -> FAIRDimensionID:
        return FAIRDimensionID(dimension_id=self.raw_value[0])

    def __hash__(self) -> int:
        return hash(self.raw_value)

    @model_serializer
    def ser_model(self) -> str:
        return self.raw_value

    @model_validator(mode="wrap")
    @classmethod
    def validator(
        cls, values: Any, handler: ModelWrapValidatorHandler, info: ValidationInfo
    ):
        try:
            return handler(values)
        except ValidationError:
            if isinstance(values, str):
                return cls(principle_id=values)
        return handler(values)


class FAIRPrincipleIDs(Enum):
    F1 = FAIRPrincipleID(principle_id="F1")
    F2 = FAIRPrincipleID(principle_id="F2")
    F3 = FAIRPrincipleID(principle_id="F3")
    F4 = FAIRPrincipleID(principle_id="F4")
    A1 = FAIRPrincipleID(principle_id="A1")
    I1 = FAIRPrincipleID(principle_id="I1")
    I2 = FAIRPrincipleID(principle_id="I2")
    R1 = FAIRPrincipleID(principle_id="R1")
    R1_1 = FAIRPrincipleID(principle_id="R1.1")
    R1_2 = FAIRPrincipleID(principle_id="R1.2")
    R1_3 = FAIRPrincipleID(principle_id="R1.3")
