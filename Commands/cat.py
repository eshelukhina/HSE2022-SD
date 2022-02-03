from typing import List


class Cat:
    def __init__(self, args: List[str]):
        self.args = args

    def execute(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.args == other.args
        return False
