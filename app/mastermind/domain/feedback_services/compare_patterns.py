import logging
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.guess_colour import GuessColour

logger = logging.getLogger(__name__)


class ComparePatterns:
    def compare(
        self,
        codebreaker_guess_pattern: List[GuessColour],
        codemaker_pattern: List[GuessColour],
    ) -> List[FeedbackColour]:
        feedback = []

        for index, colour in enumerate(codebreaker_guess_pattern):

            logger.debug(
                f" --------------  codebreaker_guess_pattern - index={index}, colur={colour}"
            )
            print(f" --------------  codebreaker_guess_pattern - index={index}, colur={colour}")


            if any(colour == c for c in codemaker_pattern):
                if codebreaker_guess_pattern[index] == codemaker_pattern[index]:

                    print(f" --------------  inside if - codebreaker_guess_pattern[index]={codebreaker_guess_pattern[index]} - codemaker_pattern[index]={codemaker_pattern[index]}")


                    feedback.append("BLACK")

                else:
                    print(f" --------------  inside else - codebreaker_guess_pattern[index]={codebreaker_guess_pattern[index]} - codemaker_pattern[index]={codemaker_pattern[index]}")

                    feedback.append("WHITE")

                codemaker_pattern[index] = GuessColour.EMPTY # avoid erroneous comparisons on repeated colors

            else:
                feedback.append("")

            print(f" -------------- codemaker_pattern iteration:{index}={codemaker_pattern}")
        return feedback
