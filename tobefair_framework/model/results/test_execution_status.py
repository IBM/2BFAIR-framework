# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class TestExecutionStatus(str, Enum):
    passed = "passed"
    failed = "failed"
    not_executed = "not executed"
