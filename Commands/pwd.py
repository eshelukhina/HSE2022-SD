from typing import List

from optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Pwd:
    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> int:
        """
        Writes current working directory in Context
        :returns: command status code
        :rtype: int
        """
        context.state = Optional.of(FileManager.get_current_directory())
        return 0

    def __str__(self):
        return f'PWD {self.args}'

    def __eq__(self, other):
        if isinstance(other, Pwd):
            return self.args == other.args
        return False
