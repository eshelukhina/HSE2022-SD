from Executor.file_manager import FileManager
from Executor.path_types import PathTypes


class Cat:
    def __init__(self, args):
        """
        :param args: list of file names
        """
        self.args = args

    def execute(self, context):
        """
        Display contents of files
        :param context:
        """
        for arg in self.args:
            file_manager = FileManager(arg)
            file_manager.get_file_type()
            if file_manager.file_type == PathTypes.file:
                context.state = file_manager.get_file_content()
            elif file_manager.file_type == PathTypes.directory:
                context.error = 'cat: Is a directory'
            else:
                context.error = 'cat: No such file or directory'

    def __str__(self):
        return f'CAT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.args == other.args
        return False
