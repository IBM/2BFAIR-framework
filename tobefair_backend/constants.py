# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

EVALUATORS_PACKAGE: str = "tobefair_backend.principle_evaluators"
MAXIMUM_RESPONSE_SIZE = 1_000_000
FILE_FORMAT_PATH = "tobefair_backend/database/file_formats.json"
METADATA_FORMAT_PATH = "tobefair_backend/database/metadata_formats.json"
METADATA_OFFERING_METHOD_PATH = (
    "tobefair_backend/database/metadata_offering_methods.json"
)
METADATA_SOURCE_PATH = "tobefair_backend/database/metadata_sources.json"
METADATA_STANDARD_PATH = "tobefair_backend/database/metadata_standards.json"
STANDARD_URI_PROTOCOL_PATH = "tobefair_backend/database/standard_uri_protocols.json"
ACCESS_LEVEL_GROUP_PATH = "database/access_rights.json"
SCHEMA_ORG_DATASET_TYPES = [
    "dataset",
    "https://schema.org/dataset",
    "http://schema.org/dataset",
]
FAIRNESS_CONFIGURATION_FILE_PATH = (
    "./tobefair_backend/config/fairness_configuration.json"
)
