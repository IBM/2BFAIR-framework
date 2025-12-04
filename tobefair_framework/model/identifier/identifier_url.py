# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel


class IdentifierURL(BaseModel):
    url: str
    is_web_accessible: bool
