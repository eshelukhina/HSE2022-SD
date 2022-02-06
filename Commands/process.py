import subprocess

from optional import Optional

from Executor.context import Context


class Process:
    def __init__(self, *, name, args):
        self.name = name
        self.args = args

    def execute(self, context: Context) -> int:
        """
        Execute external program.
        Save result to the Context, returns process status code
        :returns int
        """
        command = ' '.join([self.name] + self.args)
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, env=context.env
        )
        if result.returncode != 0:
            context.error = Optional.of(result.stderr)
        else:
            context.state = Optional.of(result.stdout)
        return result.returncode

    def __str__(self):
        return f'Process name: {self.name}, args: {self.args}'

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.name == other.name and self.args == other.args
        return False
