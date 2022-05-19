from unittest import TestCase

from fastapi.testclient import TestClient

from app.mastermind.infrastructure.config import API_V1_STR
from app.mastermind.infrastructure.FastAPI.main import app


class FunctionalTestRadar(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)

    def make_request(self):
        return self._client.get(f"{API_V1_STR}/status")

    def test_status_endpoint(self) -> None:
        endpoint_response = self.make_request()

        self.assertEqual(200, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertEqual("Hello World", json_response["message"])
