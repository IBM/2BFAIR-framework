# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel


class LandingPage(BaseModel):
    encoded_hmtl_body: bytes | None = None
    decoded_html_body: str
    url: str
