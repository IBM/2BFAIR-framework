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

from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID
from tobefair_framework.model.identifier.id import SerialHierarchicalID


class FAIRnessMetricID(BaseModel, SerialHierarchicalID[str]):
    value: str

    @property
    def raw_value(self) -> str:
        return self.value

    def get_parent_id(self) -> FAIRPrincipleID:
        id_parts = self.raw_value.split("-")
        parent_id_raw_value = id_parts[0]
        return FAIRPrincipleID(principle_id=parent_id_raw_value)

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
                return cls(value=values)
        return handler(values)


class FAIRnessMetricIDs(Enum):
    F1_01MD_GUID_identifier = FAIRnessMetricID(value="F1-01MD")
    F1_02MD_persistent_identifier = FAIRnessMetricID(value="F1-02MD")
    F2_01M_rich_metadata = FAIRnessMetricID(value="F2-01M")
    F3_01M_metadata_contains_data_identifier = FAIRnessMetricID(value="F3-01M")
    F3_02M_metadata_contains_metadata_identifier = FAIRnessMetricID(value="F3-02M")
    F4_01M_metadata_are_machine_accessible = FAIRnessMetricID(value="F4-01M")
    A1_01M_metadata_contains_access_rights = FAIRnessMetricID(value="A1-01M")
    A1_02M_metadata_and_data_retrievable_by_identifier = FAIRnessMetricID(
        value="A1-02M"
    )
    A1_03MD_metadata_and_data_accessible_via_standardized_protocol = FAIRnessMetricID(
        value="A1-03MD"
    )
    I1_01M_metadata_represented_with_formal_language = FAIRnessMetricID(value="I1-01M")
    I2_01M_metadata_uses_semantic_resources = FAIRnessMetricID(value="I2-01M")
    R1_01MD_metadata_specifies_content_of_data = FAIRnessMetricID(value="R1-01MD")
    R1_1_01M_usage_license_available = FAIRnessMetricID(value="R1.1-01M")
    R1_2_01M_provenance_information_available = FAIRnessMetricID(value="R1.2-01M")
    R1_3_01M_community_endorsed_metadata = FAIRnessMetricID(value="R1.3-01M")
    R1_3_02D_community_metadata_format = FAIRnessMetricID(value="R1.3-02D")
