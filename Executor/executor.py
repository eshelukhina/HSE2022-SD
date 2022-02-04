from Executor.context import Context


class Executor:
    def __init__(self, commands: list):
        self.commands = commands

    def run(self):
        context = Context(len(self.commands))
        for command in self.commands:
            command.execute(context)
            if len(context.error.getvalue()) != 0:
                # TODO I/O печатает ошибку
                return
            context.current_command += 1
        # TODO Передаем I/O результат
