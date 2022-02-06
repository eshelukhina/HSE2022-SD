from typing import List

from optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Pwd:
    def __init__(self, args: List[str]):
        self.args = args

    def execute(self, context: Context):
        """
        Get current working directory
        """
        context.state = Optional.of(FileManager.get_current_directory())

    def __str__(self):
        return f'PWD {self.args}'

    def __eq__(self, other):
        if isinstance(other, Pwd):
            return self.args == other.args
        return False
