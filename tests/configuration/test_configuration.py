# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest
from typing import Dict

from tobefair_backend.constants import FAIRNESS_CONFIGURATION_FILE_PATH
from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.model.configuration.fairness_metric_configuration import (
    ScoringMechanism,
)
from tobefair_framework.model.configuration.fairness_test_configuration import (
    FAIRnessTestConfiguration,
)
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID


class TestConfiguration(unittest.TestCase):

    def setUp(self) -> None:
        fairness_configuration_dao = FAIRnessConfigurationFileDAO(
            file_path=FAIRNESS_CONFIGURATION_FILE_PATH
        )
        self.configuration = (
            fairness_configuration_dao.read_configuration().configuration
        )

    def test_configured_scores(self):
        def check_alternative_scoring_mechanism(
            tests: Dict[FAIRnessTestID, FAIRnessTestConfiguration],
        ):
            # One test should have score equal to 1
            for test_id, test in tests.items():
                if test.max_score == 1:
                    return True

        def check_cumulative_scoring_mechanism(
            tests: Dict[FAIRnessTestID, FAIRnessTestConfiguration],
        ):
            # Total score should be equal to 1
            total_score = 0.0
            for test_id, test in tests.items():
                total_score = total_score + test.max_score
            return total_score

        self.assertIsNotNone(self.configuration)
        context = self.configuration
        for dimension_id, dimension in context.items():
            for principle_id, principle in dimension.principles.items():
                for metric_id, metric in principle.metrics.items():
                    if metric.scoring_mechanism == ScoringMechanism.alternative:
                        self.assertTrue(
                            check_alternative_scoring_mechanism(tests=metric.tests),
                            (
                                f"At least one test of the metric {metric.id} "
                                "should have score equals to 1"
                            ),
                        )
                    else:  # check cumulative scoring mechanism
                        self.assertEqual(
                            check_cumulative_scoring_mechanism(tests=metric.tests),
                            1.0,
                            (
                                f"The sum of tests' scores of metric {metric.id} "
                                "should be equal to 1."
                            ),
                        )
