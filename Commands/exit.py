from Executor.executor import Executor


class Exit:
    def __init__(self, args):
        self.args = args

    def execute(self, context):
        """
        Terminate the current shell
        :param context:
        """
        Executor.shell_terminated = True
        context.state = "Shell is terminated"

    def __str__(self):
        return f'EXIT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Exit):
            return self.args == other.args
        return False
