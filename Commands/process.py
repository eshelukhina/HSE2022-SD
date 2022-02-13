import subprocess

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

    def execute(self, context: Context) -> int:
        """
        Execute external program.
        :returns: Status code
        :rtype: int
        """
        if len(self.args) > 0:
            args = self.args
        else:
            args = [] if context.state.is_empty() else [context.state.get()]

        command = ' '.join([self.name] + args)
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, env=context.env.get_vars()
        )

        if result.returncode != 0:
            context.state = Optional.of(result.stderr)
            return result.returncode
        context.state = Optional.of(result.stdout)
        return result.returncode

    def __str__(self):
        return f'Process name: {self.name}, args: {self.args}'

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.name == other.name and self.args == other.args
        return False
