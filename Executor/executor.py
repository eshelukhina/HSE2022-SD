from Executor.context import Context


class Executor:
    def __init__(self):
        pass

    def set_commands(self, commands: list):
        """
        Set the sequence of commands
        """
        self.commands = commands

    def run(self):
        """
        Executes the sequence of commands
        """
        context = Context(len(self.commands))
        command_output = []
        for command in self.commands:
            command_output += [command.execute(context)]
            if len(context.error.getvalue()) != 0:
                return command_output, context.error
            context.current_command += 1
        return command_output[-1], context.error
