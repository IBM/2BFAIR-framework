# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class AlternateTestBehavior(Enum):
    skip = "skip"
    fail = "fail"
