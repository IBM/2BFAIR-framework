# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.framework_constants import (
    FAIRNESS_CONFIGURATION_FILE_PATH_FOR_THE_FRAMEWORK,
)


class TestConfigurationFileDAO(TestCase):

    def test_read_file(self):
        fairness_configuration_dao = FAIRnessConfigurationFileDAO(
            file_path=FAIRNESS_CONFIGURATION_FILE_PATH_FOR_THE_FRAMEWORK
        )
        fairness_configuration = fairness_configuration_dao.read_configuration()
        self.assertIsNotNone(fairness_configuration)
