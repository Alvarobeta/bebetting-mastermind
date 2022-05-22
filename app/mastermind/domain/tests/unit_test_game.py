from unittest import TestCase

from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.tests.pattern_mother import PatternMother


class UnitTestComparePatterns(TestCase):
    def setUp(self):
        self._codemaker_pattern = PatternMother.build(
            pattern=[
                GuessColour.BLUE,
                GuessColour.GREEN,
                GuessColour.ORANGE,
                GuessColour.PINK,
            ]
        )
        self.game = Game(code=self._codemaker_pattern)

    def test_compare_one_correct_colour_and_position(self):
        codebreaker_guess_pattern = PatternMother.build(
            pattern=[
                GuessColour.BLUE,
                GuessColour.RED,
                GuessColour.YELLOW,
                GuessColour.YELLOW,
            ]
        )
        compared_patterns_correct_answer = [
            FeedbackColour.BLACK,
            FeedbackColour.EMPTY,
            FeedbackColour.EMPTY,
            FeedbackColour.EMPTY,
        ]

        compared_patterns = self.game.compute_last_feedback(
            guess=codebreaker_guess_pattern
        )

        self.assertEqual(compared_patterns_correct_answer, compared_patterns)

    def test_compare_one_correct_colour_and_position_and_correct_colour_bad_position(
        self,
    ):

        codebreaker_guess_pattern = PatternMother.build(
            pattern=[
                GuessColour.BLUE,
                GuessColour.RED,
                GuessColour.PINK,
                GuessColour.YELLOW,
            ]
        )
        compared_patterns_correct_answer = [
            FeedbackColour.BLACK,
            FeedbackColour.EMPTY,
            FeedbackColour.WHITE,
            FeedbackColour.EMPTY,
        ]

        compared_patterns = self.game.compute_last_feedback(
            guess=codebreaker_guess_pattern
        )

        self.assertEqual(compared_patterns_correct_answer, compared_patterns)
