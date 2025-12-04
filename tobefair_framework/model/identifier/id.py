# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

RawValue = TypeVar("RawValue", covariant=True)


class ID(ABC, Generic[RawValue]):

    @property
    @abstractmethod
    def raw_value(self) -> RawValue:
        pass

    @abstractmethod
    def __lt__(self, other) -> bool:
        pass


class SerialHierarchicalID(ID[RawValue]):
    @abstractmethod
    def get_parent_id(self) -> ID:
        pass

    def __lt__(self, other) -> bool:
        if isinstance(other, SerialHierarchicalID):
            return self.raw_value < other.raw_value
        return False

    def is_descendant_of(self, ancestor: ID, generations: int) -> bool:
        descendant: ID = self
        while generations > 0 and isinstance(descendant, SerialHierarchicalID):
            descendant = descendant.get_parent_id()
            generations -= 1
        return descendant == ancestor
