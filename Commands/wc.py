class Wc:
    def __init__(self, args):
        self.args = args

    def execute(self):
        pass

    def __str__(self):
        return f'WC {self.args}'

    def __eq__(self, other):
        if isinstance(other, Wc):
            return self.args == other.args
        return False
