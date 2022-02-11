from typing import Tuple

from Executor.context import Context
from Executor.file_manager import FileManager


class Cat:
    """
    Get file contents.
    """

    def __init__(self, args):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Check that arguments are paths to existing files.
        Retrieve the contents of these files and write it to the Context
        :returns: Tuple of command result and status code
        :rtype: int
        """
        for arg in self.args:
            if not FileManager.is_file(arg):
                return f'cat: no such file {arg}\n', 2
        result = ''
        for arg in self.args:
            result += FileManager.get_file_content(arg)
        return result, 0

    def __str__(self):
        return f'CAT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.args == other.args
        return False
