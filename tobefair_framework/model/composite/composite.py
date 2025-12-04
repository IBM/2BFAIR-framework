# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

Child = TypeVar("Child", bound="Composite")


class Composite(Generic[Child], ABC):
    @abstractmethod
    def get_children(self) -> List[Child] | None:
        pass
