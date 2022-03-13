from typing import Tuple
from optional import Optional

from Executor.context import Context


class Eq:
    """
    Update value of environment variable.
    """

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.output = None

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Updates value of environment variable
        :returns: Status code
        :rtype: int
        """
        context.env.add_var(name=self.dest, value=self.src)
        return self.output, 0

    def __str__(self):
        return f'{self.dest} EQ {self.src}'

    def __eq__(self, other):
        if isinstance(other, Eq):
            return self.src == other.src and self.dest == other.dest
        return False
