from typing import List

from Executor.context import Context
from Environment.impl import Environment


class Executor:
    """
    Sequentially executes the given commands.
    """

    def __init__(self):
        self.commands = []
        self.env = Environment()

    is_shell_terminated = False

    def set_commands(self, commands: List):
        """
        Set the sequence of commands
        :param commands: list of commands
        """
        self.commands = commands

    def run(self):
        """
        Executes the sequence of commands
        """
        if not self.commands:
            return '', 0

        context = Context(env=self.env)
        output, ret_code = None, None
        for command in self.commands:
            Executor.is_shell_terminated = False
            ret_code = command.execute(context)
            if ret_code != 0:
                return context.state, ret_code
        return context.state, ret_code
