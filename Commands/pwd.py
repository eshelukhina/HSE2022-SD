from typing import List, Tuple

from optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Pwd:
    """
    Return the current directory.
    """

    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> int:
        """
        Return working directory
        :returns: Tuple of command result and status code
        :rtype: int
        """
        if len(self.args) > 0 or not context.state.is_empty():
            context.state = Optional.of("pwd: too many arguments")
            return 1
        context.state = Optional.of(FileManager.get_current_directory())
        return 0

    def __str__(self):
        return f'PWD {self.args}'

    def __eq__(self, other):
        if isinstance(other, Pwd):
            return self.args == other.args
        return False
