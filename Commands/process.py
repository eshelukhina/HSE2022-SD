class Process:
    def __init__(self, *, name, args):
        self.name = name
        self.args = args

    def execute(self):
        pass

    def __str__(self):
        return f'Process name: {self.name}, args: {self.args}'

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.name == other.name and self.args == other.args
        return False
