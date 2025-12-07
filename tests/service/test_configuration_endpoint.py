# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import unittest

from fastapi.testclient import TestClient

from tobefair_backend.service.main import app


class TestConfigurationEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app=app)
        self.route = "/configuration"

    @unittest.skip("This needs refactoring in the use of ConfigurationController.")
    def test_configuration_route(self):
        response = self.client.get(self.route)
        assert response.status_code == 200, "Error on requesting configuration."
