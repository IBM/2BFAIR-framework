# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from contextvars import ContextVar

request_id_var: ContextVar[str] = ContextVar("request_id", default="")
