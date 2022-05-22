from typing import List
from unittest import TestCase

from fastapi.testclient import TestClient

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.config import API_V1_STR
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import \
    GameRequestMother
from app.mastermind.infrastructure.FastAPI.main import app


class FunctionalTestFeedback(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)
        self._valid_request = GameRequestMother(
            code=[
                GuessColour.RED,
                GuessColour.BLUE,
                GuessColour.GREEN,
                GuessColour.YELLOW,
            ]
        )
        self._game = self.create_gamemaker_request(self._valid_request.build())
        self._game_response = self._game.json()


        self._won_string_message: str = "YOU WON!!!!!!!!!"
        self._won_feedback_answer: List[str] = ["BLACK", "BLACK", "BLACK", "BLACK"]
        self.wrong_guess_string_message: str = "Keep trying!"

    def create_gamemaker_request(self, json_data):
        return self._client.post(f"{API_V1_STR}/games", json=json_data)

    def make_request(self, json_data: dict):
        return self._client.post(
            f"{API_V1_STR}/{self._game_response['id']}/feedbacks", json=json_data
        )

    def test_get_feedback(self) -> None:
        self._game.attempts = "[]"

        request_data = GameRequestMother(
            code=[
                GuessColour.RED,
                GuessColour.ORANGE,
                GuessColour.YELLOW,
                GuessColour.ORANGE,
            ]
        )

        endpoint_response = self.make_request(json_data=request_data.build())
        json_response = endpoint_response.json()

        assert endpoint_response.status_code == 200

        self.assertTrue({"feedback", "message"}.issubset(json_response))

        self.assertEqual(self.wrong_guess_string_message, json_response["message"])
        self.assertEqual(["BLACK", "", "WHITE", ""], json_response["feedback"])

    def test_invalid_request_less_than_required_values(self) -> None:
        request_data = GameRequestMother()
        del request_data._code[0]

        endpoint_response = self.make_request(request_data.build())

        self.assertEqual(400, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("WrongInputException", json_response["error"]["type"])
        self.assertEqual(
            f"Invalid guessing length",
            json_response["error"]["message"],
        )

    def test_invalid_request_missing_colour(self) -> None:
        request_data = GameRequestMother()
        request_data._code[0] = GuessColour.EMPTY

        endpoint_response = self.make_request(json_data=request_data.build())

        self.assertEqual(400, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("WrongInputException", json_response["error"]["type"])
        self.assertEqual(
            f"Empty colour",
            json_response["error"]["message"],
        )

    def test_win_game(self) -> None:
        request_data = GameRequestMother(
            code=[
                GuessColour.RED,
                GuessColour.BLUE,
                GuessColour.GREEN,
                GuessColour.YELLOW,
            ]
        )

        endpoint_response = self.make_request(json_data=request_data.build())

        json_response = endpoint_response.json()

        assert endpoint_response.status_code == 400

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("GAME_WON_STATUS", json_response["error"]["type"])
        self.assertEqual(
            f"Congratulations, you won the game!",
            json_response["error"]["message"],
        )
