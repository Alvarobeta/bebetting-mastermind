import logging
from unittest import TestCase

from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.feedback_services_TBD.compare_patterns import \
    ComparePatterns
from app.mastermind.domain.feedback_services_TBD.tests.pattern_mother import \
    PatternMother

logger = logging.getLogger(__name__)


class UnitTestComparePatterns(TestCase):
    def setUp(self):
        self.compare_patterns = ComparePatterns()
        self.codemaker_pattern = PatternMother.build(
            pattern=[
                GuessColour.BLUE,
                GuessColour.GREEN,
                GuessColour.ORANGE,
                GuessColour.PINK,
            ]
        )

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

        compared_patterns = self.compare_patterns.compare(
            codemaker_pattern=self.codemaker_pattern,
            codebreaker_guess_pattern=codebreaker_guess_pattern,
        )

        logger.debug(f" --------------  compared_patterns={compared_patterns}")

        self.assertEqual(compared_patterns_correct_answer, compared_patterns)

    def test_compare_one_correct_colour_and_position_and_correct_colour_bad_position(
        self,
    ):
        print(f" --------------  self.codemaker_pattern={self.codemaker_pattern}")

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

        compared_patterns = self.compare_patterns.compare(
            codemaker_pattern=self.codemaker_pattern,
            codebreaker_guess_pattern=codebreaker_guess_pattern,
        )

        print(f" --------------  compared_patterns={compared_patterns}")

        self.assertEqual(compared_patterns_correct_answer, compared_patterns)
