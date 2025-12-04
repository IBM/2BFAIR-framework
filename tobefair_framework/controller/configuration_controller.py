# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.framework_constants import (
    FAIRNESS_CONFIGURATION_FILE_PATH_FOR_THE_FRAMEWORK,
)
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)


class ConfigurationController:

    @classmethod
    def get_configuration(cls) -> FAIRnessConfiguration:
        fairness_configuration = FAIRnessConfigurationFileDAO(
            file_path=FAIRNESS_CONFIGURATION_FILE_PATH_FOR_THE_FRAMEWORK
        )
        return fairness_configuration.read_configuration()
