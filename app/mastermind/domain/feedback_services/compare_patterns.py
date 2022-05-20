import logging
from typing import List
from app.mastermind.domain.entities.feedback_colour import FeedbackColour

from app.mastermind.domain.entities.guess_colour import GuessColour

logger = logging.getLogger(__name__)

class ComparePatterns:
    def compare(self,
        codebreaker_guess_pattern: List[GuessColour], 
        codemaker_pattern: List[GuessColour]
    ) -> List[FeedbackColour]:
        feedback = []

        for index, colour in enumerate(codebreaker_guess_pattern):
            logger.debug(
                f" --------------  codebreaker_guess_pattern - index={index}, colur={colour}"
            )
            #TODO casos de colores repetidos!

            if any(colour == c for c in codemaker_pattern):
                if codebreaker_guess_pattern[index] == codemaker_pattern[index]:
                    feedback.append("BLACK")
                    
                else: 
                    feedback.append("WHITE")
                    
                codemaker_pattern.remove(colour) #avoid erroneous comparisons on repeated colors
            else:
                feedback.append("")

        return feedback