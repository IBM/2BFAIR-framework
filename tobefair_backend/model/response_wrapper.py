# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from http.client import HTTPResponse
from io import BytesIO

from tobefair_backend.model.resources.data_size import DataSize


class ResponseWrapper:

    def __init__(self, http_response: HTTPResponse, maximum_response_size: int):
        self.http_response = http_response
        self.file_buffer = self.make_response_file_buffer(maximum_response_size)

    def get_response_file_buffer(self) -> BytesIO:
        return self.file_buffer

    def make_response_file_buffer(self, max_response_size: int) -> BytesIO:
        file_buffer = BytesIO()
        data_record_content = self.http_response.read(max_response_size)
        file_buffer.write(data_record_content)
        return file_buffer

    def get_response_content_size(self, max_response_size: int) -> DataSize:
        with self.get_response_file_buffer() as response_file_buffer:
            size = DataSize(value=response_file_buffer.getbuffer().nbytes)
        return size

    @property
    def wrapped_value(self) -> HTTPResponse:
        return self.http_response
