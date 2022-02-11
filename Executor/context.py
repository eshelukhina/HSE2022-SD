from optional import Optional

from Environment.impl import Environment


class Context:
    """
        Stores the execution context of the commands.
    """
    def __init__(self, *, env: Environment = Environment()):
        self.state = Optional.empty()
        self.env = env
