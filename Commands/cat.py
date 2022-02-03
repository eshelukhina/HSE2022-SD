from typing import List

from Executor.file_manager import FileManager
from Executor.path_types import PathTypes


class Cat:
    def __init__(self, args: List[str]):
        self.args = args

    def execute(self):
        for arg in self.args:
            file_manager = FileManager(arg)
            file_manager.get_file_type()
            if file_manager.file_type == PathTypes.file:
                print(file_manager.get_file_content())
            elif file_manager.file_type == PathTypes.directory:
                print('cat: Is a directory')
            else:
                print('cat: No such file or directory')

    def __str__(self):
        return f'CAT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.args == other.args
        return False
