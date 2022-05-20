import os
import logging

from unittest import TestCase, mock
from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.response_feedback import ResponseFeedback
from fastapi.testclient import TestClient

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.config import API_V1_STR
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import \
    GameRequestMother
from app.mastermind.infrastructure.FastAPI.main import app

logger = logging.getLogger(__name__)


class FunctionalTestFeedback(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)
        self._game_id: int = 1
        self._valid_request = GameRequestMother(
            code=[GuessColour.RED, GuessColour.BLUE, GuessColour.GREEN, GuessColour.YELLOW]
        )

    def make_request(self, json_data: dict, game_id: int = 1):
        return self._client.post(f"{API_V1_STR}/{game_id}/feedbacks", json=json_data)

    def test_get_feedback(self) -> None:
        request_data = GameRequestMother(
            code=[GuessColour.RED, GuessColour.BLUE, GuessColour.GREEN, GuessColour.RED]
        )

        expected_feedback_response = {
            'feedback':["BLACK", "", "WHITE", ""],
            'msg':"Keep trying!"
        }

        # logger.debug(f" -------------- request_data={request_data.build()}")

        endpoint_response = self.make_request(json_data=request_data.build())

        assert endpoint_response.status_code == 200
        assert endpoint_response.json() == expected_feedback_response

    def test_invalid_request_less_than_required_values(self) -> None:
        request_data = GameRequestMother()
        del request_data._code[0]

        endpoint_response = self.make_request(request_data.build())

        self.assertEqual(400, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("wrong_input_number", json_response["error"]["type"])
        self.assertEqual(
            f"You must input {os.environ['DEFAULT_CODE_LENGTH']} valid colours.",
            json_response["error"]["message"],
        )
        # assert endpoint_response.json() == ["BLACK", "", "WHITE", ""]

    def test_invalid_request_missing_colour(self) -> None:
        request_data = GameRequestMother()
        request_data._code[0] = GuessColour.EMPTY

        endpoint_response = self.make_request(json_data=request_data.build())

        self.assertEqual(400, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("wrong_input_number", json_response["error"]["type"])
        self.assertEqual(
            f"You must input {os.environ['DEFAULT_CODE_LENGTH']} valid colours.",
            json_response["error"]["message"],
        )

    def test_win_game(self) -> None:
        request_data = GameRequestMother(
            code=[GuessColour.RED, GuessColour.GREEN, GuessColour.YELLOW, GuessColour.ORANGE]
        )
        request_endpoint_expected_response ={
            'feedback':["BLACK", "BLACK", "BLACK", "BLACK"],
            'msg':"YOU WON!!!!!!!!!"
        }

        endpoint_response = self.make_request(json_data=request_data.build())

        assert endpoint_response.status_code == 200
        assert endpoint_response.json() == request_endpoint_expected_response

    # def test_get_feedback_2(self):
    #     with mock.patch(
    #         'mastermind.domain.entities.Game'
    #     ) as response_game:
        