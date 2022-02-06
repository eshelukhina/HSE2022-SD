from typing import List

from optional import Optional

from Executor.context import Context


class Echo:
    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context):
        """
        Output command arguments
        """
        context.state = Optional.of(" ".join(self.args))

    def __str__(self):
        return f'ECHO {self.args}'

    def __eq__(self, other):
        if isinstance(other, Echo):
            return self.args == other.args
        return False
