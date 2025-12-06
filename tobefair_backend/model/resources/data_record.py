from typing import List

from pydantic import BaseModel, Field

from tobefair_backend.model.resources.data_size import DataSize, DataType
from tobefair_backend.model.resources.typed_link import TypedLink


class DataRecord(BaseModel):
    link: TypedLink | None = None
    content_size: DataSize | None = None
    header_content_size: DataSize | None = None
    tika_content_types: List[DataType] = []
    header_content_type: DataType | None = None
    measured_variables: List[str] | None = None
    schema_: str | None = Field(
        default=None,
        alias="schema",
    )
    tika_data_content: str | None = None

    @property
    def claimed_size(self) -> DataSize | None:
        return link.content_size if (link := self.link) else None

    @property
    def claimed_type(self) -> DataType | None:
        return link.type if (link := self.link) else None

    @property
    def truncated(self) -> bool:
        return (
            self.header_content_size is not None
            and self.content_size is not None
            and self.content_size < self.header_content_size
        )

    @property
    def data_types(self) -> List[DataType]:
        return (self.tika_content_types) + (
            [header_content_type]
            if (header_content_type := self.header_content_type)
            else []
        )
