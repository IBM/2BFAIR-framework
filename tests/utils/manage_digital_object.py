# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json

from tobefair_backend.collector.digital_object_collector_from_url import (
    DigitalObjectCollectorFromURL,
)
from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.metadata.metadata_record import MetadataRecord

# from tobefair_backend.collector.metadata_source_repository_app import (
#     MetadataSourceRepositoryApp,
# )
# from tobefair_framework.model.metadata_standard import MetadataStandard

TEST_DATA_FOLDER = "tests/data_for_testing/"
DIGITAL_OBJECT_DATA_FILE_PATH = f"{TEST_DATA_FOLDER}/pangaea_digital_object.json"
FAIRNESS_EVALUATION_RESPONSE_FILE_PATH = (
    f"{TEST_DATA_FOLDER}/pangaea_evaluation_response.json"
)


def get_metadata_record_to_dict(metadata_record: MetadataRecord) -> dict:
    # save metadata source and metadata standard to separate files
    # since they do not inherit from pydantic.BaseModel
    metadata_record_dict = {
        "is_machine_retrieved": metadata_record.is_machine_retrieved,
        "raw_value": metadata_record.raw_value,
    }
    # TODO FIX IT
    # if metadata_source := metadata_record.metadata_source_key:
    #     metadata_record_dict["metadata_source"] = metadata_source.model_dump(
    #         mode="json"
    #     )
    # if metadata_standard := metadata_record.metadata_standard_name:
    #     metadata_record_dict["metadata_standard"] = metadata_standard.model_dump(
    #         mode="json"
    #     )

    return metadata_record_dict


def save_digital_object_info_to_file(resource_id: str) -> DigitalObjectInfo | None:
    if digital_object := (
        DigitalObjectCollectorFromURL().get_digital_object_info(
            raw_identifier=resource_id,
            metadata_collector=MetadataCollectorSchemaOrgJsonLD(),
        )
    ):
        digital_object_dict = {}
        # workaround required because
        # MetadataRecord does not inherit from pydantic.BaseModel
        if digital_object.metadata_record:
            digital_object_dict["metadata_record"] = get_metadata_record_to_dict(
                digital_object.metadata_record
            )
        previous_metadata_record = digital_object.metadata_record
        digital_object.metadata_record = None
        digital_object_dict["digital_object_info"] = digital_object.model_dump(
            mode="json"
        )
        with open(DIGITAL_OBJECT_DATA_FILE_PATH, "w") as f:
            json.dump(digital_object_dict, f, indent=4)
        digital_object.metadata_record = previous_metadata_record
        return digital_object
    return None


def read_digital_object_from_file() -> DigitalObjectInfo:
    with open(DIGITAL_OBJECT_DATA_FILE_PATH, "r") as file:
        digital_object_dict = json.load(file)
        digital_object: DigitalObjectInfo = DigitalObjectInfo.model_validate(
            digital_object_dict["digital_object_info"]
        )
        if metadata_record_dict := digital_object_dict.get("metadata_record"):
            metadata_record: MetadataRecord = MetadataRecord(
                is_machine_retrieved=metadata_record_dict["is_machine_retrieved"],
                raw_value=metadata_record_dict["raw_value"],
            )
            # The code should be here
            digital_object.metadata_record = metadata_record

    return digital_object


# TODO fixme
# metadata_record.metadata_source_key = (
#     MetadataSourceRepositoryApp.get_metadata_source(
#         digital_object_dict["metadata_record"]["metadata_source"]
#     )
# )
# # check if metadata_source.method was read properly
# if (
#     metadata_record.metadata_source_key
#     and not metadata_record.metadata_source_key.method
#     and digital_object_dict["metadata_record"]["metadata_source"]["method"]
# ):
#     if method := MetadataSourceRepositoryApp.get_metadata_source_method(
#         digital_object_dict["metadata_record"]["metadata_source"]["method"]
#     ):
#         metadata_record.metadata_source_key.method = method
#     else:
#         raise Exception("Could not parse metadata offering method.")
# # check if metadata_source.format was read properly
# if (
#     metadata_record.metadata_source_key
#     and not metadata_record.metadata_source_key.format
#     and digital_object_dict["metadata_record"]["metadata_source"]["format"]
# ):
#     if format := MetadataSourceRepositoryApp.get_metadata_source_format(
#         digital_object_dict["metadata_record"]["metadata_source"]["format"]
#     ):
#         metadata_record.metadata_source_key.format = format
#     else:
#         raise Exception("Could not parse metadata format.")
# if metadata_standard_dict := metadata_record_dict.get("metadata_standard"):
#     metadata_record.metadata_standard_name = (
#         MetadataStandard.model_validate(metadata_standard_dict)
#     )


def check_write_and_read_digital_object():
    resource_id = "https://doi.org/10.1594/PANGAEA.893286"
    # self.save_fairness_evaluation_response_to_file(
    #     resource_id=resource_id, file_path=FAIRNESS_EVALUATION_RESPONSE_FILE_PATH
    # )
    saved_digital_object: DigitalObjectInfo | None = save_digital_object_info_to_file(
        resource_id=resource_id
    )

    digital_object: DigitalObjectInfo = read_digital_object_from_file()

    assert (
        saved_digital_object == digital_object
    ), "Saved to file digital object is different from read from file."
