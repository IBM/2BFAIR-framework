# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import threading
from typing import Literal

from pydantic import BaseModel

from tobefair_framework.core.notification.contexts import request_id_var


class Notification(BaseModel):
    type: Literal["error", "success", "warning", "information"]
    title: str
    description: str


registry_lock = threading.Lock()


class NotificationRegistry:

    notification_registry: dict[str, list[Notification]] = {}

    @classmethod
    def add_notification(cls, notification: Notification) -> None:
        request_id = request_id_var.get()
        with registry_lock:
            if request_id not in cls.notification_registry.keys():
                cls.notification_registry[request_id] = []
            cls.notification_registry[request_id].append(notification)

    @classmethod
    def get_notifications(cls) -> list[Notification]:
        request_id = request_id_var.get()
        with registry_lock:
            if request_id not in cls.notification_registry.keys():
                return []
            return cls.notification_registry[request_id]

    @classmethod
    def clear_notifications(cls) -> None:
        request_id = request_id_var.get()
        with registry_lock:
            if request_id in cls.notification_registry.keys():
                del cls.notification_registry[request_id_var.get()]
