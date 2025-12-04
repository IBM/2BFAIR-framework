# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import re
import uuid
from typing import List

from pydantic import BaseModel

from tobefair_framework.model.identifier.identifier_type import IdentifierType


class IdentifierInfo(BaseModel):
    identifier: str
    identifier_schemas: List[str] = []
    preferred_schema: str | None = None
    url: str | None = None

    def get_identifier_type(self) -> IdentifierType:
        if self.url:
            return IdentifierType.GUID
        if self.is_hash(identifier=self.identifier):
            return IdentifierType.HASH
        elif self.is_uuid(identifier=self.identifier):
            return IdentifierType.UUID
        return IdentifierType.NOT_IDENTIFIED

    @classmethod
    def is_uuid(cls, identifier: str) -> bool:
        try:
            uuid_version = uuid.UUID(identifier).version
            if uuid_version is not None:
                return True
            else:
                return False
        except ValueError:
            return False

    @classmethod
    def is_hash(cls, identifier: str) -> bool:
        import hashid

        try:
            hash = hashid.HashID()
            valid_hash = False
            for hash_type in hash.identifyHash(identifier):
                if re.search(r"^(sha|md5|blake)", hash_type.name, re.IGNORECASE):
                    valid_hash = True
            return valid_hash
        except Exception:
            return False


mocked_identifier_info = IdentifierInfo(identifier="")
