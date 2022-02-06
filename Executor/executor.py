from typing import List

from optional.nothing import Nothing

from Executor.context import Context


class Executor:
    def __init__(self):
        pass

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
        context = Context(len(self.commands))
        for command in self.commands:
            command.execute(context)
            if context.error.is_present() is True:
                return context.state, context.error
            context.current_command += 1
        return context.state, context.error
