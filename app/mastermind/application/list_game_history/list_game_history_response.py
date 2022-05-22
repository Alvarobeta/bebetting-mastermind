from dataclasses import dataclass
from typing import List


@dataclass
class ListGameHistoryResponse:
    history: List[List[str]]
