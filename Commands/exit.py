class Exit:
    def __init__(self, args):
        self.args = args

    def execute(self):
        pass

    def __str__(self):
        return f'EXIT {self.args}'

    def __eq__(self, other):
        if isinstance(other, Exit):
            return self.args == other.args
        return False
