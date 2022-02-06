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
        context = Context(env_vars=self.env)
        for command in self.commands:
            command.execute(context)
            if context.error:
                return context.state, context.error
        return context.state, context.error
