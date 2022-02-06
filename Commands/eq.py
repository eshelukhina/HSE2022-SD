class Eq:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        pass

    def __str__(self):
        return f'{self.dest} EQ {self.src}'

    def __eq__(self, other):
        if isinstance(other, Eq):
            return self.src == other.src and self.dest == other.dest
        return False
