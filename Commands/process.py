import subprocess

from optional.optional import Optional

from Executor.context import Context


class Process:
    def __init__(self, *, name, args):
        self.name = name
        self.args = args

    def execute(self, context: Context):
        """
        Запускает внешнюю программу.
        Результат ее выполнения записывает в Context
        """
        result = subprocess.run([self.name] + self.args, capture_output=True, text=True)
        if result.returncode != 0:
            context.error = Optional.of(result.stderr)
        else:
            context.state = Optional.of(result.stdout)

    def __str__(self):
        return f'Process name: {self.name}, args: {self.args}'

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.name == other.name and self.args == other.args
        return False
