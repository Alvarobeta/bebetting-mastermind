import os
from unittest import TestCase
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import GameRequestMother

from fastapi.testclient import TestClient

from app.mastermind.infrastructure.config import API_V1_STR
from app.mastermind.infrastructure.FastAPI.main import app

import logging

logger = logging.getLogger(__name__)

class FunctionalTestCreateGame(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)

    def make_request(self, json_data):
        return self._client.post(f"{API_V1_STR}/games", json=json_data)

    def test_create_game(self) -> None:
        request_data = GameRequestMother()

        endpoint_response = self.make_request(request_data.build())

        assert endpoint_response.status_code == 200
    
    def test_invalid_create_with_less_than_required_values(self) -> None:
        request_data = GameRequestMother()
        del request_data._code[0]

        endpoint_response = self.make_request(request_data.build())

        self.assertEqual(400, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual(
            "wrong_input_number", json_response["error"]["type"]
        )
        self.assertEqual(
            f"You must input {os.environ['DEFAULT_CODE_LENGTH']} colours.",
            json_response["error"]["message"],
        )