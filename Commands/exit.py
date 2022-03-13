from typing import List, Tuple

from Executor.context import Context
from Executor.executor import Executor


class Exit:
    """
    Exit the application.
    """

    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args
        self.output = "Shell is terminated\n"

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Terminate the current shell
        :returns: Tuple of command result and status code
        :rtype: Tuple[str, int]
        """
        Executor.is_shell_terminated = True
        return self.output, 0

    def __str__(self):
        return f'EXIT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Exit):
            return self.args == other.args
        return False
