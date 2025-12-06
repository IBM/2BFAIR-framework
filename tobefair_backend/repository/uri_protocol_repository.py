# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json
from typing import ClassVar, List

from tobefair_backend.constants import STANDARD_URI_PROTOCOL_PATH
from tobefair_backend.model.uri_protocol import URIProtocol


class URIProtocolRepository:
    _all: ClassVar[List[URIProtocol] | None] = None

    @classmethod
    def all(cls) -> List[URIProtocol]:
        if cls._all is None:
            path = STANDARD_URI_PROTOCOL_PATH
            with open(path, "r") as file:
                json_string = file.read()
                json_dict = json.loads(json_string)
                cls._all = [
                    uri_protocol
                    for protocol_dict in json_dict
                    if (
                        uri_protocol := URIProtocol.model_validate_json(
                            json.dumps(protocol_dict)
                        )
                    )
                ]
            return cls._all
        return cls._all
