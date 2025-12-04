# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import re
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

from tobefair_framework.model.identifier.fairness_metric_id import FAIRnessMetricID
from tobefair_framework.model.identifier.id import SerialHierarchicalID


class FAIRnessTestID(BaseModel, SerialHierarchicalID[str]):
    value: str

    @property
    def raw_value(self) -> str:
        return self.value

    def get_parent_id(self) -> FAIRnessMetricID:
        raw_parent_metric_id = re.sub("-[0-9]+$", "", self.raw_value)
        return FAIRnessMetricID(value=raw_parent_metric_id)

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


class FAIRnessTestIDs(Enum):
    # GUID: Globally Unique Identifier
    F1_01MD_1_Hash_or_UUID = FAIRnessTestID(value="F1-01MD-1")
    F1_01MD_2_GUID = FAIRnessTestID(value="F1-01MD-2")
    # GUPRI: Globally Unique Persistent Resolvable Identifier
    F1_02MD_1_GUPRI = FAIRnessTestID(value="F1-02MD-1")
    F2_01M_1_citation_metadata = FAIRnessTestID(value="F2-01M-1")
    F2_01M_2_description_metadata = FAIRnessTestID(value="F2-01M-2")
    F2_01M_3 = FAIRnessTestID(value="F2-01M-3")
    F3_01M_1_metadata_contains_data_identifier = FAIRnessTestID(value="F3-01M-1")
    F3_02M_1_metadata_contains_metadata_identifier = FAIRnessTestID(value="F3-02M-1")
    F4_01M_1_metadata_retrievable_by_search_engines = FAIRnessTestID(value="F4-01M-1")
    A1_01M_1_access_rights_info_in_metadata = FAIRnessTestID(value="A1-01M-1")
    A1_02M_1_identifier_resolves_to_landing_page = FAIRnessTestID(value="A1-02M-1")
    A1_03M_1_standard_protocol_for_metadata = FAIRnessTestID(value="A1-03MD-1")
    A1_03MD_2_standard_protocol_in_data_link = FAIRnessTestID(value="A1-03MD-2")
    I1_01M_1_parsable_structured_metadata_available = FAIRnessTestID(value="I1-01M-1")
    I2_01M_1_namespace_are_available = FAIRnessTestID(value="I2-01M-1")
    R1_01M_1_minimal_data_information_available = FAIRnessTestID(value="R1-01M-1")
    R1_01M_2_data_type_and_size_available = FAIRnessTestID(value="R1-01M-2")
    R1_01M_3_measured_variable_information_available = FAIRnessTestID(value="R1-01M-3")
    R1_01M_4_data_type_matches_metadata = FAIRnessTestID(value="R1-01M-4")
    R1_01M_5_data_size_matches_metadata = FAIRnessTestID(value="R1-01M-5")
    R1_01M_6_measured_variable_matches_metadata = FAIRnessTestID(value="R1-01M-6")
    R1_1_01M_1_license_information_available = FAIRnessTestID(value="R1.1-01M-1")
    R1_2_01M_1_provenance_information_available = FAIRnessTestID(value="R1.2-01M-1")
    R1_2_01M_2_metadata_comply_to_standard_schema = FAIRnessTestID(value="R1.2-01M-2")
    R1_3_01M_1_community_specific_metadata = FAIRnessTestID(value="R1.3-01M-1")
    R1_3_01M_3_multidisciplinary_community_endorsed_metadata = FAIRnessTestID(
        value="R1.3-01M-3"
    )
    R1_3_02D_1_community_endorsed_file_format = FAIRnessTestID(value="R1.3-02D-1")
