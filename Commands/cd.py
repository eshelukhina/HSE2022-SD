from typing import List, Tuple

import os
from os.path import expanduser

from Executor.context import Context
from Executor.executor import Executor


class Cd:
    """
    Change current directory.
    """

    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args
        self.output = ""

    def __remove_suffix(self, string: str, suffix: str) -> str:
        if string.endswith(suffix):
            return string[:-len(suffix)]
        return string

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Change current directory
        :returns: Status code
        :rtype: int
        """
        if len(self.args) > 1:
            return f'cd: too many arguments', 1
        if not self.args:
            Executor.current_directory = expanduser("~")
            return self.output, 0
        if not self.args[0].startswith(os.path.sep):
            self.args[0] = os.path.sep + self.args[0]
        current_directory = Executor.current_directory + self.__remove_suffix(self.args[0], os.path.sep)
        if not os.path.exists(current_directory):
            if os.path.exists(self.args[0]):
                Executor.current_directory = self.__remove_suffix(self.args[0], os.path.sep)
                return self.output, 0
            return f'cd: no such directory {current_directory}', 2
        Executor.current_directory = current_directory
        return self.output, 0

    def __str__(self):
        return f'CD {self.args}'

    def __eq__(self, other):
        if isinstance(other, Cd):
            return self.args == other.args
        return False
