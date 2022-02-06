from typing import List

from optional import Optional

from Executor.context import Context
from Executor.executor import Executor


class Exit:
    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args
        self.output = "Shell is terminated"

    def execute(self, context: Context) -> int:
        """
        Terminate the current shell
        Returns command status code
        :returns int
        """
        Executor.shell_terminated = True
        context.state = Optional.of(self.output)
        return 0

    def __str__(self):
        return f'EXIT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Exit):
            return self.args == other.args
        return False
