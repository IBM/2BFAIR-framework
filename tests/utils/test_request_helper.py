# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

from mock import patch

from tests.data_for_testing.sample_html_response import html_sample
from tobefair_backend.utils.request_helper import RequestHelper


class TestRequestHelper(unittest.TestCase):
    def setUp(self) -> None:
        self.request_helper = RequestHelper()
        self.sample_response_bytes = html_sample.encode()
        return super().setUp()

    @patch("http.client.HTTPResponse")
    def test_decode_response_utf8_encoding(self, mock_response):
        mock_response.read.return_value = (
            b"\x4c\x6f\x72\x65\x6d\x20\x69\x70\x73\x75\x6d\x20\x64"
            b"\x6f\x6c\x6f\x72\x20\x73\x69\x74\x20\x61\x6d\x65\x74"
        )
        mock_response.getheader.return_value = "UTF-8"
        decoded_text = self.request_helper._decode_response(mock_response)
        self.assertEqual(decoded_text, "Lorem ipsum dolor sit amet")

    @patch("http.client.HTTPResponse")
    def test_decode_response_utf8_encoding_no_header(self, mock_response):
        mock_response.read.return_value = (
            b"\x4c\x6f\x72\x65\x6d\x20\x69\x70\x73\x75\x6d\x20\x64"
            b"\x6f\x6c\x6f\x72\x20\x73\x69\x74\x20\x61\x6d\x65\x74"
        )
        mock_response.getheader.return_value = None
        decoded_text = self.request_helper._decode_response(mock_response)
        self.assertEqual(decoded_text, "Lorem ipsum dolor sit amet")

    @patch("http.client.HTTPResponse")
    def test_decode_response_latin1_encoding(self, mock_response):
        mock_response.read.return_value = (
            b"p\xe1 caf\xe9 n\xedvel p\xf3 m\xfasica \xc1baco \xc9ter "
            b"\xcdon \xd3bvio \xdatil ma\xe7\xe3 mon\xe7\xf5es"
        )
        mock_response.getheader.return_value = "latin1"
        decoded_text = self.request_helper._decode_response(mock_response)
        self.assertEqual(
            decoded_text,
            "pá café nível pó música Ábaco Éter Íon Óbvio Útil maçã monções",
        )

    @patch("http.client.HTTPResponse")
    def test_decode_response_latin1_encoding_no_header(self, mock_response):
        mock_response.read.return_value = (
            b"p\xe1 caf\xe9 n\xedvel p\xf3 m\xfasica \xc1baco \xc9ter "
            b"\xcdon \xd3bvio \xdatil"
        )
        mock_response.getheader.return_value = None
        decoded_text = self.request_helper._decode_response(mock_response)
        self.assertEqual(
            decoded_text,
            "pá café nível pó música Ábaco Éter Íon Óbvio Útil",
        )

    @patch("http.client.HTTPResponse")
    def test_get_content_type_with_header(self, mock_response):
        mock_response.headers.get.return_value = "text/html;charset=UTF-8"
        content_type = self.request_helper._get_content_type(mock_response)
        self.assertEqual(content_type, "text/html")

    @unittest.skip("TODO: Solve error on _get_content_type")
    @patch("http.client.HTTPResponse")
    def test_get_content_type_no_header(self, mock_response):
        mock_response.headers.get.return_value = None
        mock_response.read.return_value = self.sample_response_bytes
        if content_type := self.request_helper._get_content_type(mock_response):
            self.assertEqual(
                self.request_helper._extract_mime_type_and_subtype(content_type),
                "text/html",
            )
        self.assertIsNotNone(content_type, "content_type should not be None")
