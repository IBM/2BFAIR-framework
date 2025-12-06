from concurrent import futures
from typing import Iterator, List

from tobefair_backend.constants import MAXIMUM_RESPONSE_SIZE
from tobefair_backend.model.resources.data_record import DataRecord
from tobefair_backend.model.resources.typed_link import TypedLink
from tobefair_backend.model.response_header_wrapper import ResponseHeaderWrapper
from tobefair_backend.model.response_wrapper import ResponseWrapper
from tobefair_backend.utils.data_link_collector import DataLinkCollector
from tobefair_backend.utils.request_helper import RequestHelper
from tobefair_backend.utils.tika_content_extractor import TikaContentExtractor
from tobefair_framework.model.digital_object_info import DigitalObjectInfo


class DataCollector:
    """
    Based on F-UJI's DataHarvester. The DataCollector's purpose is to collect all data
    possible from the landing page, via typed links and metadata.
    """

    def retrieve_all_data(
        self, data_links: List[TypedLink], timeout=1
    ) -> Iterator[DataRecord]:
        if len(data_links) < 1:
            return
        with futures.ThreadPoolExecutor(max_workers=len(data_links)) as executor:
            future_data = executor.map(
                self.get_data_record_from_uri, data_links, timeout=timeout
            )
        for data_record in future_data:
            if data_record is not None:
                yield data_record
            continue

    def retrieve_data_from_digital_object(
        self,
        digital_object: DigitalObjectInfo,
    ) -> List[DataRecord]:
        all_links = (
            DataLinkCollector.get_typed_links_from_metadata_record(metadata_record)
            if (metadata_record := digital_object.metadata_record)
            else []
        )
        data_record_iterator = self.retrieve_all_data(all_links)
        data_records = list(data_record_iterator)
        return data_records

    def get_data_record_from_uri(self, typed_link: TypedLink) -> DataRecord | None:
        request_helper = RequestHelper()
        tika_content_extractor: TikaContentExtractor
        if (response := request_helper.make_request(typed_link.href)) and (
            response_wrapper := ResponseWrapper(
                http_response=response, maximum_response_size=MAXIMUM_RESPONSE_SIZE
            )
        ):
            tika_content_extractor = TikaContentExtractor.from_response_wrapper(
                response_wrapper, MAXIMUM_RESPONSE_SIZE
            )
            data_record = self.assemble_data_record(typed_link, response_wrapper)
            if (
                content_size.value > int(0)
                if (content_size := data_record.content_size)
                else False
            ):
                tika_content_types = tika_content_extractor.get_file_content_types()
                data_record.tika_content_types = tika_content_types or []
                data_record.tika_data_content = tika_content_extractor.extract_content()
            return data_record
        return None

    def assemble_data_record(
        self, typed_link: TypedLink, response_wrapper: ResponseWrapper
    ) -> DataRecord:
        wrapped_response_headers: ResponseHeaderWrapper = ResponseHeaderWrapper(
            response_wrapper.wrapped_value.headers
        )
        content_size = response_wrapper.get_response_content_size(
            max_response_size=MAXIMUM_RESPONSE_SIZE
        )
        header_content_size = wrapped_response_headers.get_header_content_size(
            max_download_size=MAXIMUM_RESPONSE_SIZE
        )
        header_content_type = wrapped_response_headers.get_header_content_type()
        return DataRecord(
            link=typed_link,
            content_size=content_size,
            header_content_size=header_content_size,
            header_content_type=header_content_type,
        )
