from unittest import TestCase

from app.mastermind.domain.app_service_name.compare_patterns import ComparePatterns
from app.mastermind.domain.app_service_name.tests.pattern_mother import PatternMother
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.entities.feedback_colour import FeedbackColour

class UnitTestComparePatterns(TestCase):
    def setUp(self):
        self.compare_patterns = ComparePatterns()

    def test_compare_one_correct_colour_and_position(self):
        codemaker_pattern = PatternMother.build(
            pattern=[
                GuessColour.BLUE, 
                GuessColour.GREEN, 
                GuessColour.ORANGE, 
                GuessColour.PINK]
        )
        codebreaker_guess_pattern = PatternMother.build(
            pattern=[
                GuessColour.BLUE, 
                GuessColour.RED, 
                GuessColour.YELLOW, 
                GuessColour.YELLOW]
        )
        compared_patterns_correct_answer = [
            FeedbackColour.BLACK, 
            FeedbackColour.EMPTY, 
            FeedbackColour.EMPTY, 
            FeedbackColour.EMPTY
        ]

        compared_patterns = self.compare_patterns.compare(codemaker_pattern=codemaker_pattern, codebreaker_guess_pattern=codebreaker_guess_pattern)

        self.assertEqual(compared_patterns_correct_answer, compared_patterns)