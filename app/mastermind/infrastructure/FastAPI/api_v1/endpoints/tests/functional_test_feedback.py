import json
from unittest import TestCase
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import GameRequestMother
from app.mastermind.infrastructure.config import API_V1_STR

from fastapi.testclient import TestClient

from app.mastermind.infrastructure.FastAPI.main import app

import logging

logger = logging.getLogger(__name__)

class FunctionalTestFeedback(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app) 
        self._game_id: int = 1

    def make_request(self, game_id, json_data):
        return self._client.post(f"{API_V1_STR}/{game_id}/feedbacks", json=json_data)


    def test_get_feedback(self) -> None:
        request_data = GameRequestMother(code=["RED", "BLUE", "GREEN", "RED"])        
        
        logger.debug(
            f" ------------------------------------- request_data={request_data.build()}"
        )
        endpoint_response = self.make_request(self._game_id, request_data.build())



        assert endpoint_response.status_code == 200
        assert endpoint_response.json() == ["BLACK", "", "WHITE", ""] 

    #check that the input is 4 (or required)
    #check that the input is correct (strings)