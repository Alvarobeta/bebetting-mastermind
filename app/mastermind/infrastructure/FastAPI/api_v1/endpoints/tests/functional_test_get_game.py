from unittest import TestCase

from fastapi.testclient import TestClient

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.config import API_V1_STR
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import \
    GameRequestMother
from app.mastermind.infrastructure.FastAPI.main import app


class FunctionalTestGetGame(TestCase):
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

    def create_gamemaker_request(self, json_data):
        return self._client.post(f"{API_V1_STR}/games", json=json_data)

    def make_request(self, code_id):
        return self._client.get(f"{API_V1_STR}/game/{code_id}")

    def test_get_game(self) -> None:

        game = self.create_gamemaker_request(self._valid_request.build())
        game_response = game.json()

        endpoint_response = self.make_request(code_id=game_response["id"])
        json_response = endpoint_response.json()

        assert endpoint_response.status_code == 200

        self.assertTrue({"attempts"}.issubset(json_response))
        self.assertTrue({"feedbacks"}.issubset(json_response))
        self.assertTrue({"code"}.issubset(json_response))
        self.assertTrue({"status"}.issubset(json_response))
        self.assertTrue({"id"}.issubset(json_response))
        self.assertEqual(game_response["id"], json_response["id"])
        self.assertEqual("[]", json_response["attempts"])
        self.assertEqual("[]", json_response["feedbacks"])
        self.assertEqual(["RED", "BLUE", "GREEN", "YELLOW"], json_response["code"])
        self.assertEqual("Playing", json_response["status"])
