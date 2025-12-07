# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

from tobefair_backend.utils.dict_utils import remove_empty_fields


class TestDictUtils(unittest.TestCase):
    def test_remove_empty_fields(self):
        d1: dict = {1: "", 2: None, 3: []}
        self.assertEqual(remove_empty_fields(d1), {})

        d2: dict = {4: "foo", 5: 2, 6: [1, 2]}
        self.assertEqual(remove_empty_fields(d2), d2)

        d3 = d1.copy()
        d3.update(d2)
        self.assertEqual(remove_empty_fields(d3), d2)
