# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class IdentifierType(str, Enum):
    UUID = "uuid"
    HASH = "hash"
    GUID = "guid"
    NOT_IDENTIFIED = "not identified"
