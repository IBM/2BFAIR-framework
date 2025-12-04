# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import Any, List

from pydantic import (
    BaseModel,
    ValidationError,
    ValidationInfo,
    model_serializer,
    model_validator,
)
from pydantic.functional_validators import ModelWrapValidatorHandler

from tobefair_framework.model.identifier.id import ID


class FAIRDimensionID(BaseModel, ID[str]):
    dimension_id: str

    def __lt__(self, other) -> bool:
        fair_dimension_id_raw_values: List[str] = ["F", "A", "I", "R"]
        if isinstance(other, FAIRDimensionID):
            try:
                self_index = fair_dimension_id_raw_values.index(self.raw_value)
                other_index = fair_dimension_id_raw_values.index(other.raw_value)
                return self_index < other_index
            except ValueError:
                return False
        return False

    @property
    def raw_value(self) -> str:
        return self.dimension_id

    def __hash__(self) -> int:
        return hash(self.raw_value)

    @model_validator(mode="wrap")
    @classmethod
    def validator(
        cls, values: Any, handler: ModelWrapValidatorHandler, info: ValidationInfo
    ):
        try:
            return handler(values)
        except ValidationError:
            if isinstance(values, str):
                return cls(dimension_id=values)
        return handler(values)

    @model_serializer
    def ser_model(self) -> str:
        return self.raw_value


class FAIRDimensionIDs(Enum):
    F = FAIRDimensionID(dimension_id="F")
    A = FAIRDimensionID(dimension_id="A")
    I = FAIRDimensionID(dimension_id="I")
    R = FAIRDimensionID(dimension_id="R")
