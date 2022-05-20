import json
from unittest import TestCase
from urllib import request
from app.mastermind.domain.entities.guess_colour import GuessColour
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

    def make_request(self, json_data:dict, game_id: int = 1):
        return self._client.post(f"{API_V1_STR}/{game_id}/feedbacks", json=json_data)


    def test_get_feedback(self) -> None:
        request_data = GameRequestMother(
            code=[GuessColour.RED, GuessColour.BLUE, GuessColour.GREEN, GuessColour.RED])        
        
        logger.debug(
            f" -------------- request_data={request_data.build()}"
        )

        endpoint_response = self.make_request(json_data=request_data.build())

        assert endpoint_response.status_code == 200
        assert endpoint_response.json() == ["BLACK", "", "WHITE", ""] 

    def test_invalid_request_less_than_required_values(self) -> None:
        request_data = GameRequestMother()
        del request_data._code[0]

        endpoint_response = self.make_request(json_data=request_data.build())

        assert endpoint_response.status_code == 200
        # assert endpoint_response.json() == ["BLACK", "", "WHITE", ""] 

    # def test_invalid_request_missing_first_colour(self) -> None:
    #     request_data = GameRequestMother()
    #     request_data[0] = ""
        
    #     endpoint_response = self.make_request(json_data=request_data.build())

    #     self.assertEqual(422, endpoint_response.status_code)

    #     json_response = endpoint_response.json()

    #     self.assertTrue({"error"}.issubset(json_response))
    #     self.assertTrue({"type", "message"}.issubset(json_response["error"]))
    #     self.assertEqual("invalid_request", json_response["error"]["type"])
    #     self.assertIn("On body.code.0, value is not a valid enumeration member; permitted: 'RED', 'YELLOW', 'ORANGE', 'BLUE', 'PINK', 'GREEN'", json_response["error"]["message"])
    
    # def test_invalid_request_missing_fourth_colour(self) -> None:
    #     request_data = GameRequestMother(code=["RED", "BLUE", "GREEN", ""]) 

    #     endpoint_response = self.make_request(json_data=request_data.build())

    #     self.assertEqual(422, endpoint_response.status_code)

    #     json_response = endpoint_response.json()

    #     self.assertTrue({"error"}.issubset(json_response))
    #     self.assertTrue({"type", "message"}.issubset(json_response["error"]))
    #     self.assertEqual("invalid_request", json_response["error"]["type"])
    #     self.assertIn("On body.code.3, value is not a valid enumeration member; permitted: 'RED', 'YELLOW', 'ORANGE', 'BLUE', 'PINK', 'GREEN'", json_response["error"]["message"])

    # def test_invalid_request_wrong_value_type(self) -> None:
    #     request_data = {["RED", 69, "GREEN", ""]}

    #     endpoint_response = self.make_request(json_data=request_data)

    #     self.assertEqual(422, endpoint_response.status_code)

    #     json_response = endpoint_response.json()

    #     self.assertTrue({"error"}.issubset(json_response))
    #     self.assertTrue({"type", "message"}.issubset(json_response["error"]))
    #     self.assertEqual("invalid_request", json_response["error"]["type"])
    #     self.assertIn("On body.code.1, value is not a valid enumeration member; permitted: 'RED', 'YELLOW', 'ORANGE', 'BLUE', 'PINK', 'GREEN'", json_response["error"]["message"])

    #check that the input is correct (strings)
    #check that has 4 values on input