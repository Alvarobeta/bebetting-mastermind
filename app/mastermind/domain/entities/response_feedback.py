
from dataclasses import dataclass
from typing import List


@dataclass
class ResponseFeedback:
    feedback: List[str]
    