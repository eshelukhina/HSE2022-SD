import sys


from optional import Optional

from App.io import IO
from Executor.executor import Executor
from parser.substitution import Substitution
from parser.parser import Parser, ParserException


class App:
    """
    Shell emulator.
    """

    def __init__(self):
        self.parser = Parser()
        self.executor = Executor()
        self.substitution = Substitution()
        
    def run(self):
        """
        Run shell emulator
        """
        while not self.executor.is_shell_terminated:
            user_input = None
            while user_input is None:
                try:
                    user_input = IO.read()
                except KeyboardInterrupt:
                    IO.write(Optional.of(''))
                except EOFError:
                    IO.write(Optional.of(''))
                    sys.exit(0)
            try:
                subst_user_input = self.substitution.substitute(user_input)
                commands = self.parser.parse(input=subst_user_input)
            except ParserException as v_err:
                IO.write(Optional.of(v_err))
                continue

            self.executor.set_commands(commands)
            output, ret_code = self.executor.run()
            IO.write(output)
