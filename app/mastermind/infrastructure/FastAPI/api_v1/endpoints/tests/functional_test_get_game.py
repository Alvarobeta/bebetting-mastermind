# import json
# from unittest import TestCase, mock
# from unittest.mock import create_autospec

# from urllib import request
# from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.tests.game_request_mother import GameRequestMother

# from fastapi.testclient import TestClient

# from app.mastermind.infrastructure.config import API_V1_STR
# from app.mastermind.infrastructure.FastAPI.main import app
# from models import Game
# from app.mastermind.infrastructure.FastAPI.api_v1.endpoints.get_game import get_game

# import logging

# logger = logging.getLogger(__name__)

# # # PATH = 'app.models'

# # @mock.patch(Game)
# class FunctionalTestGetGame(TestCase):
#     def setUp(self):
#         self._client: TestClient = TestClient(app)
#         self.code_id = mock.Mock()

#     def make_request(self, code_id):
#         return self._client.get(f"{API_V1_STR}/game/{code_id}")

#     @mock.patch("app.mastermind.infrastructure.FastAPI.api_v1.endpoints.get_game")
#     def test_get_game(self, game) -> None:
#         self.assertFalse(game.called)

#         # request_data = GameRequestMother()
#         # mock_game = create_autospec(Game, spec_set=True)
#         # mock_game = game.objects.get.return_value

#         # game.filter.return_value = mock_game

#         # logger.debug(
#         #     f" ------------------------------------- test_get_game. game={mock_game}"
#         # )

#         # game.filter.assert_called_once()
#         endpoint_response = self.make_request(self.code_id)
#         self.assertTrue(game.called)
#         # self.assertEqual(200, endpoint_response.status_code)

#         # self.assertEqual(endpoint_response, mock_game.return_value)

        