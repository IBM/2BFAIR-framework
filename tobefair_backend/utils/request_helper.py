import http.client
import http.cookiejar
import ssl
import urllib
import urllib.request
from http.client import HTTPResponse
from mimetypes import guess_type
from typing import List, NamedTuple
from urllib import request

import tika

tika.initVM()  # noqa: E402
from bs4.dammit import UnicodeDammit  # noqa: E402
from mimeparse import parse_mime_type  # noqa: E402
from tika import parser  # noqa: E402

from tobefair_framework.model.accept_type import AcceptType  # noqa: E402

NegotiationResult = NamedTuple(
    "NegotiationResult", [("content_type", str | None), ("response", str)]
)


class RequestHelper:

    def __init__(self):
        pass

    def _extract_mime_type_and_subtype(self, mime_type: str) -> str:
        parsed_content_type = parse_mime_type(mime_type)
        return parsed_content_type[0] + "/" + parsed_content_type[1]

    def _make_request_header(self, accepted_types: List[AcceptType]):
        header = {}
        accept_header_value = ""
        for accepted_type in accepted_types:
            accept_header_value += accepted_type.make_accept_header() + ", "
        header["Accept"] = accept_header_value[:-2]
        return header

    def _generate_request(
        self, url: str, accepted_types: List[AcceptType]
    ) -> urllib.request.Request:
        request_headers = self._make_request_header(accepted_types)
        request = urllib.request.Request(url, headers=request_headers)
        return request

    def make_request(
        self,
        url: str,
        auth_token: str | None = None,
        auth_token_type: str = "",
        timeout=1,
    ) -> HTTPResponse | None:
        header = {"Accept": "*/*", "User-Agent": "F-UJI"}
        if auth_token:
            header["Authorization"] = auth_token_type + " " + auth_token
        url = url
        try:
            req = request.Request(url, headers=header)
            response = request.urlopen(req, timeout=timeout)
        except Exception:
            return None
        return response

    def _make_request_opener_director(self) -> urllib.request.OpenerDirector:
        cookiejar = http.cookiejar.MozillaCookieJar()
        context = ssl._create_unverified_context()
        context.set_ciphers("DEFAULT@SECLEVEL=1")
        redirect_handler = urllib.request.HTTPRedirectHandler()
        request_opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cookiejar),
            urllib.request.HTTPSHandler(context=context),
            urllib.request.HTTPHandler(),
            redirect_handler,
        )
        return request_opener

    def _decode_response(self, response: http.client.HTTPResponse) -> str:
        response_body = response.read()
        if charset := response.getheader("charset"):
            return response_body.decode(charset)
        if unicode_markup := UnicodeDammit(response_body).unicode_markup:
            return unicode_markup
        else:
            raise Exception("Error on decoding response.")

    def _get_content_type(self, response: http.client.HTTPResponse) -> str | None:
        if content_type := (
            response.headers.get("content-type") or response.headers.get("Content-type")
        ):
            return self._extract_mime_type_and_subtype(content_type)
        if content_type := guess_type(response.url, strict=False)[0]:
            return self._extract_mime_type_and_subtype(content_type)
        try:
            if (parsed_response_content := parser.from_buffer(response.read())) and (
                content_type := parsed_response_content.get("metadata").get(
                    "Content-Type"
                )
            ):
                return self._extract_mime_type_and_subtype(content_type)
        except Exception:
            return None
        return None

    def negotiate_content(
        self, url: str, accepted_types: List[AcceptType]
    ) -> NegotiationResult:
        request = self._generate_request(url=url, accepted_types=accepted_types)
        request_opener_director = self._make_request_opener_director()
        urllib.request.install_opener(request_opener_director)
        try:
            response = request_opener_director.open(request)
        except urllib.error.HTTPError as http_error:
            # TODO: implement retry_connection()
            response = None
            raise http_error
        except Exception as exception:
            raise exception
        decoded_response = self._decode_response(response=response)
        content_type = self._get_content_type(response=response)
        return NegotiationResult(content_type=content_type, response=decoded_response)
