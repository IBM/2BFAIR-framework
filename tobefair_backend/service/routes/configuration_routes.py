# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from fastapi import APIRouter

from tobefair_framework.controller.configuration_controller import (
    ConfigurationController,
)
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)

configuration_router = APIRouter()

TAG_FAIRNESS_CONFIGURATION = "Configuration"


@configuration_router.get("/configuration", tags=[TAG_FAIRNESS_CONFIGURATION])
async def configuration() -> FAIRnessConfiguration:
    return ConfigurationController.get_configuration()
