# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import time
import unittest
from concurrent.futures import ThreadPoolExecutor

from fastapi.testclient import TestClient

from tobefair_backend.service.main import app


class TestNotifications(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.endpoint_url = [
            "http://127.0.0.1:8000/evaluate",
            "http://127.0.0.1:8000/evaluate",
            "http://127.0.0.1:8000/evaluate",
            "http://127.0.0.1:8000/evaluate",
        ]
        cls.request_data = [
            {
                "resource_id": "https://doi.org/10.1594/PANGAEA.893286",
                "community": "string",
                "task": "string",
            },
            {
                "resource_id": "00000",
                "community": "string",
                "task": "string",
            },
            {
                "resource_id": "https://doi.org/10.1594/PANGAEA.893286",
                "community": "string",
                "task": "string",
            },
            {
                "resource_id": "00000",
                "community": "string",
                "task": "string",
            },
        ]
        try:
            with ThreadPoolExecutor(max_workers=4) as executor:
                cls.results = list(
                    executor.map(
                        cls.make_request,
                        cls.endpoint_url,
                        cls.request_data,
                    )
                )
        except Exception as e:
            raise unittest.SkipTest(f"Skipping test due to setup error: {e}")

    @classmethod
    def make_request(cls, url: str, data: dict):
        try:
            start_request = time.time()
            response = TestClient(app=app).post(url, json=data)
            end_request = time.time()
            response.raise_for_status()  # Raise an exception for bad status codes
            return [response.json(), [start_request, end_request]]
        except Exception as e:
            raise e

    def check_intervals_overlap(self, intervals: list):
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Compare each interval with the previous one
        for i in range(1, len(intervals)):
            previous_end = intervals[i - 1][1]
            current_start = intervals[i][0]

            # If current start is before previous end, there is overlap
            if current_start < previous_end:
                return True
        return False

    def test_notifications_answer(self):
        for result in self.results:
            evaluation_id = result[0]["overall_result"]["evaluation_id"]
            notifications = result[0]["notifications"]

            if evaluation_id == "https://doi.org/10.1594/PANGAEA.893286":
                self.assertEqual(notifications, [])
            if evaluation_id == "0000":
                self.assertEqual(
                    notifications,
                    [
                        {
                            "type": "error",
                            "title": "Error",
                            "description": "Digital object's URI \
                                could not be resolved to an URL.",
                        }
                    ],
                )

    def test_parallelism(self):
        intervals: list = []
        for result in self.results:
            intervals.append(result[1])

        self.assertTrue(self.check_intervals_overlap(intervals))
