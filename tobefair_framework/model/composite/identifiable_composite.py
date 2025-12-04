# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from tobefair_framework.model.composite.composite import Composite
from tobefair_framework.model.identifier.id import ID

IdentifiableChild = TypeVar("IdentifiableChild", bound="IdentifiableComposite")


class IdentifiableComposite(
    Generic[IdentifiableChild], Composite[IdentifiableChild], ABC
):
    @property
    @abstractmethod
    def get_id(self) -> ID:
        pass
