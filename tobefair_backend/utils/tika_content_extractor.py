# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import re
from io import BytesIO
from typing import Any, List, TypeAlias, cast

from tika import parser

from tobefair_backend.model.resources.data_record import DataType
from tobefair_backend.model.response_wrapper import ResponseWrapper
from tobefair_backend.utils.list_utils import remove_duplicates

ParsedFile: TypeAlias = dict[str, None]


class TikaContentExtractor:

    def __init__(self, max_download_size: int, file: BytesIO) -> None:
        self.max_download_size = max_download_size
        self.file = file
        self.parse_file()

    @classmethod
    def from_response_wrapper(
        cls, response_wrapper: ResponseWrapper, max_download_size: int
    ) -> "TikaContentExtractor":
        file: BytesIO = response_wrapper.get_response_file_buffer()
        return TikaContentExtractor(max_download_size, file)

    def extract_content(self) -> str | None:
        if self.parsed_file is not None:
            return self.parsed_file.get("content")
        return None

    def get_file_content_types(self) -> List[DataType] | None:
        content_type_header_value: Any = (
            metadata.get("Content-Type")
            if (
                (parsed_file := self.parsed_file)
                and (metadata := cast(dict, parsed_file.get("metadata")))
            )
            else []
        )
        single_content_type_found = not isinstance(content_type_header_value, list)
        if single_content_type_found:
            tika_content_types = [content_type_header_value]
        else:
            tika_content_types = content_type_header_value
        tika_content_types = remove_duplicates(
            self.extend_mime_type_list(tika_content_types)
        )
        if tika_content_types:
            return [DataType(value=content_type) for content_type in tika_content_types]
        return None

    def extract_mime_types(self, tika_type_list: list[str]) -> list[str]:
        return [tika_type.split(";")[0] for tika_type in tika_type_list]

    # TODO: Understand what this method does
    def extend_mime_type_list(self, mime_list):
        if isinstance(mime_list, str):
            mime_list = [mime_list]
        for mime in mime_list:
            xm = re.split(r"/(?:[xX][-\.])?", mime)
            if len(xm) == 2:
                if str(xm[0] + "/" + xm[1]) not in mime_list:
                    mime_list.append(str(xm[0] + "/" + xm[1]))
        return mime_list

    def parse_file(self):
        try:
            parsed_file = parser.from_buffer(self.file.getvalue())
            parsed_file = cast(dict[str, None], parsed_file)
            self.parsed_file = parsed_file
        except Exception:
            self.parsed_file = None
