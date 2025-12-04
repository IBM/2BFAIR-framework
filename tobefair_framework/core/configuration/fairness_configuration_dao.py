# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod

from pydantic import BaseModel

from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)


class FAIRnessConfigurationDAO(ABC, BaseModel):

    @abstractmethod
    def read_configuration(self) -> FAIRnessConfiguration:
        return FAIRnessConfiguration()
