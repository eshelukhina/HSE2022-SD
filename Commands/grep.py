import argparse
from typing import List, Tuple

from Executor.context import Context


class ArgumentParserError(Exception):
    pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


class Grep:
    """
    TODO написать описание
    """

    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def parse_arguments(self, args):
        parser = ThrowingArgumentParser(exit_on_error=False)
        parser.add_argument("-w", dest="words", action="store_true", default=False)
        parser.add_argument("-i", dest="case_insensitive", action="store_true", default=False)
        parser.add_argument("-A", dest="count", type=int)
        parser.add_argument("pattern")
        parser.add_argument("files", nargs="+")
        return parser.parse_args(args)

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        TODO написать описание
        :returns: Status code
        :rtype: int
        """
        result_of_parsing = self.parse_arguments(self.args)
        # TODO написать реализацию
        return "", 0

    def __str__(self):
        return f'GREP {self.args}'

    def __eq__(self, other):
        if isinstance(other, Grep):
            return self.args == other.args
        return False
