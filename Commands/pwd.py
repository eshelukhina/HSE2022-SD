import os


class Pwd:
    def __init__(self, args):
        self.args = args

    def execute(self, context):
        """
        Get current working directory
        :param context:
        """
        context.state = os.getcwd()

    def __str__(self):
        return f'PWD {self.args}'

    def __eq__(self, other):
        if isinstance(other, Pwd):
            return self.args == other.args
        return False
