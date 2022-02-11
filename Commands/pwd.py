from typing import List, Tuple

from optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Pwd:
    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Writes current working directory in Context
        :returns: command status code
        :rtype: int
        """
        return FileManager.get_current_directory() + '\n', 0

    def __str__(self):
        return f'PWD {self.args}'

    def __eq__(self, other):
        if isinstance(other, Pwd):
            return self.args == other.args
        return False
