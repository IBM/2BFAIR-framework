# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json

from pydantic import ValidationError

from tobefair_framework.core.configuration.fairness_configuration_dao import (
    FAIRnessConfigurationDAO,
)
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)


class FAIRnessConfigurationFileDAO(FAIRnessConfigurationDAO):

    file_path: str

    def read_configuration(self) -> FAIRnessConfiguration:
        f = open(self.file_path)
        json_data = json.load(f)
        f.close()
        try:
            configuration = FAIRnessConfiguration()
            configuration.set_configuration(json_data=json_data)
            return configuration
        except ValidationError as e:
            raise Exception(e)
