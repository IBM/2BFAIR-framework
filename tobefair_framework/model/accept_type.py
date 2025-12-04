# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import List

from pydantic import BaseModel


class AcceptType(BaseModel):
    def make_accept_header(self):
        header = ""
        for mime_type in self.mime_types:
            header += mime_type + ", "
        return header[:-2]

    mime_types: List[str]
