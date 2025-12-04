# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from tobefair_framework.core.notification.contexts import request_id_var
from tobefair_framework.core.notification.notification_context import (
    NotificationRegistry,
)


class NotificationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        context_token = request_id_var.set(request_id)
        try:
            response = await call_next(request)
            return response
        finally:
            NotificationRegistry.clear_notifications()
            request_id_var.reset(context_token)
