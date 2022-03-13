import os
import subprocess
from typing import Tuple

from Executor.context import Context


class Process:
    """
    The process command allows you to spawn new processes, connect to their input/output/error pipes,
    and obtain their return codes.
    """

    def __init__(self, *, name, args):
        self.name = name
        self.args = args

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Execute external program.
        :returns: Tuple of command result and status code
        :rtype: Tuple[str, int]
        """
        command = ' '.join([self.name] + self.args)
        env = os.environ.copy()
        env.update(context.env.get_vars())
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, env=env
        )
        if result.returncode != 0:
            return result.stderr, result.returncode

        return result.stdout if result.stderr == '' else result.stdout + '\n' + result.stderr, result.returncode

    def __str__(self):
        return f'Process name: {self.name}, args: {self.args}'

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.name == other.name and self.args == other.args
        return False
