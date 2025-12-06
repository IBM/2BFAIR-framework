from typing import ClassVar, List

from pydantic import BaseModel, PrivateAttr

from tobefair_backend.model.resources.data_size import DataSize, DataType


class TypedLink(BaseModel):
    href: str
    rel: str | None = None
    type: DataType | None = None
    profile: str | None = None
    content_size: DataSize | None = None
    measured_variable: List[str] | str | None = None

    _accepted_rel_types: ClassVar[List[str]] = PrivateAttr(
        [
            "meta",
            "alternate meta",
            "metadata",
            "collection",
            "author",
            "describes",
            "item",
            "type",
            "search",
            "alternate",
            "describedby",
            "cite-as",
            "linkset",
            "license",
        ]
    )

    def __eq__(self, value: object) -> bool:
        if isinstance(value, TypedLink):
            return self.href == value.href
        return False

    def __hash__(self) -> int:
        return hash(self.href)

    @classmethod
    def rel_type_is_accepted(cls, typed_link: "TypedLink"):
        return typed_link.rel in cls._accepted_rel_types
