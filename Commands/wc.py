from typing import List, Tuple

from optional.optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Wc:
    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> Tuple[str, int]:
        """
        Check that all arguments are paths to existing files.
        Retrieves the contents of these files and count the number of strings, words, and bytes for each.
        Save the result to the Context
        :returns: command status code
        :rtype: int
        """
        for arg in self.args:
            if not FileManager.is_file(arg):
                return f'wc: no such file {arg}\n', 2
        final_result = []
        for arg in self.args:
            result = []
            file_content = FileManager.get_file_content(arg)

            # Count the number of lines as the number of newline characters
            lines = file_content.count('\n')
            result.append(str(lines))

            # Count the number of words
            words = len(file_content.split())
            result.append(str(words))

            # Transform the contents of the file into bytes and count their number
            num_bytes = len(file_content.encode())
            result.append(str(num_bytes))

            result.append(arg)
            final_result.append(' '.join(result))
        return '\n'.join(final_result) + '\n', 0

    def __str__(self):
        return f'WC {self.args}'

    def __eq__(self, other):
        if isinstance(other, Wc):
            return self.args == other.args
        return False
