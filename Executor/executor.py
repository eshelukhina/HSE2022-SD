from typing import List

from Executor.context import Context
from Environment.impl import Environment


class Executor:
    def __init__(self):
        self.commands = []
        self.env = Environment()

    shell_terminated = False

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
            output, ret_code = command.execute(context)
            if ret_code != 0:
                return output, ret_code
        return output, ret_code
