import json
from unittest import TestCase
from urllib import request
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