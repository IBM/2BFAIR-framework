# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

from tobefair_framework.model.metadata.metadata_standard import (
    ExternalID,
    MetadataStandard,
    MetadataStandardType,
)


class TestMetadataStandard(unittest.TestCase):
    def test_get_type_from_subjects_generic(self):
        self.assertEqual(
            MetadataStandard.get_type_from_subjects(["sciences"]),
            MetadataStandardType.Generic,
        )
        self.assertEqual(
            MetadataStandard.get_type_from_subjects(
                ["Multidisciplinary", "Multidisciplinary"]
            ),
            MetadataStandardType.Generic,
        )
        self.assertEqual(
            MetadataStandard.get_type_from_subjects(
                ["Multidisciplinary", "scientific"]
            ),
            MetadataStandardType.Disciplinary,
        )
        self.assertEqual(
            MetadataStandard.get_type_from_subjects(
                ["Multidisciplinary", "cristallogy"]
            ),
            MetadataStandardType.Disciplinary,
        )

    def test_equals(self):
        schema_org_1 = MetadataStandard(
            name="Schema.org",
            external_ids=[
                ExternalID(value="https://doi.org/10.25504/FAIRsharing.hzdzq8")
            ],
        )
        schema_org_2 = MetadataStandard(
            name="Schema.org",
        )
        schema_org_3 = MetadataStandard(
            name="Not_Schema.org",
            subjects=[],
            external_ids=[
                ExternalID(value="https://doi.org/10.25504/FAIRsharing.hzdzq8")
            ],
        )
        schema_org_4 = MetadataStandard(
            name="Not_Schema.org",
            subjects=[],
            external_ids=[
                ExternalID(value="https://doi.org/10.25504/FAIRsharing.hzdzq8"),
                ExternalID(value="msc:m101"),
                ExternalID(value="https://schema.org"),
                ExternalID(value="https://schema.org/docs/schemas.html"),
            ],
        )
        self.assertEqual(schema_org_1, schema_org_4)
        self.assertNotEqual(schema_org_2, schema_org_4)
        self.assertEqual(schema_org_3, schema_org_4)
        self.assertEqual(schema_org_1, schema_org_3)
        self.assertNotEqual(schema_org_2, schema_org_3)
