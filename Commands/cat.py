from typing import List

from Executor.context import Context
from Executor.file_manager import FileManager


class Cat:
    def __init__(self, args: List[str]):
        self.args = args

    def execute(self, context: Context):
        for arg in self.args:
            if not FileManager.is_file(arg):
                context.error = 'cat: No such file'
                return
        for arg in self.args:
            context.state += FileManager.get_file_content(arg) + '\n'

    def __str__(self):
        return f'CAT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.args == other.args
        return False
