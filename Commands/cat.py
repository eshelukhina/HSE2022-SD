from optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Cat:
    """
    Get file contents.
    """

    def __init__(self, args):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> int:
        """
        Check that arguments are paths to existing files.
        Return the contents of these files
        :returns: Status code
        :rtype: int
        """
        for arg in self.args:
            if not FileManager.is_file(arg):
                context.state = Optional.of(f'cat: no such file {arg}')
                return 2
        if len(self.args) > 0:
            result = ''.join([FileManager.get_file_content(arg) for arg in self.args])
        else:
            if context.state.is_empty():
                context.state = Optional.of("wc: empty input")
                return 1
            result = ''.join(context.state.get())
        context.state = Optional.of(result)
        return 0

    def __str__(self):
        return f'CAT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.args == other.args
        return False
