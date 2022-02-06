from App.io import IO
from Executor.executor import Executor
from parser.impl import Parser


class App:
    def __init__(self):
        self.io_handler = IO()
        self.parser = Parser()
        self.executor = Executor()

    def run(self):
        """
        Run shell emulator
        """
        while not self.executor.shell_terminated:
            user_input = self.io_handler.read()
            commands = self.parser.parse(input_data=user_input)
            self.executor.set_commands(commands)
            command_output, err_output = self.executor.run()
            self.io_handler.write(command_output, err_output)
