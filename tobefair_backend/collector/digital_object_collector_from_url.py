from tobefair_backend.utils.request_helper import RequestHelper
from tobefair_framework.core.collector.digital_object_collector import (
    DigitalObjectCollector,
)
from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.model.accept_type import AcceptType
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo
from tobefair_framework.model.landing_page import LandingPage
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class DigitalObjectCollectorFromURL(DigitalObjectCollector):

    def _read_digital_object_info(
        self,
        identifier_info: IdentifierInfo,
        metadata_collector: MetadataCollector,
    ) -> DigitalObjectInfo:
        metadata_record: MetadataRecord | None = None
        landing_page = None
        if identifier_info.url:
            if negotiation_result := RequestHelper().negotiate_content(
                identifier_info.url, [AcceptType(mime_types=["text/html"])]
            ):
                landing_page = LandingPage(
                    decoded_html_body=negotiation_result.response,
                    url=identifier_info.url,
                )
                metadata_record = metadata_collector.get_metadata_record(
                    raw_digital_object=negotiation_result.response
                )
        return DigitalObjectInfo(
            identifier_info=identifier_info,
            metadata_record=metadata_record,
            landing_page=landing_page,
        )
