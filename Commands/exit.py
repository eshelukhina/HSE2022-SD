from typing import List, Tuple

from optional import Optional

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
        self.output = ""

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Terminate the current shell if executed as a single command or at the end of a pipe
        :returns: Status code
        :rtype: int
        """
        Executor.is_shell_terminated = True
        # context.state = Optional.of(self.output)
        return self.output, 0

    def __str__(self):
        return f'EXIT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Exit):
            return self.args == other.args
        return False
