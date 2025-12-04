# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel


class FAIRnessEvaluationRequest(BaseModel):
    resource_id: str = "https://doi.org/10.1594/PANGAEA.893286"
    community: str | None = None
    task: str | None = None
