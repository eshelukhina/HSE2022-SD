from typing import List

from optional.optional import Optional

from Executor.context import Context
from Executor.file_manager import FileManager


class Wc:
    def __init__(self, args: List[str]):
        self.args = args

    def execute(self, context: Context):
        """
        Checks that all arguments are paths to existing files.
        Retrieves the contents of these files and counts the number of strings, words, and bytes for each.
        Saves the result to the Context
        """
        for arg in self.args:
            if not FileManager.is_file(arg):
                context.error = Optional.of(f'wc: {arg}: No such file')
                return
        final_result = []
        for arg in self.args:
            result = []
            file_content = FileManager.get_file_content(arg)

            # Count the number of lines as the number of newline characters
            lines = file_content.count('\n')
            result.append(str(lines))

            # Split the contents of the file into lines, then split the lines by spaces and delete the empty lines
            words = len([y for x in file_content.split('\n') for y in x.split(' ') if y != ''])
            result.append(str(words))

            # Transform the contents of the file into bytes and count their number
            num_bytes = len(file_content.encode())
            result.append(str(num_bytes))

            result.append(arg)
            final_result.append(' '.join(result))
        context.state = Optional.of('\n'.join(final_result))

    def __str__(self):
        return f'WC {self.args}'

    def __eq__(self, other):
        if isinstance(other, Wc):
            return self.args == other.args
        return False
