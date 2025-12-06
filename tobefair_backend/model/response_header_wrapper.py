from http.client import HTTPMessage

from tobefair_backend.model.resources.data_size import DataSize, DataType


class ResponseHeaderWrapper:

    def __init__(self, wrapped_response_header: HTTPMessage):
        self._wrapped_value = wrapped_response_header

    def get_header_content_size(self, max_download_size: int) -> DataSize | None:
        if content_length := (
            self._wrapped_value.get("content-length")
            or self._wrapped_value.get("Content-Length")
        ):
            try:
                return DataSize(value=int(content_length.split(";")[0]))
            except Exception:
                return DataSize(value=max_download_size)
        return None

    def get_header_content_type(self) -> DataType | None:
        if content_type := (
            self._wrapped_value.get("content-type")
            or self._wrapped_value.get("Content-Type")
        ):
            return DataType(value=content_type.split(";")[0])
        return None

    @property
    def wrapped_value(self) -> HTTPMessage:
        return self._wrapped_value
