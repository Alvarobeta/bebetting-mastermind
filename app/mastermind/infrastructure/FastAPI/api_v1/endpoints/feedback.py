from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.mastermind.application.make_a_guess_command import MakeAGuessCommand
from app.mastermind.application.make_a_guess_handler import MakeAGuessHandler
from app.mastermind.domain.entities.guessing_pattern import GuessingPattern

import logging

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/{game_id}/feedbacks", response_model=List[str])
async def get_feedback(game_id: int, guess_attempt_pattern: GuessingPattern):
    
    logger.debug(
        f" ------------------------------------- gameID={game_id}, guessingPattern={guess_attempt_pattern}"
    )

    handler = MakeAGuessHandler()

    return handler(
        MakeAGuessCommand(
            game_id=game_id,
            pattern=guess_attempt_pattern,
        )
    )