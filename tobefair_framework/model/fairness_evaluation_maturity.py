# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import Any, List

from pydantic import BaseModel, ValidationInfo, model_validator
from pydantic.functional_validators import ModelWrapValidatorHandler


class FAIRnessMaturity(BaseModel):
    value: str

    @model_validator(mode="wrap")
    @classmethod
    def validator(
        cls, values: Any, handler: ModelWrapValidatorHandler, info: ValidationInfo
    ) -> "FAIRnessMaturity":
        if isinstance(values, str):
            return cls(value=values)
        return handler(values)

    def __lt__(self, other: "FAIRnessMaturity") -> bool:
        return FAIRnessMaturities.all().index(self) < FAIRnessMaturities.all().index(
            other
        )


class FAIRnessMaturities(Enum):
    Incomplete = FAIRnessMaturity(value="Incomplete")
    Initial = FAIRnessMaturity(value="Initial")
    Moderate = FAIRnessMaturity(value="Moderate")
    Advanced = FAIRnessMaturity(value="Advanced")

    @classmethod
    def all(cls) -> List[FAIRnessMaturity]:
        return [maturity.value for maturity in FAIRnessMaturities]


def get_highest_maturity(maturity_a, maturity_b):
    if maturity_a == FAIRnessMaturities.Incomplete.value:
        return maturity_b
    if maturity_b == FAIRnessMaturities.Incomplete.value:
        return maturity_a
    if maturity_a == FAIRnessMaturities.Initial.value:
        return maturity_b
    if maturity_b == FAIRnessMaturities.Initial.value:
        return maturity_a
    if maturity_a == FAIRnessMaturities.Moderate.value:
        return maturity_b
    if maturity_b == FAIRnessMaturities.Moderate.value:
        return maturity_a
    return maturity_a
