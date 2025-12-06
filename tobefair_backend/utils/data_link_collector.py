from typing import Callable, ClassVar, List, cast
from urllib.parse import ParseResult, ParseResultBytes, urljoin, urlparse

from lxml import html
from pydantic import BaseModel, PrivateAttr
from pydantic_core import ValidationError

from tobefair_backend.collector.metadata_collector_schemaorg_jsonld import (
    MetadataCollectorSchemaOrgJsonLD,
)
from tobefair_backend.model.resources.data_size import DataType
from tobefair_backend.model.resources.typed_link import TypedLink
from tobefair_backend.utils.list_utils import remove_duplicates
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


def cache_links(typed_link_extractor: Callable[..., List[TypedLink]]):
    def wrapper(*args, **kwargs):
        returned_links = typed_link_extractor(*args, *kwargs)
        DataLinkCollector._all_links += returned_links
        DataLinkCollector._all_links = remove_duplicates(DataLinkCollector._all_links)
        return returned_links

    return wrapper


class DataLinkCollector(BaseModel):

    _all_links: ClassVar[List[TypedLink]] = PrivateAttr([])

    @classmethod
    def get_all_links(cls) -> List[TypedLink]:
        return remove_duplicates(cls._all_links)

    @classmethod
    def get_typed_links_from_body(
        cls, landing_html: str, landing_url
    ) -> List[TypedLink]:
        typed_links: List = []
        links: list = []
        try:
            dom = html.fromstring(landing_html.encode("utf8"))
            links = cast(list, dom.xpath("/*/head/link"))
        except Exception:
            return []
        for link in links:
            href = link.attrib.get("href")
            rel = link.attrib.get("rel")
            type = link.attrib.get("type")
            profile = link.attrib.get("format")
            type = str(type).strip()
            linkparts: ParseResult | ParseResultBytes = urlparse(href)
            if linkparts.scheme == "":
                href = urljoin(landing_url, href)
            if (path := str(linkparts.path)) and path.endswith(".xml"):
                if type not in ["application/xml", "text/xml"] and not type.endswith(
                    "+xml"
                ):
                    type += "+xml"
            typed_link: TypedLink
            try:
                typed_link = TypedLink(
                    href=href,
                    rel=rel,
                    type=DataType(value=type),
                    profile=profile,
                )
            except ValidationError:
                continue
            if TypedLink.rel_type_is_accepted(typed_link):
                typed_links.append(typed_link)
        return typed_links

    @classmethod
    def get_typed_links_from_metadata_record(
        cls, metadata_record: MetadataRecord
    ) -> List[TypedLink]:
        return MetadataCollectorSchemaOrgJsonLD.get_content_links(
            metadata_record.raw_value
        )

    @classmethod
    def get_typed_links_from_digital_object(
        cls, digital_object: DigitalObjectInfo
    ) -> List[TypedLink]:
        links: List[TypedLink] = []
        if landing_page := digital_object.landing_page:
            links += cls.get_typed_links_from_body(
                landing_html=landing_page.decoded_html_body,
                landing_url=landing_page.url,
            )
        if metadata_record := digital_object.metadata_record:
            links += cls.get_typed_links_from_metadata_record(
                metadata_record=metadata_record
            )
        return links
