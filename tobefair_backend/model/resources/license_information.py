# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel


class LicenseInformation(BaseModel):
    raw_value: str
