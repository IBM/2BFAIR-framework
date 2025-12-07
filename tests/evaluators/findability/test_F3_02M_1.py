# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json
from unittest import TestCase

from tests.evaluators.fairness_principle_evaluation_tester import (
    FAIRNESS_CONFIGURATION_FOR_TESTS,
)
from tobefair_backend.principle_evaluators.identifier_in_metadata_evaluator import (
    IdentifierInMetadataEvaluator,
)
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class TestF302Metric(TestCase):
    def test_f3_02m_1_metadata_identifier_in_metadata(self):
        path = "tests/data_for_testing/pangaea-metadata-in-schema.org.json"
        with open(path, "r") as file:
            text = file.read()
            metadata_record = MetadataRecord(
                is_machine_retrieved=False, raw_value=json.loads(text)
            )
            evaluator = IdentifierInMetadataEvaluator(
                fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
            )
            result = evaluator._evaluate_json_ld_contains_metadata_info(
                json_ld_metadata=metadata_record.raw_value,
                meta_data_identifier="https://doi.pangaea.de/10.1594/PANGAEA.908011",
            )
            self.assertTrue(result)

    def test_f3_02m_1_metadata_identifier_not_in_metadata(self):
        path = "tests/data_for_testing/pangaea-metadata-in-schema.org.json"
        with open(path, "r") as file:
            text = file.read()
            metadata_record = MetadataRecord(
                is_machine_retrieved=False, raw_value=json.loads(text)
            )
            evaluator = IdentifierInMetadataEvaluator(
                fairness_configuration=FAIRNESS_CONFIGURATION_FOR_TESTS
            )
            result = evaluator._evaluate_json_ld_contains_metadata_info(
                json_ld_metadata=metadata_record.raw_value,
                meta_data_identifier="wrong_url_identifier",
            )
            self.assertFalse(result)
