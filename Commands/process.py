import os

import subprocess
from typing import Tuple

from optional import Optional

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
        :returns: Status code
        :rtype: int
        """
        args = self.args
        if context.state:
            inp = context.state.get()
        else:
            inp = None

        command = ' '.join(
            ["\"" + self.name + "\""] +
            ["\"" + arg + "\"" if ' ' in arg else arg for arg in args]
        )
        env = os.environ.copy()
        env.update(context.env.get_vars())
        if os.name == 'nt':
            env.pop('')
        result = subprocess.run(
            command, shell=True, input=inp, text=True, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        return result.stdout, result.returncode

    def __str__(self):
        return f'Process name: {self.name}, args: {self.args}'

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.name == other.name and self.args == other.args
        return False
