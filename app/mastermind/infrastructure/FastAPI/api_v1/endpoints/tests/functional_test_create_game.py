from unittest import TestCase

from fastapi.testclient import TestClient

from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.config import API_V1_STR
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import \
    GameRequestMother
from app.mastermind.infrastructure.FastAPI.main import app


class FunctionalTestCreateGame(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)
        self._valid_game = GameRequestMother(
            code=[
                GuessColour.RED,
                GuessColour.GREEN,
                GuessColour.YELLOW,
                GuessColour.ORANGE,
            ]
        )

    def make_request(self, json_data):
        return self._client.post(f"{API_V1_STR}/games", json=json_data)

    def test_create_game(self) -> None:
        request_data = self._valid_game

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
        self.assertEqual("WrongInputException", json_response["error"]["type"])
        self.assertEqual(
            f"You must input {Game.CODE_LENGTH} colours.",
            json_response["error"]["message"],
        )

    def test_invalid_create_with_empty_type_value(self) -> None:
        request_data = GameRequestMother()
        request_data._code[0] = GuessColour.EMPTY

        endpoint_response = self.make_request(request_data.build())

        self.assertEqual(400, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("WrongInputException", json_response["error"]["type"])
        self.assertEqual(
            f"You must input {Game.CODE_LENGTH} colours.",
            json_response["error"]["message"],
        )
