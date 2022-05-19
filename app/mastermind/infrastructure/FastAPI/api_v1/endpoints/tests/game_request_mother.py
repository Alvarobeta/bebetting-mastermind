import random
from typing import List

class GameRequestMother:
    def __init__(self, code: List[str] = None):
        self._code = code or self._generate_code()

    @staticmethod
    def _generate_code() -> List[str]:
        code = []
        default_code_length = 4
        possible_colours = ["RED", "YELLOW", "ORANGE", "BLUE", "PINK", "GREEN"]

        for i in range(default_code_length):
            code.append(random.choice(possible_colours))
        
        return code

    def build(self
        # code: List[str] = [
        #     random.choice(["soldier", "mech"]),,,,]
        # coordinate_x: int = random.randint(0, 100),
        # coordinate_y: int = random.randint(0, 100),
        # enemies_type: str = random.choice(["soldier", "mech"]),
        # enemies_number: int = random.randint(0, 100),
        # allies: int = random.randint(0, 100),
    ) -> dict:
        return {"code": self._code}
