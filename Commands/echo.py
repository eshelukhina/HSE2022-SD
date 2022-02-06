class Echo:
    def __init__(self, args):
        """
        :param args:
        """
        self.args = args

    def execute(self, context):
        """
        Output command arguments
        :param context:
        """
        context.state = " ".join(self.args)

    def __str__(self):
        return f'ECHO {self.args}'

    def __eq__(self, other):
        if isinstance(other, Echo):
            return self.args == other.args
        return False
