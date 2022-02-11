from App.io import IO
from Executor.executor import Executor
from parser.impl import Parser


class App:
    def __init__(self):
        self.parser = Parser()
        self.executor = Executor()

    def run(self):
        """
        Run shell emulator
        """
        while not self.executor.shell_terminated:
            user_input = IO.read()
            try:
                commands = self.parser.parse(input_data=user_input)
            except ValueError as v_err:
                IO.write(str(v_err))
                continue

            self.executor.set_commands(commands)
            output, ret_code = self.executor.run()
            IO.write(output)
